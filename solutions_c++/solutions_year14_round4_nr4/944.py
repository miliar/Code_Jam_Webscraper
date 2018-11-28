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

#define MAX 1005
#define NMAX 105
#define LMAX 105

char str[MAX][LMAX];
int choose[MAX];
int ans, ans2;

int n, m;

int lcp(const string& a, const string& b)
{
    int len = min(a.size(), b.size());

    for (int i = 0; i < len; ++i)
        if (a[i] != b[i])
            return i;
    return len;
}

int count(const vector<string>& v)
{
    int cnt = 0;
    for (int i = 0; i < SZ(v); i++)
    {
        const string& sa = v[i];

        int ma = 0;
        for (int j = 0; j < i; ++j)
        {
            const string& sb = v[j];

            ma = max(ma, lcp(sa, sb));
        }
        cnt += sa.size() - ma;
    }
    return cnt + 1;
}

void dfs(int now)
{
    if (now == 0)
    {
        vector<string> s[NMAX];

        for (int i = 1; i <= n; ++i)
            s[choose[i]].PB(str[i]);

        int cnt = 0;
        for (int i = 0; i < m; ++i)
        {
            if (SZ(s[i]) == 0) return;

            cnt += count(s[i]);
        }

        if (cnt > ans)
            ans = cnt, ans2 = 0;
        if (cnt == ans)
            ans2 ++;

        return ;
    }

    for (int i = 0; i < m; ++i)
    {
        choose[now] = i; 
        dfs(now - 1);
    }
}

int main()
{
    int z;
    scanf("%d", &z);

    for (int zi = 1; zi <= z; ++zi)
    {
        fprintf(stderr, "%d\n", zi);
        scanf("%d %d", &n, &m);
        for (int i = 1; i <= n; ++i)
            scanf("%s", str[i]);

        ans = -1;
        dfs(n);

        printf("Case #%d: %d %d\n", zi, ans, ans2);
    }
}

