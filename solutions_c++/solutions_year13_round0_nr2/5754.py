#include <iostream>
#include<cstdio>
#include<string>
using namespace std;

int main()
{
   freopen("B-small-attempt2.in","r", stdin);
    freopen("output.in","w", stdout);

    int t,it,a[12][12],i,j,x,k;
    scanf("%d",&t);
    for(it=1;it<=t;it++)
    {printf("Case #%d: ",it);
        int n,m;
        bool f=false;
        scanf("%d%d",&n,&m);
        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            {
                scanf("%d",&a[i][j]);
            }
        }
        if(n==1) {printf("YES\n");continue;}
        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            {
                if(a[i][j]==1)
                {
                    for(k=0;k<n;k++) if(a[k][j]!=1) break;
                    if(k==n) continue;
                    for(k=0;k<m;k++) if(a[i][k]!=1) break;
                    if(k==m) continue;
                    f=1;

                }
            }
        }
        if(f==0) printf("YES\n");
        else printf("NO\n");
    }

    return 0;
}
