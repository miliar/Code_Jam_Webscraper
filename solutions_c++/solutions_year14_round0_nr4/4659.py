#include<stdio.h>
#include<algorithm>
#include<queue>
using namespace std;
int main()
{
    int t,l;
    scanf("%d",&t);
    for(l=1;l<=t;l++)
    {
        double a1[1001]={0},b1[1001]={0};
        double a2[1001]={0},b2[1001]={0};
        int n,i,j;
        scanf("%d",&n);
        for(i=0;i<n;i++)
            scanf("%lf",&a1[i]);
        for(i=0;i<n;i++)
            scanf("%lf",&a2[i]);
        sort(a1,a1+n);
        sort(a2,a2+n);
        for(i=0;i<n;i++)
        {
            b1[i]=a1[i];
            b2[i]=a2[i];
        }
        int count=0;
        int w1=0,w2=0;
        while(count!=n)
        {
            if(a1[n-count-1]<a2[n-count-1])
            {
                a1[0]=10000;
                a2[n-count-1]=10000;
            }
            else
            {
                w1++;
                for(i=0;i<n-count;i++)
                {
                    if(a1[i]>a2[0])
                    {
                        a1[i]=10000;
                        a2[0]=10000;
                        break;
                    }
                }
            }
            sort(a1,a1+n);
            sort(a2,a2+n);
            count++;
        }
        sort(b1,b1+n);
        sort(b2,b2+n);
        count=0;
        while(count!=n)
        {
            if(b1[0]>b2[n-count-1])
            {
                w2++;
                b1[0]=10000;
                b2[0]=10000;
            }
            else
            {
                for(i=0;i<n-count;i++)
                {
                    if(b2[i]>b1[0])
                    {
                        b2[i]=10000;
                        b1[0]=10000;
                        break;
                    }
                }
            }
            count++;
            sort(b1,b1+n);
            sort(b2,b2+n);
        }

        printf("Case #%d: %d %d\n",l,w1,w2);
    }
    return 0;
}

