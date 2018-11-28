#include<stdio.h>
#include<algorithm>
using namespace std;
int grd[105][105];
int mxc[105];
int mxr[105];
int rl[105][105];
int main()
{
freopen("B-large.in","r",stdin);
freopen("out.out","w",stdout);    
    int n,m,i,j,a;
    int t;
    scanf("%d",&t);
    for(a=1;a<=t;a++)
    {
        printf("Case #%d: ",a);
        scanf("%d%d",&n,&m);
        for(i=0;i<n;i++)
        {
            mxr[i]=-1;
            for(j=0;j<m;j++)
            {
            mxc[j]=-1;    
                scanf("%d",&grd[i][j]);
                rl[i][j]=100;
            }
        }
        for(i=0;i<n;i++)
        for(j=0;j<m;j++)
        {
            mxr[i]=max(mxr[i],grd[i][j]);
            mxc[j]=max(mxc[j],grd[i][j]);
        }        
        /*hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhfor(i=0;i<n;i++)
            printf("%d ",mxr[i]);
        for(i=0;i<m;i++)
            printf("%d ",mxc[i]);
                        */
        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            {
                //printf("%d ",min(100,min(mxr[i],mxc[j])));
                if(min(100,min(mxr[i],mxc[j])) != grd[i][j])
                {
                    printf("NO\n");
                    i=n+5;
                    break;
                }
        }
            
        }
        if(i != n)
            continue;
        printf("YES\n");
    }
    //while(1);
}
