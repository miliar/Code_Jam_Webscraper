#include <stdio.h>
#include <algorithm>

using namespace std;

double a[1005],b[1005];
int u[1005];

int main()
{
    int i,j,k,t,T,n,p,q;

    freopen("D-large.in","r",stdin);
    freopen("d-large.txt","w",stdout);

    scanf("%d",&T);

    for(t=1;t<=T;t++)
    {
        scanf("%d",&n);

        for(i=0;i<n;i++) scanf("%lf",&a[i]);
        for(i=0;i<n;i++) scanf("%lf",&b[i]);
        for(i=0;i<n;i++) u[i]=0;

        sort(a,a+n);
        sort(b,b+n);

       i=j=p=0;

       while(i<n && j<n)
       {
           if(a[i]>b[j])
           {
               p++;
               i++;
               j++;
           }

           else i++;
       }

       for(j=n-1; j>=0 ; j--)
       {

           for(i=n-1;i>=0;i--)
           {
               if(u[i]) continue;

               if(a[i]>b[j]) continue;

               u[i]=1;
               k=i;
               break;
           }

           if(i==-1) break;
       }

        printf("Case #%d: %d %d\n",t,p,j+1);
    }

    return 0;
}
