#include <bits/stdc++.h>

using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
#define lb lower_bound
#define ub upper_bound
#define pb push_back
#define mp make_pair
#define ll long long
#define fi(filename) freopen(filename, "r", stdin)
#define fo(filename) freopen(filename, "w", stdout)
#define popcount(i) __builtin_popcount(i)      //count one. in long long use __builtin_popcountll(i)
#define gcd __gcd
#define parity(i)   __builtin_parity(i)       //evenparity 0 and odd parity 1
#define btz(a)   __builtin_ctz(a)            //count binary trailling zero
#define blz(a)   __builtin_clz(a)            //count binary leading zero
//debug
#define debug(args...) cerr<<__FUNCTION__<<":"<<__LINE__<<" ";do{cerr<<#args<<": ";dbg,args;cerr<<endl;} while(0)
struct debugger
{template<typename T> debugger& operator ,(const T& v){cerr<<v<<" ";return *this;}}dbg;
#define dbgarr(a,start,end) cerr<<__FUNCTION__<<":"<<__LINE__<<"\n";for(ll i=start;i<end;i++) cerr<<#a<<"["<<i<<"] -> "<<a[i]<<" "<<endl;
#define dbgmat(mat,row,col) cerr<<__FUNCTION__<<":"<<__LINE__<<"\n";for(ll i=0;i<row;i++) {for(ll j=0;j<col;j++) cerr<<mat[i][j]<<" ";cerr<<endl;}
#define F(i,a,n) for(typeof(a) i=(a);i<(n);++i)
#define R(i,a,n) for(typeof(a) i=(a);i>=(n);--i)
#define tr(it,container) for(typeof(container.begin()) it = container.begin(); it != container.end(); ++it)
#define S(x) scanf("%d",&x)
#define Sl(x) scanf("%lld",&x)
#define P(x) printf("%d\n",x)
#define Pl(x) printf("%lld\n",x)
#define M(x,i) memset(x,i,sizeof(x))      // useful to clear array of integer
#define fr first
#define se second
#define INF 2147483647
#define MOD 1000000007   //	(int)1e9+7
#define all(x)    x.begin(),x.end()

int main()
{
	int t,n,no=0,ans,standing;
	char a[2000];
	S(t);
	while(t--) {
		ans=0;
		++no;
		S(n);
		scanf("%s",a);
		standing=a[0]-'0';
		F(i,1,n+1) {
			if(standing<i&&(a[i]-'0')) {
				ans+=i-standing;
				standing+=i-standing;
			}
			else {
			}
			standing+=a[i]-'0';
		}
		printf("Case #%d: %d\n",no,ans);
	}
	return 0;
}

