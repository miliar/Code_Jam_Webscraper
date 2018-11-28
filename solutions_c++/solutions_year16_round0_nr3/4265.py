#include<bits/stdc++.h>
using namespace std;
#define lop(i,a,n) for(ll i=a;i<n;++i)
#define loop(i,n,a)for(ll i=n-1;i>=a;--i)
#define R_(s)      freopen(s, "r", stdin)
#define W_(s)      freopen(s, "w", stdout)
#define R_W        R_("input.txt"),W_("output.txt")
#define ll         long long
#define ld         long double
#define ii         pair<ll,ll>
#define vii        vector<ii>
#define vi         vector<int>
#define vll        vector<ll>
#define vs         vector<string>
#define vvii       vector<vector<ii>>
#define vvi        vector<vector<int>>
#define vvll       vector<vector<ll>>
#define sz(v)      (ll)v.size()
#define all(v)     v.begin(),v.end()
#define sc(n)      scanf("%d",&n)
#define scl(n)     scanf("%lld",&n)
#define pr1(n)     printf("%d\n",n)
#define pr2(n)     printf("%d " ,n)
#define pr4(n)     printf("%lld\n",n)
#define pr3(n)     cout<<fixed<<setprecision(2)<<n<<endl
#define endl       "\n"
#define PI         2*acos(0.0)
#define DFS_GRAY  -1
#define DFS_WHITE  0
#define DFS_BLACK  1
#define oo  1e9
#define OO  1e18
#define EPS pow(10,-9)
int dr[] = { 1, 0, -1, 0, -1, -1, 1, 1 };
int dc[] = { 0, -1, 0, 1, -1, 1, -1, 1 };
const int MAX = 500 + 7;
const int MOD = 1e9 + 7;
bool IsPrime2(ll n)
{
	if (n < 2||n%2==0)return false;
	if (n == 2)return true;
	for (ll i = 3; i*i < n; i += 2){ if (n%i == 0)return false;  } return true;
}
ll power_log(ll b, ll p){
	ll mul = b, ret = 1;
	while (p){
		if (p & 1)ret = (ret*mul);
		mul = (mul*mul);
		p >>= 1;
	}
	return ret;
}
int n,m;
void solve(int i,string s)
{
    if(m==0)return;
    if(i==n-2)
    {
        s+='1';
        s='1'+s;
        vll N;
        lop(i,2,11)
        {
            ll x=0;
            loop(j,sz(s),0)
            {
                x+=(s[j]-'0')*power_log(i,sz(s)-j-1);
            }
            if(IsPrime2(x))return;
            N.push_back(x);
        }
        cout<<s<<" ";
        lop(i,0,sz(N))
        {
            //cout<<N[i]<<" "<<IsPrime2(N[i])<<" ";continue;
            for(ll j=1;j*j<=N[i];j++)
            {
                ll a=j,b=N[i]/j;
                if(N[i]%a==0&&a!=1){cout<<a<<" ";break;}
                if(N[i]%b==0&&b!=N[i]){cout<<b<<" ";break;}
            }
        }
        cout<<endl;
        m--;
        return;
    }
    solve(i+1,s+'0');
    solve(i+1,s+'1');
}
int main()
{
	R_W;
	int t;cin>>t;
	lop(T,1,t+1)
	{
	    cin>>n>>m;
        printf("Case #%d:\n",T);
	   solve(0,"");
	}
}
