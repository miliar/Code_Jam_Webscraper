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

int ary[MAX];
int bry[MAX];
int ord[MAX];
int tmp[MAX];

int buf[MAX];

int solve(int ary[], int l, int r)
{
    //printf("%d %d\n", l, r);
    if (l >= r)
        return 0;

    int mid = (l + r) / 2;

    int ans = 0;
    ans += solve(ary, l, mid);
    ans += solve(ary, mid + 1, r);

    int i = l, j = mid + 1, n = l;
    int cj = 0;
    while (i <= mid and j <= r)
    {
        if (ary[i] < ary[j])
        {
            buf[n++] = ary[i++];
            ans += cj;
        }
        else
        {
            buf[n++] = ary[j++];
            cj++;
        }
    }
    while (i <= mid)
    {
        buf[n++] = ary[i++];
        ans += cj;
    }
    while (j <= r)
    {
        buf[n++] = ary[j++];
        cj++;
    }

    for (int k = l; k <= r; ++k)
        ary[k] = buf[k];

    return ans;
}


int main()
{
    int z;
    scanf("%d", &z);

    for (int zi = 1; zi <= z; ++zi)
    {
        fprintf(stderr, "!! %d\n", zi);

        int n; 
        scanf("%d", &n);
        for (int i = 0; i < n; ++i)
            scanf("%d", &ary[i]);

        for (int i = 0; i < n; ++i)
            ord[i] = i;

        int ans = INT_MAX;
        do
        {
            for (int j = 0; j < n; ++j)
                tmp[j] = ord[j];

            int cnt = solve(tmp, 0, n-1);

            for (int i = 0; i < n; ++i)
                bry[i] = ary[ord[i]];

            int flag = 0;
            for (int i = 1; i < n; ++i)
            {
                if (not flag and bry[i-1] < bry[i]) continue;
                if (flag and bry[i-1] > bry[i]) continue;

                flag ++;
            }
            if (flag > 1) continue;

            ans = min(cnt, ans);
        }
        while (next_permutation(ord, ord + n));


        printf("Case #%d: %d\n", zi, ans);
    }
}

