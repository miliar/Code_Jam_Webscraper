#include<bits/stdc++.h>
#define LOCAL
#define DEBUG
#define si(n) scanf("%d",&n)
#define sl(n) cin>>n
#define sf(n) scanf("%f",&n)
#define pn(n) printf("%d\n",n)
#define ps(n) printf("%d ",n)
#define pln(n) cout<<n<<endl
#define pnl() printf("\n")
#define pls(n) cout<<n<<" "
#define pl(n) cout<<n
#define FOR(i,j,n) for(i=j;i<=n;i++)
#define FORR(i,j,n) for(i=j;i>=n;i--)
#define SORT(n) std::sort(n.begin(),n.end())
#define FILL(n,a) std::fill(n.begin(),n.end(),a)
#define ALL(n) n.begin(),n.end()
#define rsz resize
#define pb push_back
#define MAXINT std::numeric_limits<int>::max()
#define MININT std::numeric_limits<int>::min()
#define getchar gc
#define putchar pc
#define iOS std::ios_base::sync_with_stdio(false)
#define endl "\n"
#ifdef DEBUG
    #define debug(x) cout << #x << " = " << x << endl
#else
    #define debug(x)
#endif
using namespace std;
typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<bool> vb;
typedef vector<vector<int> > vvi;
typedef vector<vector<ll> > vvl;
typedef pair<int,int> pii;
 
/**************** TEMPLATE ENDS HERE *************************/
const int MAXN=10;
bool app[MAXN];
bool mark(ll n) {
	int i;
	if(n==0LL) app[0]=true;
	else {
		while(n>0LL) {
			app[n%10LL]=true;
			n/=10LL;
		}
	}
	FOR(i,0,9) if(!app[i]) return false;
	return true;
}
int main() {
	int t,tt;
	ll n,m;
	si(t);
	FOR(tt,1,t) {
		sl(n);
		if(n==0LL) {
			printf("Case #%d: INSOMNIA\n",tt);
			continue;
		}
		bool done;
		memset(app,false,sizeof(app));
		m=0;
		do {
			//debug(m);
			m+=n;
			done=mark(m);
		}while(!done);
		printf("Case #%d: ",tt);
		cout<<m<<endl;
	}
	return 0;
}
