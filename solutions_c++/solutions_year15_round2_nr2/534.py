/**
 *    author:  enot.1.10, Vladimir Smykalov (enot.1.10@gmail.com)
 *    created: 02.05.2015 19:39:47       
**/
#include <bits/stdc++.h>

#define forn(i, n) for(int i = 0 ; (i) < (n) ; ++i)
#define eprintf(...) fprintf(stderr, __VA_ARGS__),fflush(stderr)

using namespace std;

typedef long long ll;
typedef double dbl;

const int inf = (int)1.01e9;
const dbl eps = 1e-9;

/** --- main part --- **/

#define TASK "a"

const int maxn = (int)1e4 + 10;

#define fs first
#define sc second
#define mp make_pair
typedef pair<int, int> pi;


int n, m;

int a[maxn];
int inn[maxn];
set<pi> S;

int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

#define forit(it,v) for(typeof((v).begin()) it = v.begin() ; it != (v).end() ; ++it)


inline bool in(int x, int y)
{
    return 0 <= x && x < n && 0 <= y && y < m;
}

#define pb push_back
#define sz(a) ((int)(a).size())
#define all(a) (a).begin(),a.end()
typedef vector<int> vi;


vector<vi> v;

int main()
{
    #ifdef home
        assert(freopen(TASK".in", "r", stdin));
        assert(freopen(TASK".out", "w", stdout));
    #endif
    int tn;
    scanf("%d", &tn);
    forn(tt, tn)
    {
        printf("Case #%d: ", tt + 1);
        int T;
        scanf("%d%d%d", &n, &m, &T);
        v = vector<vi>(n);
        forn(i, n) v[i] = vi(m, 0);
        int res = inf;
        forn(M, 1 << (n * m))
        {
            int xx = 0;
            forn(i, n) forn(j, m) v[i][j] = (M >> (i * m + j)) & 1;
            forn(i, n) forn(j, m) xx += v[i][j];
            if (xx != T) continue;
            int cnt = 0;
            forn(i, n) forn(j, m)
            {
                forn(k, 4)
                {
                    int i2 = i + dx[k];
                    int j2 = j + dy[k];
                    if (in(i2, j2) && v[i][j] && v[i2][j2]) cnt += 1;
                }
            }
            cnt >>= 1;
            res = min(res, cnt);
        }
        printf("%d\n", res);
        forn(i, n) v[i].clear();
        v.clear();
    }
    #ifdef home
        eprintf("Time: %d ms\n", (int)(clock() * 1000. / CLOCKS_PER_SEC));
    #endif
    return 0;
}
 