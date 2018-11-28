#include <bits/stdc++.h>
#define ll long long
#define ll unsigned long long
#define rep(i,a,b) for(long long i=a;i<b;i++)
#define repi(i,a,b) for(long long i=a;i>b;i--)
#define MOD 1000000007
using namespace std;

int main()
{
    int dp[2000]={0};
    dp[1]=1;
    dp[2]=2;
    dp[3]=dp[4]=3;
    rep(i,5,2000)
    {
        if(i&1)
            dp[i]=1+max(dp[(i)/2],dp[(i+1)/2]);
        else
            dp[i]=1+dp[i/2];
    }
    //rep(i,1,100)
    //    cout<<"Val for "<<i<<": "<<dp[i]<<endl;
    int t;
    cin>>t;
    rep(looper, 0, t)
    {
        int d, temp, max_i=0;
        cin>>d;
        vector<int> arr;
        rep(i,0,d)
        {
            cin>>temp;
            arr.push_back(temp);
            max_i=max(max_i,temp);
        }
        int ans=max_i, cur;
        rep(i,1,ans+1)
        {
            cur=i;
            rep(j,0,d)
            {
                if(arr[j]>i)
                    cur+=(arr[j]%i==0?arr[j]/i-1:arr[j]/i);
            }
            ans=min(cur,ans);
        }
        cout<<"Case #"<<looper+1<<": "<<ans<<endl;
    }
    return 0;
}

