/**
 *    author:  itmo1
 *    created: 11.06.2016 17:03:53       
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

const int N = 1e5 + 10;

char s[N];
char r[N];
int rc = 0;

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
        scanf("%s", s);
        rc = 0;
        int n = strlen(s);
        int res = 0;
        forn(i, n)
        {
            if (rc > 0 && s[i] == r[rc - 1])
            {
                res += 10;
                rc--;
            }
            else
            {
                r[rc++] = s[i];
            }
        }
        res += rc / 2 * 5;
        printf("Case #%d: %d\n", tt + 1, res);
    }

                
    #ifdef home
        eprintf("time = %d ms\n", (int)(clock() * 1000. / CLOCKS_PER_SEC));
    #endif
    return 0;
}
