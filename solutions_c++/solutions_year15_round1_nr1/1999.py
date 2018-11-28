/*Mushroom Monster*/
#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("1_large.txt","w",stdout);
    int t;
    cin>>t;
    int cas=1;
    while(t--)
    {   long long n;
        cin>>n;
        long long a[n],i;
        for(i=0;i<n;i++)
            cin>>a[i];
        long long ans1=0,ans2=0;
        for(i=1;i<n;i++)
            if(a[i]<a[i-1])
                ans1+=a[i-1]-a[i];
        long long max=0;
        for(i=1;i<n;i++)
        {   if(a[i-1]-a[i]>max)
                max=a[i-1]-a[i];
        }
        for(i=0;i<n-1;i++)
        {   if(a[i]<=max)
                ans2+=a[i];
            else
                ans2+=max;
        }
        cout<<"Case #"<<cas<<": "<<ans1<<" "<<ans2<<endl;
        cas++;
    }
    return 0;
}
