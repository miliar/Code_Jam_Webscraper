/**
 *    author:  [itmo] enot.1.10
 *    created: 21.01.2017 23:42:28       
**/
#define __USE_MINGW_ANSI_STDIO 0
#include <bits/stdc++.h>

#define F first
#define S second
#define pb push_back
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


const int N = 1010;

char s[N];


int main(int argc, char* argv[])
{
    assert(freopen("1.in", "r", stdin));
    int tn;
    scanf("%d", &tn);
    int testL = 0, testR = tn;
    if (argc == 4)
    {
        sscanf(argv[1], "%d", &testL);
        sscanf(argv[2], "%d", &testR);
        assert(freopen(argv[3], "w", stdout));
    }
    else
    {
        assert(freopen("1.out", "w", stdout));
    }


    forn(tt, tn)
    {
        scanf("%s", s);
        int k;
        scanf("%d", &k);
        
        if (!(testL <= tt && tt < testR)) continue;
        printf("Case #%d: ", tt + 1);
        
        int n = strlen(s);
        int res = 0;
        for (int i = 0; i + k <= n; ++i)
        {
            if (s[i] == '-')
            {
                res++;
                forn(j, k) s[i + j] ^= '-' ^ '+';
            }
        }
        int ok = 1;
        forn(i, n) if (s[i] != '+') ok = 0;
        if (ok) printf("%d\n", res);
        else printf("IMPOSSIBLE\n");

    }
            
    #ifdef home
        eprintf("time = %d ms\n", (int)(clock() * 1000. / CLOCKS_PER_SEC));
    #endif
    return 0;
}
