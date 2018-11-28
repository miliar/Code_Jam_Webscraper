/* --- author: enot-the-rockstar ---*/
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <ctime>
#include <cassert>

#define fs first
#define sc second
#define pb push_back
#define mp make_pair
#define forn(i, n) for(int i = 0 ; (i) < (n) ; ++i)
#define forit(it,v) for(typeof((v).begin()) it = v.begin() ; it != (v).end() ; ++it)
#define eprintf(...) fprintf(stderr, __VA_ARGS__),fflush(stderr)
#define sz(a) ((int)(a).size())
#define all(a) (a).begin(),a.end()

static inline unsigned long long rdtsc() { unsigned long long d; __asm__ __volatile__ ("rdtsc" : "=A" (d) ); return d; }

using namespace std;

typedef long long ll;
typedef double dbl;
typedef vector<int> vi;
typedef pair<int, int> pi;

const int inf = (int)1e9;
const dbl eps = 1e-9;

/* --- main part --- */

#define TASK "a"

const int maxn = 110;

char s[maxn][maxn];

char dd[4] = {'>', '<', '^', 'v'};
int dx[4] = {0, 0, -1, 1};
int dy[4] = {1, -1, 0, 0};
int n, m;

inline bool in(int x, int y)
{
    return 0 <= x && x < n && 0 <= y && y < m;
}

bool ok;
int col[maxn];
int row[maxn];
void check(int x, int y)
{
    if (col[y] + row[x] == 2)
    {
        ok = false;
    }
}

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
        scanf("%d%d", &n, &m);
        forn(i, n) scanf("%s", s[i]);
        int res = 0;
        ok = true;
        forn(i, n) row[i] = 0;
        forn(j, m) col[j] = 0;
        forn(i, n) forn(j, m) if (s[i][j] != '.') row[i] += 1, col[j] += 1;
        forn(i, n) forn(j, m) if (s[i][j] != '.')
        {
            forn(k, 4) if (s[i][j] == dd[k])
            {
                int i2 = i, j2 = j;
                while (1)
                {
                    i2 += dx[k];
                    j2 += dy[k];
                    if (!in(i2, j2))
                    {
                        res += 1;
                        check(i, j);
                        break;
                    }
                    if (s[i2][j2] != '.') break;
                }
            }
        }
        if (ok) printf("%d\n", res);
        else printf("IMPOSSIBLE\n");
    }
    #ifdef home
        eprintf("Time: %d ms\n", (int)(clock() * 1000. / CLOCKS_PER_SEC));
    #endif
    return 0;
}
 