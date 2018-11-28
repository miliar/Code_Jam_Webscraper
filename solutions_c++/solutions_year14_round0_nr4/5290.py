#include<stdio.h>
#include<algorithm>
using namespace std;
int main()
{
    int t,i,n,cd,c,ct=0,j;
    double a[11],b[11],a1[11];
    scanf("%d",&t);
    while(t--)
    {
        ct++;
        cd=0;c=0;
        scanf("%d",&n);
        for(i=0;i<n;i++)
            scanf("%lf",&a[i]);
        for(i=0;i<n;i++)
            scanf("%lf",&b[i]);
        sort(a,a+n);
        sort(b,b+n);
        for(i=0;i<n;i++)
            a1[i]=a[i];
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                if(b[i]<a1[j])
                {
                    cd++;
                    a1[j]=0;
                    break;
                }
            }
        }
        for(i=0;i<n;i++)
        {
            for(j=0;j<n;j++)
            {
                if(a[i]<b[j])
                {
                    c++;
                    b[j]=0;
                    break;
                }
            }
        }
        printf("Case #%d: %d %d\n",ct,cd,n-c);
    }
    return 0;
}
