#include <bits/stdc++.h>
#define ll long long
#define ll unsigned long long
#define rep(i,a,b) for(long long i=a;i<b;i++)
#define repi(i,a,b) for(long long i=a;i>b;i--)
#define MOD 1000000007
using namespace std;

int main()
{
    int t;
    cin>>t;
    rep(looper, 0, t)
    {
        int s_max;
        cin>>s_max;
        string shy;
        cin>>shy;
        int ans=0, cur=0;
        rep(i,0,shy.length())
        {
            int val=shy[i]-'0';
            if(i==0)
                cur+=val;
            else
            {
                if(cur<(i))
                {
                    ans+=i-cur;
                    cur+=i-cur;
                }
                cur+=val;
            }
        }
        cout<<"Case #"<<looper+1<<": "<<ans<<endl;
    }
    return 0;
}

