#include <stdio.h>
#include <cstring>
const int maxn=110;
int a[maxn][maxn];
int t,n,m;
bool is()
{
    bool ret1=false,ret2=false;
    for(int i=0; i<n; i++)
    {
        for(int j=0; j<m; j++)
        {
            int x=i,y=j;
            int tx=0,ty=0;
            int temp=a[i][j];
            ret1=false,ret2=false;
            while(tx<n)
            {
                if(a[tx][y]>temp)
                {
                    ret1=true;
                    break;
                }
                tx++;
            }
            while(ty<m)
            {
                if(a[x][ty]>temp)
                {
                    ret2=true;
                    break;
                }
                ty++;
            }
            if(ret1&&ret2) return false;
        }
    }
    return true;
}
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("sum.out","w",stdout);
    scanf("%d",&t);
    for(int p=1; p<=t; p++)
    {
        scanf("%d%d",&n,&m);
        for(int i=0; i<n; i++)
            for(int j=0; j<m; j++)
            {
                scanf("%d",&a[i][j]);
            }
        printf("Case #%d: ",p);
        if(is()) printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}
