#include<cstdlib>
#include<algorithm>
#include<cstring>
#include<iostream>
#include<cstdio>
#include<vector>
#include<map>
#include<cmath>

#define maxn 100000000
using namespace std;
const int cnt_pri = 25;

int prime[100];
int bit_mod[11][32][cnt_pri];
int bit_div[11];
int bit[32];
int vis[maxn];
int n;

void sieve(int num)
{
    int m = (int)sqrt(num+0.5);
    memset(vis, 0, sizeof(vis));
    for (int i=2;i<=m;i++) if (!vis[i])
        for (int j=i*i;j<=n;j+=i) vis[j] = 1;
}

void get_pri(int k)
{
    sieve(maxn);
    int c =0;
    for (int i=2;i<=maxn;i++)
        if (!vis[i])
        {
            prime[c++] = i;
            if (c == k) return;
        }
}

void getbit(int num)
{
    bit[0] = 1;
    for (int i=1;i<=n-2;i++)
    {
        bit[i] = num % 2;
        num = num / 2;
    }
    bit[n-1] = 1;
}

bool judge()
{
    for (int i=2;i<=10;i++)
    {
        bool f = false;
        for (int k=0;k<cnt_pri;k++)
        {
            int ret = 0;
            for (int j=0;j<n;j++)
                if (bit[j] == 1) ret = (ret + bit_mod[i][j][k]) % prime[k];
            if (ret % prime[k] == 0)
            {
                bit_div[i] = prime[k];
                f = true;
                break;
            }
        }
        if (!f) return false;
    }
    return true;
}
int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("ans.out", "w", stdout);
    get_pri(cnt_pri);

    for (int i=2;i<=10;i++)
        for (int k=0;k<cnt_pri;k++)
        bit_mod[i][0][k] = 1;

    for (int i=2;i<=10;i++)
        for (int j=1;j<32;j++)
            for (int k=0;k<cnt_pri;k++)
            bit_mod[i][j][k] = (bit_mod[i][j-1][k] * i) % prime[k];

    int T;
    scanf("%d", &T);
    for (int kase=1;kase<=T;kase++)
    {
        printf("Case #%d:\n", kase);
        int j;
        scanf("%d%d", &n, &j);
        int cnt = 1;
        int num = 0;
        while (cnt <= j)
        {
            getbit(num);
            if (judge())
            {
                printf("1");
                for (int i=n-2;i>=1;i--) printf("%d", bit[i]);
                printf("1");
                for (int i=2;i<=10;i++)
                    printf(" %d", bit_div[i]);
                printf("\n");
                cnt++;
            }
            num++;
        }
    }
    return 0;
}
