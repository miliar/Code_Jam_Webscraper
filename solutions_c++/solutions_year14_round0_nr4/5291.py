#include<stdio.h>
#include<algorithm>
using namespace std;
int main()
{
    double a[15],b[15];
    int i,j,k,count1,count2,n,t;
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
        count1=0;
        count2=0;
        scanf("%d",&n);
        for(i=0;i<n;i++)
        {
            scanf("%lf",&a[i]);
        }
        for(i=0;i<n;i++)
        {
            scanf("%lf",&b[i]);
        }
        sort(a,a+n);
        sort(b,b+n);
        j=n-1;
        for(i=n-1;i>=0;i--)
        {
            if(a[i]>b[j])
            {
                count2++;
            }
            else
            {
                j--;
            }
        }
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                if(a[i]>b[j])
                {
                    b[j]=10.0;
                    count1++;
                    break;
                }
            }

        }
        printf("Case #%d: %d %d\n",k,count1,count2);
    }
    return 0;
}
