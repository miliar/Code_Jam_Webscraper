#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <functional>
#include <iostream>
#include <iomanip>
#include <iterator>
#include <map>
#include <queue>
#include <utility>
#include <vector>

using namespace std;

typedef long long Long;
#define whole(xs) xs.begin(), xs.end()

ostream& operator<<(ostream& os, const vector<int>& v) {
    for (int i = 0; i < v.size(); i++) os << v[i] << " ";
    return os;
}

struct BIT {
    typedef int T;
    static const T Tinit = 0;
    static T op(const T& x, const T& y) {
        return x + y;
    }
    static T rop(const T& x, const T& y) {
        return x - y;
    }
    
    T n;
    T* bit;
    BIT(int n) {
        this->n = n;
        bit = new T[n + 1];
        for (int i = 0; i <= n; i++) bit[i] = Tinit;
    }
    ~BIT() {
        delete[] bit;
    }
    void apply(int i, T x) {
        i++;
        while (i <= n) {
            bit[i] = op(x, bit[i]);
            i += i & -i;
        }
    }
    T query(int i) {
        i++;
        T s = 0;
        while (i > 0) {
            s = op(s, bit[i]);
            i -= i & -i;
        }
        return s;
    }
};


int N;
vector<int> A;
vector<int> B;

void input() {
    cin >> N;
    A.resize(N, 0);
    for (int i = 0; i < N; i++) {
        cin >> A[i];
    }
    B.clear();
}

int MaxIndex() {
    int Max = 0;
    for (int i = 0; i < A.size(); i++) {
        Max = max(Max, A[i]);
    }
    for (int i = 0; i < A.size(); i++) {
        if (A[i] == Max) {
            return i;
        }
    }
    assert(0);
}

int Count(vector<int>& v) {
    int Ret = 0;
    for (int i = 0; i < v.size(); i++) {
        for (int j = i + 1; j < v.size(); j++) {
            if (v[i] > v[j]) Ret++;
        }
    }
    /*
    BIT bit(v.size());
    for (int i = 0; i < v.size(); i++) {
        Ret += i - bit.query(v[i]);
        bit.apply(v[i], 1);
    }
    */
    return Ret;
}

int CountR(vector<int>& v) {
    reverse(v.begin(), v.end());
    int Ret = Count(v);
    reverse(v.begin(), v.end());
    return Ret;
}

void Compress(vector<int>& v) {
    vector<int> v1 = v;
    sort(whole(v1));
    map<int, int> Map;
    for (int i = 0; i < v1.size(); i++) {
        Map[ v1[i] ] = i;
    }
    for (int i = 0; i < v.size(); i++) {
        v[i] = Map[ v[i] ];
    }
}

void solve() {
    int Ans = (1 << 28);
    Compress(A);
    for (int bit = 0; bit < (1 << N); bit++) {
        vector<int> a, b;
        vector<int> c(N, 0);
        for (int i = 0; i < N; i++) {
            if (bit & (1 << i)) {
                c[i] = 1;
                a.push_back(A[i]);
            } else {
                c[i] = 0;
                b.push_back(A[i]);
            }
        }
        /*
        cerr << "a: " << a << endl;
        cerr << "b: " << b << endl;
        cerr << Count(a) << " " <<  CountR(b) << " " <<  CountR(c) << endl;
        */
        Ans = min(Ans, Count(a) + CountR(b) + CountR(c));
    }
    cout << Ans << endl;
}

int main() {
    int T; cin >> T;
    for (int t = 1; t <= T; t++) {
        cerr << "Case #" << t << endl;
        input();
        cout << "Case #" << t << ": ";
        solve();
    }
    return 0;
}
