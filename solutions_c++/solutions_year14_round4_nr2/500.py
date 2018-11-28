#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;

class sum {
public:
    vector<int> a;
    int limit;
    int lbt(int x) {
        return x & (-x);
    }
    
    sum(int size) {
        a.clear();
        a.resize(size + 1, 0);
        limit = size + 1;
    }
    void add(int x) {
        for (; x < limit; x += lbt(x))  a[x]++;
    }
    int getsum(int x) {
        int sum = 0;
        for (; x; x -= lbt(x)) sum += a[x];
        return sum;
    }
};

void solve() {
    int N;
    cin >> N;
    vector<int> a(N);
    map<int, int> M;
    for (int i = 0; i < N; i++) {
        cin >> a[i];
        M[a[i]] = 0;
    }
    int loop = 0;
    for (map<int, int> :: iterator ii = M.begin(); ii != M.end(); ii++) 
        ii->second = ++loop;
    for (int i = 0; i < N; i++) {
        a[i] = M[a[i]];
    }

    sum c1(N), c2(N);
    vector<int> v1(N), v2(N);
    for (int i = 0; i < N; i++) {
        v1[i] = i - c1.getsum(a[i]);
        c1.add(a[i]);
    }
    for (int i = N - 1; i >= 0; i--) {
        v2[i] = N - i - 1 - c2.getsum(a[i]);
        c2.add(a[i]);
    }
    int ans = 0;
    for (int i = 0; i < N; i++) {
        ans += min(v1[i], v2[i]);
        //cout << v1[i] << " " << v2[i] << endl;
    }
    cout << ans << endl;
}

int main() {
    int T;
    cin >> T;
    for (int i = 1; i <= T; i++) {
        printf("Case #%d: ", i);
        solve();
    }
}