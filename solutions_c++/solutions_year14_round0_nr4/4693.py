#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
int main()
{
    int t,n,i,cas=0,co,k,j;
   // freopen("D-large.in","r",stdin);
   // freopen("out1.txt","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
        cas++;
        co=0;
        k=0;
        scanf("%d",&n);
        double a[n],b[n],x[n],y[n];
        for(i=0;i<n;i++){
            scanf("%lf",&a[i]);
            x[i]=a[i];
        }
        for(i=0;i<n;i++){
            scanf("%lf",&b[i]);
             y[i]=b[i];
        }
        if(n==1)
        {
            if(a[0]>b[0])
                printf("Case #%d: 1 1\n",cas);
            else
                printf("Case #%d: 0 0\n",cas);
        }
        else
        {
            sort(a,a+n);
            sort(b,b+n);
            for(i=n-1;i>=0;i--)
            {
                for(j=n-1;j>=0;j--)
                {
                    if(b[i]>a[j] && a[j]!=-1)
                    {
                        a[j]=-1;
                        b[i]=-1;
                        co++;
                        break;
                    }
                   // co=n-co;
                }
            }
            co=n-co;
            sort(x,x+n);
            sort(y,y+n);
            for(i=n-1;i>=0;i--)
            {
                for(j=n-1;j>=0;j--)
                {
                    if(x[i]>y[j] && y[j]!=-1)
                    {
                        y[j]=-1;
                        x[i]=-1;
                        k++;
                        break;
                    }
                   // co=n-co;
                }
            }
                printf("Case #%d: %d %d\n",cas,k,co);
            }

        }


    return 0;
}
