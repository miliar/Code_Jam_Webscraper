#include <stdio.h>
#include <map>
#include <string.h>

using namespace std;

const int maxn = 50;

int key[maxn][50];
int need[maxn], kn[maxn];
int start[50];

int f[1<<20];
bool flag[1<<20];
int n, k;
int ans[maxn];

map<int, int> have;

void dp()
{
    int sta, i, j;
    memset(f, 0, sizeof(f));
    f[0] = 1<<n;
    for (sta = 0; sta < (1<<n); sta++) if (f[sta]>0)
    {
        have.clear();
        for (i=0; i<k; i++)
            have[start[i]]++;
        for (i=0; i<n; i++)
            if ((sta>>i)&1)
        {
            have[need[i]]--;
            for (j=0; j<kn[i]; j++)
            have[key[i][j]]++;
        }
        for (i=0; i<n; i++)
            if (((sta>>i)&1)==0 && have[need[i]]>0)
                f[sta|(1<<i)] |= 1<<i;
    }
}

void build_ans()
{
    int sta, i, j;
    memset(flag, false, sizeof(flag));
    flag[(1<<n)-1] = true;
    for (sta = (1<<n) - 1; sta > 0; sta--)
        if (flag[sta])
        {
            for (i=0; i<n; i++)
                if ((f[sta]>>i)&1)
                    flag[sta - (1<<i)] = true;
        }
    sta = 0;
    for (i = 0; i < n; i++)
    {
        for (j=0; j<n; j++)
            if (flag[sta|(1<<j)] && (((sta>>j)&1)==0) && (f[sta|(1<<j)]>>j)&1) break;
        ans[i] = j + 1;
        sta |= 1<<j;
    }
}

int main()
{
    //freopen("B-large.in", "r", stdin);
    freopen("D-small-attempt2.in", "r", stdin);
    freopen("dout.txt", "w", stdout);
    int T, i, j, sta;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++)
    {
        scanf("%d%d", &k, &n);
        for (i=0; i<k; i++)
             scanf("%d", &start[i]);
        for (i=0; i<n; i++)
        {
            scanf("%d%d", &need[i], &kn[i]);
            for (j=0; j<kn[i]; j++)
                scanf("%d", &key[i][j]);
        }
        dp();
        if (f[(1<<n)-1]!=0)
        {
            build_ans();
            printf("Case #%d:", cas);
            for (i=0; i<n; i++)
                printf(" %d", ans[i]);
            printf("\n");
        }
        else printf("Case #%d: IMPOSSIBLE\n", cas);
    }
    return 0;
}
