#include<cstdio>
#include<algorithm>

using namespace std;

int T;
int n;
int pp[100][100];
int p[100][100];
int a[100];

inline check1(int x,int X)
{
    //printf("%d %d\n",x,X);
    if(x==n+1)return true;
    bool flag=false;
    for(int i=1;i<=n;i++)
        if(pp[a[x]][i]&&((X|(1<<i-1)))!=X)
        {
            flag=true;
            if(!check1(x+1,X|(1<<i-1)))return false;
        }
    return flag;
}
inline bool check(int x)
{
    for(int i=1;i<=n;i++)
        for(int j=1;j<=n;j++)
        {
            pp[i][j]=x&1;
            x>>=1;
            if(pp[i][j]==0&&p[i][j]==1)return false;
        }

    for(int i=1;i<=n;i++)
        a[i]=i;

    while(true)
    {
        if(!check1(1,0))return false;
        if(!next_permutation(a+1,a+n+1))break;
    }
    return true;
}
int main()
{
    freopen("d.in","r",stdin);
    freopen("d.out","w",stdout);

    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        scanf("%d",&n);
        int cnt=0;
        char str[10];
        for(int i=1;i<=n;i++)
        {
            scanf("%s",str);
            for(int j=1;j<=n;j++)
            {
                p[i][j]=str[j-1]-'0';
                cnt+=p[i][j];
            }
        }
        int ma=100000;
        for(int i=0;i<(1<<n*n);i++)
        {
            if(check(i))
            {
                int cnt1=0;
                for(int i0=1;i0<=n;i0++)
                    for(int j0=1;j0<=n;j0++)
                        cnt1+=pp[i0][j0];
                if(cnt1-cnt<ma)
                {
                    ma=cnt1-cnt;
                }
            }
        }
        printf("Case #%d: %d\n",t,ma);
    }
    return 0;
}
