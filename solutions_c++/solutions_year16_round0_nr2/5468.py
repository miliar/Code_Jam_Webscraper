#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef vector<pii> vpii;
typedef unsigned long long llu;

#define author ayushtomar
#define rf freopen("haha.in", "r", stdin)
#define wf freopen("out.txt", "w", stdout)
#define debug(x) cerr<<#x<<" "<<x<<endl;
#define f first
#define s second
#define mp make_pair
#define pb push_back
typedef pair<int,int> ii;
typedef pair<int,pair<int,int> > iii;
string s1;
int dp[101][2];
int main()
{
    rf;wf;

    int t,n,T;
    scanf("%d",&t);
    for(int tt=1;tt<=t;tt++)
    {
        cin>>s1;
        for(int i=0;i<=100;i++)
            dp[i][0]=dp[i][1]=0;

        if(s1[0]=='-')
        {
            dp[0][0]=0;
            dp[0][1]=1;
        }
        else
        {
            dp[0][0]=1;
            dp[0][1]=0;
        }

        for(int i=1;i<s1.size();i++)
        {
            if(s1[i]=='-')
            {
                dp[i][0]=dp[i-1][0];
                dp[i][1]=dp[i-1][0]+1;
            }
            else
            {
                dp[i][0]=1+dp[i-1][1];
                dp[i][1]=dp[i-1][1];
            }
        }
        cout<<"Case #"<<tt<<": ";
        cout<<dp[s1.size()-1][1]<<"\n";
    }

    return 0;
}
