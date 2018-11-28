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

const int maxn = (int)1e6 + 10;
char s[maxn];
int BAD[256];
int a[maxn];
int sum[maxn];
int good[maxn];
int next[maxn];

int main()
{
    #ifdef home
        assert(freopen(TASK".in", "r", stdin));
        assert(freopen(TASK".out", "w", stdout));
    #endif
    BAD[(int)'a'] = 1;
    BAD[(int)'e'] = 1;
    BAD[(int)'i'] = 1;
    BAD[(int)'o'] = 1;
    BAD[(int)'u'] = 1;
    int tn;
    scanf("%d", &tn);
    forn(_, tn)
    {
        memset(good, 0, sizeof good);

        printf("Case #%d: ", _ + 1);
        int k;
        scanf("%s%d", s, &k);
        int n = strlen(s);
        ll res = 0;
        forn(i, n) a[i] = BAD[(int)s[i]] ^ 1;
        sum[0] = 0;
        forn(i, n) sum[i + 1] = sum[i] + a[i];
        forn(i, n - k + 1) if(sum[i + k] - sum[i] == k) good[i] = 1;
        next[n] = inf;
        for(int i = n - 1 ; i >= 0 ; i--)
        {
            next[i] = next[i + 1];
            if(good[i]) next[i] = i;
        }
        forn(i, n)
        {
            int j = next[i] + k;
            if(j < inf) res += n - j + 1;
        }
        printf("%I64d\n", res);
    }

    #ifdef home
        eprintf("Time: %d ms\n", (int)(clock() * 1000. / CLOCKS_PER_SEC));
    #endif
    return 0;
}
 