#include <bits/stdc++.h>

using namespace std;
long long int a[1005];
int main()
{
    freopen("C:\\Users\\DARPAN\\Desktop\\input.in","r",stdin);
    freopen("C:\\Users\\DARPAN\\Desktop\\output.txt","w",stdout);
    int k=1;
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        for(int i=0;i<n;i++) cin>>a[i];
        long long int rate=0LL,ans1=0LL;
        for(int i=0;i<n-1;i++)
        {
            if(a[i]>a[i+1])
            {
                ans1+=(a[i]-a[i+1]);
                rate=max(rate,a[i]-a[i+1]);
            }
        }
        long long int ans2=0LL;
        for(int i=0;i<n-1;i++)
        {
            if(a[i]>=rate) ans2+=rate;
            else ans2+=a[i];
        }
        cout<<"Case #"<<k<<": "<<ans1<<" "<<ans2<<endl;
        k++;
    }
    return 0;
}
