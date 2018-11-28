// macros {{{
#include <bits/stdc++.h>

using namespace std;

#define ALL(x) (x).begin(), (x).end()
#define SZ(x) ((int)(x).size())
#define BIT(n) ((1LL) << (long long)(n))
//#define FOR(i,c) for (auto i=(c).begin(); i != (c).end(); ++i)
//#define REP(i,n) for (int i = 0; i < (int)(n); ++i)
//#define REP1(i,a,b) for (int i=(int)(a); i <= (int)(b); ++i)
#define MP make_pair
#define MT make_tuple
#define PB push_back
#define PF push_front

#ifdef WIN32
#define LLD "%I64d"
#else
#define LLD "%lld"
#endif

typedef long long ll;
typedef unsigned int uint;
typedef unsigned long long ull;
typedef long double ld;

typedef pair<int, int> PII;
typedef vector<int> VI;

#define runtime() ((double)clock() / CLOCKS_PER_SEC)

const double eps = 1e-7;
// }}}

#define MAX 705

int ct[MAX];

int main()
{
    int z;
    scanf("%d", &z);

    for (int zi = 1; zi <= z; ++zi)
    {
        int n, m;
        scanf("%d %d", &n, &m);

        memset(ct, 0, sizeof(ct));
        for (int i = 0; i < n; ++i)
        {
            int t;
            scanf("%d", &t);
            ct[t]++;
        }

        int ans = 0;
        for (int i = m; i > 0; --i)
        {
            while (ct[i] > 0)
            {
                ct[i]--;

                for (int j = i; j > 0; --j)
                    if (ct[j] > 0 and i + j <= m)
                    {
                        ct[j]--;
                        break;
                    }

                ans++;
            }
        }
        printf("Case #%d: %d\n", zi, ans);

    }
}

