/* --- Author: Vladimir Smykalov, enot.1.10@gmail.com --- */
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

using namespace std;

typedef long long ll;
typedef double ld;
typedef vector<int> vi;
typedef pair<int, int> pi;

const int inf = (int)1e9;
const ld eps = 1e-9;

/* --- main part --- */

#define TASK "a"

const int maxn = (int)110;
int a[maxn][maxn];
int row[maxn], col[maxn];

int main()
{
    #ifdef home
        assert(freopen(TASK".in", "r", stdin));
        assert(freopen(TASK".out", "w", stdout));
    #endif
    int tn;
    scanf("%d", &tn);
    forn(_, tn)
    {
        printf("Case #%d: ", _ + 1);
        int n, m;
        scanf("%d%d", &n, &m);
        forn(i, n) forn(j, m) scanf("%d", &a[i][j]);
        forn(i, n)
        {
            row[i] = 0;
            forn(j, m) row[i] = max(row[i], a[i][j]);
        }
        forn(i, m)
        {
            col[i] = 0;
            forn(j, n) col[i] = max(col[i], a[j][i]);
        }
        bool ok = true;
        forn(i, n) forn(j, m) if(a[i][j] < min(row[i], col[j])) ok = false;
        if(ok) printf("YES\n");
        else printf("NO\n");
    }
    #ifdef home
        eprintf("Time: %d ms\n", (int)(clock() * 1000. / CLOCKS_PER_SEC));
    #endif
    return 0;
}
 