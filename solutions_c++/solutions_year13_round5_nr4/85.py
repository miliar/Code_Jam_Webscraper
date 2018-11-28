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
typedef long  double ld;
typedef vector<int> vi;
typedef pair<int, int> pi;

const int inf = (int)1e9;
const ld eps = 1e-14;

/* --- main part --- */

#define TASK "a"

const int N = 20;
ld p[1 << N];
ld a[1 << N];

char s[N + 1];

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
        memset(a, 0, sizeof a);
        memset(p, 0, sizeof p);
        printf("Case #%d: ", _ + 1);
        scanf("%s", s);
        int n = strlen(s);
        int mask = 0;
        forn(i, n) if(s[i] == 'X') mask |= 1 << i;
        p[mask] = 1;
        a[mask] = 0;
        forn(m, (1 << n) - 1)
        {
            if(p[m] < eps) continue;
            a[m] /= p[m];
            forn(i, n)
            {
                int j = i;
                int cc = n;
                while((m & (1 << j)) > 0)
                {
                    cc -= 1;
                    j += 1;
                    if(j == n) j = 0;
                }
                p[m | (1 << j)] += p[m] / n;
                a[m | (1 << j)] += (p[m] / n) * (a[m] + cc);
            }
        }
        printf("%.18lf\n", (double)a[(1 << n) - 1]);
    }
                

    #ifdef home
        eprintf("Time: %d ms\n", (int)(clock() * 1000. / CLOCKS_PER_SEC));
    #endif
    return 0;
}
 