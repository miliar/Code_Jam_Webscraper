#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
double a[1111],b[1111];
int n;
int ans1,ans2;
int main()
{
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);
    int ca=1;
    int t;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&n);
        for(int i=1;i<=n;i++)scanf("%lf",&a[i]);
        for(int i=1;i<=n;i++)scanf("%lf",&b[i]);
        sort(a+1,a+n+1);
        sort(b+1,b+n+1);
        ans1=ans2=0;
        int low=0,high=n,mid;
        while(low<=high)
        {
            mid=(low+high)/2;
            bool f=0;
            for(int i=1;i<=mid;i++)
            {
                if(a[i]>=b[n-mid+i])
                {
                    f=1;
                    break;
                }
            }
            if(f)
            {
                high=mid-1;
            }
            else
            {
                low=mid+1;
                ans1=max(ans1,mid);
            }
        }
        high=n;
        low=0;
        while(low<=high)
        {
            mid=(low+high)/2;
            bool f=0;
            for(int i=1;i<=mid;i++)
            {
                if(b[i]>=a[n-mid+i])
                {
                    f=1;
                    break;
                }
            }
            if(f)
            {
                high=mid-1;
            }
            else
            {
                low=mid+1;
                ans2=max(ans2,mid);
            }
        }
        cout<<"Case #"<<ca++<<": ";
        cout<<ans2<<" "<<n-ans1<<endl;
    }
    return 0;
}
