#include <cassert>
#include <cstdio>
#include <iostream>
#include <sstream>
#include <numeric>
#include <bitset>
#include <vector>
#include <set>
#include <string>
#include <map>
#include <cmath>
#include <algorithm>
#include <queue>
#include <cstdlib>
#include <functional>
#include <cstring>
#include <ctime>
#include <memory.h>

#define y1 AAA_BBB
#define y0 AAA_AAA

#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; --i)
#define fore(i, a, b) for(int i = (int)(a); i <= (int)(b); ++i)
#define for1(i, n) for(int i = 1; i <= (int)(n); ++i)
#define all(v) (v).begin(), (v).end()

using namespace std;

typedef long long i64;
typedef unsigned long long u64;
typedef long double ld;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef vector<pii> vpi;
typedef vector<vi> vvi;

template <class T> T inline sqr(T x) {
        return x * x;
}

const ld pi = 3.1415926535897932384626433832795;
const ld eps = 1e-8;

map<char, int> dirs = {{'>', 0}, {'^', 1}, {'<', 2}, {'v', 3}};
const int di[4] = {0, -1, 0, 1};
const int dj[4] = {1, 0, -1, 0};
const int N = 110;
int a[N][N];

bool isIn(int x, int r)
{
    return 0 <= x && x < r;
}

void solve()
{
    int n, m;
    cin >> n >> m;
    forn (i, n)
        forn (j, m) {
            char symb;
            cin >> symb;
            if (dirs.count(symb))
                a[i][j] = dirs[symb];
            else
                a[i][j] = -1;
        }
    int ans = 0;
    forn(i, n)
        forn (j, m) if (a[i][j] != -1) {
            vector<char> avail(4, 0);
            forn (dir, 4) {
                int ci = i + di[dir], cj = j + dj[dir];
                bool stop = false;
                while (isIn(ci, n) && isIn(cj, m)) {
                    if (a[ci][cj] != -1) {stop = true; break;}
                    ci += di[dir]; cj += dj[dir];
                }
                if (stop) {
                    avail[dir] = true;
                }
            }
            int sum = 0; for (int x: avail) sum += x;
            if (!sum) {
                cout << "IMPOSSIBLE";
                return;
            }
            if (!avail[a[i][j]])
                ans++;
        }
    cout << ans;
}

int main()
{
#ifdef HOME
    //freopen("a.in", "r", stdin);
    freopen("A-large.in", "r", stdin); 
    freopen("output.txt", "w", stdout);
#endif
    int T;
    cin >> T;
    for1 (t, T)
    {
        cout << "Case #" << t << ": ";
        solve();
        cout << "\n";
    }
    return 0;
}
