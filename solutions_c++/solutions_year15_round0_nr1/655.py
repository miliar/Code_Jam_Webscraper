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
char s[N];
void solve()
{
	int n;
	scanf("%d",&n);
	scanf("%s",s);
	int sum = s[0] - '0';
	int ans = 0;
	for(int i=1;i<=n;++i)
	{
		if(sum<i)
		{
			++ans;++sum;
		}
		sum += s[i]-'0';
	}
	printf("%d\n",ans);
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("ansA.txt","w",stdout);
	int t = 1;
	scanf("%d",&t);
	for(int z=1;z<=t;++z)
	{
		printf("Case #%d: ",z);
		solve();
	}
	return 0;
}
/*
Code Inspection:
N
return value of function
overflow
*/

