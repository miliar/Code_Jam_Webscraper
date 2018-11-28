#include <bits/stdc++.h>
using namespace std;
typedef vector<int> vi; typedef pair<int,int> pii; typedef vector<pair<int,int> > vpii;
typedef long long ll; typedef vector<long long> vl; typedef pair<long long,long long> pll;
typedef vector<pll> vpll;typedef vector<string> vs; typedef double D; typedef vector<bool> vb;
typedef pair<ll,pll> pip;
#define sz(v) int((v).size())
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define sd(x) scanf("%d", &x)
#define slld(x) scanf("%I64d", &x)
#define debug(X) cerr << "	--> " << #X << " = " << X << endl
#define present(c,x) ((c).find(x) != (c).end())
#define mod 1000000007LL
#define INF 2000000000LL
#define N 1123
int ar[N];
int dp[N][N];
multiset<int> st;
bool f(int n)
{
	for(int i=n;i>0;--i)
	{
		if(*st.rbegin()<=i)return true;
		else
		{
			int ma = *st.rbegin();
			st.insert(ma/2);
			st.insert(ma/2+(ma&1));
			st.erase(st.find(ma));
		}
	}
	return false;
}
void solve()
{
	int d;
	scanf("%d",&d);
	int ma = 0;
	for(int i=0;i<d;++i)
	{
		scanf("%d",&ar[i]);
		ma = max(ar[i],ma);
	}
	int ans = ma;
	for(int i=0;i<ma;++i)
	{
		int c = 0;
		for(int j=0;j<d;++j)
		{
			c += dp[ar[j]][i];
		}
		c += i;
		ans = min(ans,c);
	}
	printf("%d\n",ans);
}
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("ansC.txt","w",stdout);
	int t = 1;
	scanf("%d",&t);
	for(int j=0;j<N;++j)
	{
		for(int i=0;i<N;++i)
		{
			if(i<=j)dp[i][j] = 0;
			else
			{
				dp[i][j] = i-j;
				for(int k=1;k<=i/2+1;++k)
				{
					dp[i][j] = min(dp[k][j]+dp[i-k][j]+1,dp[i][j]);
				}
			}
		}
	}
	for(int z=1;z<=t;++z)
	{
		printf("Case #%d: ",z);
		solve();
	}
	return 0;
}
/**
Code Walkthrough
Code Inspection:
N
return value of function
Overflow
**/

