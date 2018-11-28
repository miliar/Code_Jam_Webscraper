#include<stdio.h>
#include<algorithm>
using namespace std;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t,n,i,cas=1;
    scanf("%d",&t);
    while(t--)
    {
        int a[10002],s1=0,s2=0;
        scanf("%d",&n);
        for(i=0;i<n;i++)
            scanf("%d",&a[i]);
            int max=0;
        for(i=0;i<n-1;i++)
        if(a[i]>a[i+1]) {s1+=a[i]-a[i+1];if((a[i]-a[i+1])>max)   max=a[i]-a[i+1]; }
        for(i=0;i<n-1;i++)
            if(a[i]>max) s2+=max;
        else s2+=a[i];
        printf("Case #%d: %d %d\n",cas++,s1,s2);

    }
}
