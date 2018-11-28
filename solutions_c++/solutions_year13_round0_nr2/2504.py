#include <iostream>
#include <fstream>
using namespace std;
typedef long long lld;
lld n,m,lawn[102][102],brow[102],bcol[102];
int main ()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    lld i,j,t,test,h;
    bool success;
    scanf("%lld",&test);
    for (t=1;t<=test;t++)
    {
        success=true;
        scanf("%lld %lld",&n,&m);
        for (i=1;i<=n;i++)
        {
            h=0;
            for (j=1;j<=m;j++)
            {
                scanf("%lld",&lawn[i][j]);
                if (h<lawn[i][j]) h=lawn[i][j];
            }
            brow[i]=h;
        }
        for (j=1;j<=m;j++)
        {
            h=0;
            for (i=1;i<=n;i++)
            {
                if (h<lawn[i][j]) h=lawn[i][j];
            }
            bcol[j]=h;
        }

        for (i=1;i<=n;i++)
        {
            for (j=1;j<=m;j++)
            {
                if (lawn[i][j]<brow[i]&&lawn[i][j]<bcol[j])
                {
                    success=false;
                    break;
                }
            }
            if (!success) break;
        }
        printf("Case #%lld: ",t);
        if (success)
        {
            printf("YES\n");
        }
        else
        {
            printf("NO\n");
        }
    }
}
