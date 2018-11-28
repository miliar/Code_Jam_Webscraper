#include <bits/stdc++.h>
#define ll long long
#define ull unsigned long long
#define sqr(x) ((x)*(x))
#define cube(x) ((x)*(x)*(x))
#define rep(i,n) for(ll i=0;i<(n);i++)
#define repp(i,a,b) for(ll i=(a);i<(b);++i)
#define fore(i,a,b) for(ll i=(a);i<=(b);++i)
#define ford(i,a,b,d) for(ll i=(a);i<(b);i+=(d))
#define forr(i,n,e) for(ll i=(n);i>=(e);--i)
#define forrd(i,n,e,d) for(ll i=(n);i>=(e);i-=(d))
#define repit(it,m) for(it=m.begin();it!=m.end();it++)
#define fori(it,s) for(__typeof((s).begin()) (it)=(s).begin();(it)!=(s).end();(it)++)
#define foreach(it, X) for(__typeof((X).begin()) it = (X).begin(); it != (X).end(); ++it)
#define unique(v) sort(all(v)),v.erase(unique(all(v)),v.end())
#define fill(a,b) memset(a,b,sizeof(a))
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define test ll T;cin>>T;fore(t,1,T)
#define sz size()
#define s(n) cin>>n;
#define p(n) cout<<n<<endl;
using namespace std;
typedef std::pair<ll,ll> ii;
typedef std::pair<double,double> dd;
typedef std::vector<ll> vi;
typedef std::vector<double> vd;
typedef std::vector<vi> vvi;
typedef std::vector<std::string> vs;
typedef std::vector<ii> vii;
double _st;
const ll mod = 1000000007;
const ll inf = 1e12;
const ll N = 1234567;
ll a[N],h[N];
void pre()
{

}
void solve()
{
	test
	{
        int curr=0,ans=0,len;
        string s;
        cin>>len>>s;
        len++;
        rep(i,len)
        {
            if(s[i]=='0')
                continue;
            int val = s[i]-'0';
            if(curr<i)
            {
                ans += (i-curr);
                curr += ans;
            }
            curr += val;
        }
        cout << "Case #"<<t<<": "<<ans << endl;
	}
}
void end()
{
#ifdef dexter
  fprintf(stdout,"\nTIME: %.3lf sec\n",(double)(clock()-_st)/(CLOCKS_PER_SEC));
#endif
}
int main()
{
//#ifdef dexter
  freopen("C://Users//sweet sis//Dropbox//ZONE//inout//input.txt","r",stdin);
  freopen("C://Users//sweet sis//Dropbox//ZONE//inout//output.txt","w",stdout);
  _st = clock();
//#endif
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  pre();
  solve();
  end();
  return 0;
}
