#include <bits/stdc++.h>
using namespace std;

typedef long long LL;
const int N = 1 << 24;

bool g[N + 10];
int f[50];
int q[11] = {0,0,3,2,5,2,7,2,9,2,11};

int n,m,ans = 0;

void init()
{
    scanf("%d %d",&n,&m);
    f[1] = f[n] = 1;
}

void print()
{
    ans++;//cout<<ans<<endl;
    for(int i = 1;i <= n;i++) printf("%d",f[i]);
    for(int i = 2;i <= 10;i++) printf(" %d",q[i]);
    printf("\n");

  /*  LL sign = 0;
    for(LL i = 2;i <= 9;i++)
    {
        LL j = 0;
        for(LL k = 1;k <= n;k++)
          j = j * i + 1LL * f[k] * 1LL;
        cout<<j<<" ";
        if(j % (1LL * q[i] * 1LL) != 0LL) sign = i;
    }
    cout<<endl<<sign;
    printf("\n");*/
}

void dfs(int now,int x1,int x2,int p1,int p2)
{
    if(ans >= m) return;

    if(x1 + p1 < x2 || x2 + p2 < x1) return;

    if(p1 == 0 && p2 == 0)
    {
        if(x1 == x2) print();
        return;
    }

    if(now % 2 == 1)
    {
        f[now] = 0;
        dfs(now + 1,x1 ,x2 ,p1 - 1,p2);
        f[now] = 1;
        dfs(now + 1,x1 + 1,x2,p1 - 1,p2);
    }
    else
    {
        f[now] = 0;
        dfs(now + 1,x1,x2,p1,p2 - 1);
        f[now] = 1;
        dfs(now + 1,x1,x2 + 1,p1,p2 - 1);
    }
}

void work()
{
    dfs(2,0,0,n / 2 - 1,n / 2 - 1);
}

int main()
{
    freopen("C-large.in","r",stdin);
    freopen("C-large.out","w",stdout);

    int T;
    cin>>T;
    memset(g,0,sizeof(g));

    for(int i = 1;i <= T;i++)
    {
        init();
        printf("Case #%d:\n",i);
        work();
    }
    return 0;
}
