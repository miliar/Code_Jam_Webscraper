#include<stdio.h>
#include<algorithm>
using namespace std;
int s[1007];
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t,cas=1;
    scanf("%d",&t);
    while(t--)
    {
        int n,maxx=-1;
        scanf("%d",&n);
        for(int i=1;i<=n;i++)
            scanf("%d",&s[i]),maxx=max(maxx,s[i]);
        int sum=0,minn=10000;
        for(int i=1;i<=maxx;i++)
        {
            sum=0;
            for(int j=1;j<=n;j++)
                if(s[j]>i)sum+=(s[j]-1)/i;
            sum+=i;
            minn=min(minn,sum);
        }
        printf("Case #%d: %d\n",cas++,minn);
    }
    return 0;
}
