#include<bits/stdc++.h>

using namespace std;

#define sd(x) scanf("%d",&x);
#define slld(x) scanf("%lld",&x);
#define LL long long
#define LD long double
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define Fill(a, b) memset(a, b, sizeof(a))
#define INF 2000000009

typedef pair<int,int> PII;
typedef vector<int> VI;

#define N 110

int dp[N][2];

void solve()
{
    string s;
    cin>>s;
    for(int i=0;i<s.length();i++)
    {
        if(s[i] == '-')
        {
            dp[i+1][0] = min(dp[i][0], dp[i][1]+2);
            dp[i+1][1] = dp[i+1][0] + 1 ;
        }
        else
        {
            dp[i+1][1] = min(dp[i][1], dp[i][0]+2);
            dp[i+1][0] = dp[i+1][1] + 1;
        }
    }
    cout<<dp[s.length()][1]<<endl;
}

int main()
{
    freopen("1l.in","r",stdin);
    freopen("1l.out","w",stdout);
	int t=1;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
        printf("Case #%d: ",i);
		solve();
	}
}

