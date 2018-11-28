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

const int P = 1000002013;
const int rev2 = (P + 1) >> 1;

const int maxn = (int)1e4 + 10;
pi e[maxn]; 
int n, m, ec = 0;

inline int mult(int a, int b)
{
    return (a * (ll)b) % P;
}
inline int GET(int x)
{
    return (n * (ll)x - mult(mult(x, x - 1), rev2) + P) % P;
}

pi st[maxn];
int stc = 0;

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
        scanf("%d%d", &n, &m);
        ec = 0, stc = 0;
        ll RES1 = 0;
        forn(i, m)
        {
            int a, b, p;
            scanf("%d%d%d", &a, &b, &p);
            RES1 += mult(GET(b - a), p);
            e[ec++] = mp(a, -p);
            e[ec++] = mp(b, p);
        }
        RES1 %= P;
        sort(e, e + ec);
        ll RES2 = 0;
        forn(i, ec)
        {
            if(e[i].sc < 0)
            {
                st[stc++] = mp(e[i].fs, -e[i].sc);
            }
            else
            {
                while(st[stc - 1].sc < e[i].sc)
                {
                    RES2 += mult(GET(e[i].fs - st[stc - 1].fs), st[stc - 1].sc);
                    e[i].sc -= st[stc - 1].sc; 
                    stc -= 1;
                }
                RES2 += mult(GET(e[i].fs - st[stc - 1].fs), e[i].sc);
                st[stc - 1].sc -= e[i].sc;
                if(st[stc - 1].sc == 0) stc -= 1;
            }
        }
        RES2 %= P;
        printf("%d\n", (int)((RES1 - RES2 + P) % P));
    }
                     
    #ifdef home
        eprintf("Time: %d ms\n", (int)(clock() * 1000. / CLOCKS_PER_SEC));
    #endif
    return 0;
}
 