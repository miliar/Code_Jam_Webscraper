#include <cstdio>

using namespace std;
int viz[100],a[100][100],b[100][100],nr,nr2,ok,sol,t;
int main()
{
    freopen("magic.in","r",stdin);
    freopen("magic.out","w",stdout);
    scanf("%d",&t);
    for(int k=1;k<=t;k++)
    {
        for(int i=1;i<=16;i++)
        {
            viz[i]=0;
        }
        scanf("%d",&nr);
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                scanf("%d",&a[i][j]);
            }
        }
        scanf("%d",&nr2);
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                scanf("%d",&b[i][j]);
            }
        }
        for(int i=1;i<=4;i++)
        {
            viz[a[nr][i]]++;
            viz[b[nr2][i]]++;
        }
        ok=0;
        for(int i=1;i<=16;i++)
        {
            if(viz[i]>1)
            {
                ok++;
                sol=i;
            }
        }
        if(ok==0)
        {
            printf("Case #%d: Volunteer cheated!\n",k);
        }
        if(ok==1)
        {
            printf("Case #%d: %d\n",k,sol);
        }
        if(ok>1)
        {
            printf("Case #%d: Bad magician!\n",k);
        }
    }
    return 0;
}
