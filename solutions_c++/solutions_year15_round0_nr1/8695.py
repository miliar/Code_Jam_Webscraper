#include <bits/stdc++.h>
#define fo(i,x,y) for (int i = x; i < y; i++)
#define fd(i,x,y) for(int i = x; i>= y; i--)
#define ll long long
#define clr(A,x) memset(A, x, sizeof A)
#define pb push_back
#define mod 1000000007
#define debug(x) cout <<#x << " = " << x << endl
using namespace std;
int main()
{
    freopen("D:\input.txt","r",stdin);
    freopen("D:\output.txt","w",stdout);
    int t;
    cin>>t;
    fo(q,0,t)
    {
        int s;
        cin>>s;
        string let;
        cin>>let;
        int cnt=0;
        vector<int> dp(s+2,0);
        dp[0]=(let[0]-'0');
        int ans=0;
        fo(i,1,s+1)
        {
            if((let[i]-'0')==0)
            {
                dp[i]=dp[i-1];
            }
            else if(dp[i-1]>=i)
            {
                dp[i]=dp[i-1]+(let[i]-'0');
            }
            else
            {
                ans+=(i-dp[i-1]);
                dp[i]=dp[i-1]+(let[i]-'0')+(i-dp[i-1]);
            }
        }
        cout<<"Case #"<<q+1<<": "<<ans<<endl;
    }
}
