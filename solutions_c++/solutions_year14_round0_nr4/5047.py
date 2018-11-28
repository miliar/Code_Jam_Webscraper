#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,n,i,count,count1,k,l,m,p;
    float a[100],b[100],x;
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
        count=0,count1=0;
        scanf("%d",&n);
        for(i=0;i<n;i++)
            scanf("%f",&a[i]);
        for(i=0;i<n;i++)
            scanf("%f",&b[i]);
        sort(a,a+n);
        sort(b,b+n);
        p=0;
        for(i=0;i<n;i++)
        {
            if(a[i]>b[p])
            {
                count1++;
                p++;
            }
        }
        m=n-1;
        for(i=n-1;i>=0;i--)
        {
            if(a[i]>b[m])
                count++;
            else
                m--;
        }
        printf("Case #%d: %d %d\n",k,count1,count);
    }
    return 0;
}
