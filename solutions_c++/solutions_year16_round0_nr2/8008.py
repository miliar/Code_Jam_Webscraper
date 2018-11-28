#include<bits/stdc++.h>
using namespace std;
#define no 31623
//#define getchar_unlocked getchar
#define ll long long int
#define mb make_pair
#define pb push_back
#define F first
#define S second
#define pii pair<int,int>
#define pll pair<ll,ll>
#define pdd pair<double,double>
#define tr(it,x) for(auto it=x.begin(); it!=x.end(); it++)
#define rep(i,n) for(int i=0;i<n;i++)
#define repp(i,a,b) for(int i=a;i<=b;i++)
#define ref(i,n) for(int i=n;i>1;i--)
#define reff(i,a,b) for(int i=a;i>=b;i--)
#define M 1000000007
#define MAX 100005 
#define fastScan ios_base::sync_with_stdio(0); cin.tie(NULL);
//#define sc(x) scanf("%d",&x)
//#define scc(x1,x2) scanf("%d%d",&x1,&x2)
//#define sccc(x1,x2,x3) scanf("%d%d%d",&x1,&x2,&x3)
//#define scl(x) scanf("%lld",&x)
//#define sccl(x1,x2) scanf("%lld%lld",&x1,&x2)
//#define sccl(x1,x2,x3,x4,x5) scanf("%lld%lld%lld%lld%lld",&x1,&x2,&x3,&x4,&x5)
//#define pr(x) printf("%f\n",x)
//#define prl(x) printf("%lld\n",x)
//#define prrl(x1,x2) printf("%lld %lld\n",x1,x2)
#define fill(a,x) memset(a,x,sizeof(a))
ll gcd(ll a, ll b) { return (b == 0 ? a : gcd(b, a % b)); }
ll lcm(int a, int b) { return (a * (b / gcd(a, b))); }
ll max(ll a,ll b,ll c){return max(a,max(b,c));}
ll power(ll x,ll y)
{
    ll ans=1;
    while(y>0){
        if(y&1)
            ans=(ans*x)%M;
        x=(x*x)%M;
        y/=2;
    }
    return ans;
}
//ifstream ifs("Subtask1.txt");
//ofstream ofs("Solution1.txt");
int main()
{
	ll t,n,cnt=1;
	cin>>t;
	while(t--)
	{
		string s;
		cin>>s;
		n=s.size();
		ll ans=0;
		rep(i,n-1)
		{
			if(s[i]!=s[i+1])
			ans++;
		}
		if(s[n-1]=='-')
		ans++;
		cout << "Case #" << cnt << ": " << ans << endl;
		//ofs << "Case #" << cnt << ": " << ans << endl;
		cnt++;
	}
}
