/**
 *    author:  itmo1
 *    created: 11.06.2016 18:58:08       
**/
#define __USE_MINGW_ANSI_STDIO 0
#include <bits/stdc++.h>

#define F first
#define S second
#define pb push_back
#define mp make_pair
#define forn(i, n) for(int i = 0 ; (i) < (n) ; ++i)
#define eprintf(...) fprintf(stderr, __VA_ARGS__),fflush(stderr)
#define sz(a) ((int)(a).size())
#define all(a) (a).begin(),a.end()
#define pw(x) (1LL<<(x))

using namespace std;

typedef long long ll;
typedef double dbl;
typedef vector<int> vi;
typedef pair<int, int> pi;

const int inf = 1.01e9;
const dbl eps = 1e-9;

/* --- main part --- */

const int N = 210;

char bad[N];
char s[N][N];

char r[N];
char z[N];



int main()
{
    #ifdef home
        assert(freopen("1.in", "r", stdin));
        assert(freopen("1.out", "w", stdout));
    #endif
    int tn;
    scanf("%d", &tn);
    forn(tt, tn)
    {
        printf("Case #%d: ", tt + 1);
        int n, l;
        scanf("%d%d", &n, &l);    
        forn(i, n) scanf("%s", s[i]);
        scanf("%s", bad);
        int ok = 1;
        forn(i, n)
        {
            ok = 0;
            forn(j, l) if (s[i][j] != bad[j]) ok = 1;
            if (!ok) break;
        }
        if (!ok)
        {
            printf("IMPOSSIBLE\n");
            continue;
        }
        int rc = 0;
        int zc = 0;
        forn(i, l)
        {
            if (bad[i] == '0')
            {
                r[rc++] = '1';
                r[rc++] = '?';
                z[zc++] = '0';
            }
            else
            {
                r[rc++] = '0';
                r[rc++] = '?';
                z[zc++] = '1';
            }
        }
        z[zc - 1] = '0' + '1' - z[zc - 1];
        z[zc] = 0;
        r[rc] = 0;
        printf("%s %s\n", r, z);
    }
            
                


    #ifdef home
        eprintf("time = %d ms\n", (int)(clock() * 1000. / CLOCKS_PER_SEC));
    #endif
    return 0;
}
