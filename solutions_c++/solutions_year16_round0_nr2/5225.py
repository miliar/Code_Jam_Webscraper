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
void solve(string s)
{
   int ans=0;
   int pos=0;
  lop(i,0,sz(s))
  {
      if(s[i]=='-')
      {
          int x=i;
          lop(j,i+1,sz(s))if(s[j]=='-')x++;else break;
          ans++;
          ans+=pos;
          i=x;
      }else pos=1;
  }
  cout<<ans<<endl;
}
int main()
{
	R_W;
	int t;cin>>t;
	lop(T,1,t+1)
	{
	    string s;cin>>s;
        printf("Case #%d: ",T);
	   solve(s);
	}
}
