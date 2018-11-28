#include<stdio.h>
#include<algorithm>

using namespace std;

int main()
{
    int t,n,a[1000],b[1000],bx[1000],ax[1000];
    scanf("%d",&t);
    for(int k=1;k<=t;k++)
    {
        int count1=0,count2=0;
        scanf("%d",&n);
        for(int i=0;i<n;i++)
        {
            scanf("%f",&a[i]);
        }
        for(int i=0;i<n;i++)
        {
            scanf("%f",&b[i]);
        }
        sort(a,a+n);
        sort(b,b+n);
        for(int i=0;i<n;i++) bx[i]=b[i];
        for(int i=n-1;i>=0;i--)
        {
            for(int j=n-1;j>=0;j--)
            {
                if(bx[j]<a[i]&&bx[j]>0)
                {
                    bx[j]=0;
                    count1++;
                    break;
                }
            }
        }
        for(int i=0;i<n;i++) ax[i]=a[i];
        for(int i=n-1;i>=0;i--)
        {
            for(int j=n-1;j>=0;j--)
            {
                if(b[i]>ax[j]&&ax[j]>0)
                {
                    ax[j]=0;
                    count2++;
                    break;
                }
            }
        }
        printf("Case #%d: %d %d\n",k,count1,n-count2);
    }
}
