#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <set>
#include <map>
#include <unordered_map>
#include <unordered_set>

#define hmap unordered_map
#define hset unordered_set
#define ll long long
#define mkveci mkvec<int>
#define vpri vpr<int>
#define forn(i, n) for (int i = 0; i < (n); ++i)
#define ford(i, n) for (int i = (n) - 1; i >= 0; --i)

using namespace std;


template<class T>
istream& operator >> (istream& in, vector<T>& v) {
    for (size_t i = 0; i < v.size(); ++i) {
        in >> v[i];
    }
    return in;
}

template<class T>
ostream& operator << (ostream& out, const vector<T>& v) {
    for (size_t i = 0; i < v.size(); ++i) {
        out << v[i];
    }
    return out;
}

template<class T>
vector<T> mkvec(int n) {
    return vector<T>(n);
}

template<class T>
vector<vector<T> > mkvec(int n, int m) {
    return vector<vector<T> >(n, vector<T>(m));
}

template<class T>
vector<vector<vector<T> > > mkvec(int n, int m, int k) {
    return vector<vector<vector<T> > >(n, vector<vector<T> >(m, vector<T>(k)));
}

template<class T>
class vpr {
  public:
    vpr(const vector<T>& v, const string& sep)
        : vec1(v)
        , sep1(sep) {
    }

    const vector<T>& vec1;
    const string& sep1;

};

template<class T>
ostream& operator << (ostream& out, const vpr<T>& pr) {
    for (int i = 0; i < pr.vec1.size(); ++i) {
        if (i > 0) {
            out << pr.sep1;
        }
        out << pr.vec1[i];
    }
    return out;
}

void solve();

void runTests() {
    int t;
    cin >> t;
    forn(i, t) {
        cout << "Case #" << i+1 << ": ";
        solve();
        cout << endl;
    }
}

void solve() {
    string f = "RICHARD";
    string s = "GABRIEL";
    int x, rr, cc, r, c;
    cin >> x >> rr >> cc;
    c = min(rr, cc);
    r = max(rr, cc);
    if (x > 6) {
        cout << f;
        return;
    }
    if (r * c % x) {
        cout << f;
        return;
    }
    if (x == 1 || x == 2) {
        cout << s;
        return;
    }
    if ((x + 1) / 2 > c) {
        cout << f;
        return;
    }
    if (x > r) {
        cout << f;
        return;
    }
    if (x == 3) {
        cout << s;
        return;
    }
    if (x == 4) {
        if (c == 2) {
            cout << f;
            return;
        }
        cout << s;
        return;
    }
    if (x == 5) {
        if (c == 3 && r == 5) {
            cout << f;
            return;
        }
        cout << s;
        return;
    }
    if (c == 3) {
        cout << f;
        return;
    }
    cout << s;
    // R x C divisible by X
    // X = 6
    // X-omino can be put inside


}

int main() {
    runTests();
    //sove();
    return 0;
}
