#include<cstdio>
#include<algorithm>
using namespace std;
int n;
int a[20],b[20];
int used[20];
void read()
{
    int i;
    double d;
    scanf("%d",&n);
    for(i=1;i<=n;i++)
    {
        scanf("%lf",&d);
        a[i]=int(d*100000);
    }
    for(i=1;i<=n;i++)
    {
        scanf("%lf",&d);
        b[i]=int(d*100000);
    }
}
void solveDeceitful()
{
    int i,j,ans=0,in;
    for(i=1;i<=n;i++)
    {
        for(j=1;j<=n;j++)
        if(!used[j])
        {
            if(a[i]>b[j])
            {
                in=j;
                break;
            }
            else in=j;
        }
        if(j<=n)
        {
            ans++;
            used[in]=j;
        }
        else used[in]=1;
    }
    printf("%d",ans);
}
void solveWar()
{
    int i,j,ans=0;
    for(i=1;i<=n;i++)
    {
        for(j=1;j<=n;j++)
        if(!used[j]&&b[j]>a[i])break;
        if(j>n)ans++;
        else used[j]=1;
    }
    printf(" %d\n",ans);
}
int main()
{
    int i,t;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        read();
        printf("Case #%d: ",i);
        sort(a+1,a+(n+1));
        sort(b+1,b+(n+1));
        solveDeceitful();
        memset(used,0,sizeof(used));
        solveWar();
        memset(used,0,sizeof(used));
    }
}
