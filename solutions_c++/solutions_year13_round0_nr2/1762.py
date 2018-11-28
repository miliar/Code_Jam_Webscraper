#include<stdio.h>
#include<algorithm>
using namespace std;
int main()
{
    int t,n,m,a[100][100],i,j,k,maxm;
    scanf("%d",&t);
    for(k=1;k<=t;++k)
    {
        int maxmvertical[100],maxmhorizontal[100],flag=0;
        scanf("%d %d",&n,&m);
        for(i=0;i<n;++i)
        {
            maxm=0;
            for(j=0;j<m;++j)
            {
                scanf("%d",&a[i][j]);
                if(a[i][j]>maxm)
                    maxm=a[i][j];
            }
            maxmhorizontal[i]=maxm;
        }
        for(j=0;j<m;++j)
        {
            maxm=0;
            for(i=0;i<n;++i)
            {
                if(a[i][j]>maxm)
                    maxm=a[i][j];
            }
            maxmvertical[j]=maxm;
        }
        for(i=0;i<n;++i)
        {
            for(j=0;j<m;++j)
            {
                maxm=min(maxmhorizontal[i],maxmvertical[j]);
                if(a[i][j] < maxm)
                {
                    flag=1;                         //not possible
                }
            }
        }
    //out:;
    if(flag)
        printf("Case #%d: NO\n",k);
    else
        printf("Case #%d: YES\n",k);
    }

    return 0;
}
