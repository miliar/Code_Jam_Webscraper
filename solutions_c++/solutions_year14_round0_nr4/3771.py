//BISMILLAHIR RAHMANIR RAHIM
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<string>
#include<map>
#include<queue>
#include<vector>
#include<iostream>
using namespace std;
#define inf 1<<25
#define sz 2000
int main()
{
    int n,i,j,nwp,ndp,t,k,knwp,kndp,x;
    double nmi[sz],ken[sz],nmw[sz],kenw[sz];
    double told;
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
        nwp=ndp=knwp=kndp=0;
        scanf("%d",&n);
        for(i=0;i<n;i++)
        {
             scanf("%lf",&nmi[i]);
             nmw[i]=nmi[i];
        }

        for(i=0;i<n;i++)
        {
             scanf("%lf",&ken[i]);
             kenw[i]=ken[i];
        }
         sort(nmi,nmi+n);
         sort(nmw,nmw+n);
         sort(ken,ken+n);
         sort(kenw,kenw+n);
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                if(kenw[j]>nmw[i])
                {
                    kenw[j]=nmw[i]=0;
                    break;
                }
            }
            if(nmw[i]!=0)
                nwp++;
        }
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                if(ken[i]<nmi[j])
                {
                    ken[i]=nmi[j]=0;
                    ndp++;
                    break;
                }
            }
        }

        printf("Case #%d: %d %d\n",k,ndp,nwp);
    }
    return 0;
}

