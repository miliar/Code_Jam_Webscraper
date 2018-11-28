#include<stdio.h>
#include<algorithm>
using namespace std;
bool cmp(double a,double b)
{
    return a>b;
}

int main()
{
    int t,c1,c2,n;
    double a[1003],b[1003];
    int i,j,k;
    freopen("H:D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
        c1=0;
        c2=0;
        scanf("%d",&n);
        for(i=0;i<n;i++)
        scanf("%lf",&a[i]);
        for(i=0;i<n;i++)
        scanf("%lf",&b[i]);
        sort(a,a+n,cmp);
        sort(b,b+n,cmp);
        for(i=0,j=0;i<n;i++)
        {
            if(a[j]>b[i])
            {
                c1++;
                j++;
            }
        }
        for(i=n-1,j=n-1;i>=0;)
        {
            if(a[j]>b[i])
            {
                i--;
            }
            else
            {
                i--;
                j--;
            }
        }
        printf("Case #%d: ",k);
        printf("%d %d\n",c1,j+1);
    }
    return 0;
}
