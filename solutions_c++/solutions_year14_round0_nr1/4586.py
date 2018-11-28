#include <cstdio>
#include <cstdlib>
#include <cstring>

int t,f[5][5],a,b,x,ans,i,j;

int ini()
{
    scanf("%d",&x);
    ans=0;
    for(i=1;i<=4;i++)
        for(j=1;j<=4;j++)
            scanf("%d",&f[i][j]);
    for(i=1;i<=4;i++)
        ans|=(1<<f[x][i]);
    return ans;
}

int main()
{
    freopen("A.in","r",stdin);
    freopen("a-out.txt","w",stdout);
    scanf("%d",&t);
    for(int cas=1;cas<=t;cas++)
    {
        a=ini();
        b=ini();
        x=a&b;
        if(x==0)printf("Case #%d: Volunteer cheated!\n",cas);
        else
        {
            ans=-1;
            for(int i=1;i<=16;i++)
                if(x==(1<<i))ans=i;
            if(ans==-1)printf("Case #%d: Bad magician!\n",cas);
            else printf("Case #%d: %d\n",cas,ans);
        }
    }
    return 0;
}
