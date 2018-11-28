#include <algorithm>
#include <iostream>
#include <sstream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <complex>
#include <numeric>
#include <bitset>
#include <vector>
#include <string>
#include <queue>
#include <map>
#include <set>

using namespace std;

#define all(a) (a).begin(), (a).end()
#define sz(a) int((a).size())
#define FOR(i, a, b) for (int i(a), _b(b); i < _b; ++i)
#define REP(i, n) FOR (i, 0, n)
#define FORD(i, a, b) for (int i(a), _b(b); i >= _b; --i)
#define UN(a) sort(all(a)), (a).erase(unique(all(a)), (a).end())
#define CL(a, v) memset(a, v, sizeof a)
#define pb push_back
#define X first
#define Y second

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef vector<pii> vpii;

const int INF = 1000000000;
const ll INF_LL = 1000000000000000000LL;
const double pi = 2 * acos(0.0);

template<class T> void smin(T& a, T b) { if (a > b) a = b; }
template<class T> void smax(T& a, T b) { if (a < b) a = b; }
template<class T> T gcd(T a, T b) { return b == 0 ? a : gcd(b, a % b); }
template<class T> T sqr(T a) { return a * a; }

template<class T> void outp(const vector<T>& v) {
    REP(i, sz(v)) cout << v[i] << (i + 1 == sz(v) ? '\n' : ' ');
}
template<class T> void outp(T* v, int n) {
    REP(i, n) cout << *v++ << (i + 1 == n ? '\n' : ' ');
}

const int N = 105;
const int H = 105;

int a[N][N];
int test;
int n, m;
vpii levels[H];

int main() {
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
    scanf("%d", &test);
    FOR (t, 1, test + 1) {
        REP(i, H)
            levels[i].clear();
        scanf("%d%d", &n, &m);
        REP(i, n)
            REP(j, m) {
                scanf("%d", &a[i][j]);
                levels[a[i][j]].pb(pii(i, j));
            }
        string res = "YES";
        REP(k, H) {
            REP(l, sz(levels[k])) {
                int i = levels[k][l].X;
                int j = levels[k][l].Y;
                bool flag_hor = 1;
                REP(p, m)
                    flag_hor &= (a[i][p] <= a[i][j]);
                bool flag_ver = 1;
                REP(p, n)
                    flag_ver &= (a[p][j] <= a[i][j]);
                if (!flag_hor && !flag_ver) {
                    res = "NO";
                    break;
                }
            }
            if (res != "YES") break;
        }
        printf("Case #%d: %s\n", t, res.c_str());
    }
    cerr << endl << endl << "TIME: " << clock() << endl;
    return 0;
}
