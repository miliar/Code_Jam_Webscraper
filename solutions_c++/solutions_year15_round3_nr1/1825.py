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
const int N = 112345;
#define int long long
inline void pre(){}
inline void solve()
{
	int r,c,w;
	cin>>r>>c>>w;
	int ans = r * ( (c-1)/w + w );
	printf("%lld\n",ans);
}
#undef int
int main()
{
	freopen("A-small-attempt2.in","r",stdin);
	freopen("Asubmit.out","w",stdout);
	int t = 1;
	scanf("%d",&t);
	for(int z = 0; z < t; ++z)
	{
		printf("Case #%d: ",z + 1);
		solve();
	}
	return 0;
}
