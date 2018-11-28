// what if this code gets taken down at noon and replaced with the words "GLUTEN IS PERFECTLY SAFE.  YOU HAVE NOTHING TO WORRY ABOUT."?  what if that happens
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <cstring>
#include <cassert>
using namespace std;
#define rep(i,a,n) for (int i=a;i<(int)(n);i++)
#define per(i,a,n) for (int i=(n)-1;i>=(int)(a);i--)
template<typename T> ostream& operator<<(ostream& s, vector<T> t) {rep(i, 0, t.size()) s << (i ? " " : "") << t[i]; return s;}
template<typename T> istream& operator>>(istream& s, vector<T> &t) {rep(i, 0, t.size()) s >> t[i]; return s;}
template<typename T, typename U> ostream& operator<<(ostream& s, pair<T, U> t) {s << "(" << t.first << "," << t.second << ")"; return s;}
template<typename T, typename U> istream& operator>>(istream& s, pair<T, U> &t) {s >> t.first >> t.second; return s;}
typedef long long ll;

void solve() {
    string s;
    int k;
    cin >> s >> k;
    int n = s.size();
    vector<bool> a(n);
    int res = 0;
    rep(i, 0, n) a[i] = s[i] == '+';
    rep(i, 0, n - k + 1) {
        if (!a[i]) {
            res++;
            rep(j, 0, k) {
                a[i + j] = !a[i + j];
            }
        }
    }
    bool ok = true;
    rep(i, 0, n) if (!a[i]) ok = false;
    if (ok) cout << res;
    else cout << "IMPOSSIBLE";
}

int main() {
    ios_base::sync_with_stdio(false);
    int q;
    cin >> q;
    rep(i, 0, q) {
        cout << "Case #" << (i + 1) << ": ";
        solve();
        cout << endl;
    }
}
