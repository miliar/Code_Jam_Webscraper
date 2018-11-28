#include<bits/stdc++.h>

using namespace std;


#define LL 				"%I64d"
#define sz(a) 			int((a).size())
#define pb 				push_back
#define mp 				make_pair
#define F				first
#define S				second
#define all(c) 			(c).begin(),(c).end()
#define tr(c,i) 		for(typeof(c.begin()) i = c.begin(); i != c.end(); i++)
#define present(c,x) 	((c).find(x) != (c).end())
#define cpresent(c,x) 	(find(all(c),x) != (c).end()) 
#define INF				(int(1e9))
#define INFL			(int(1e18))
#define EPS				1e-12
const int inf = 100010;
const int MOD = 1000000007;
const double pi=acos(-1.0);

#define iabs(x)  ((x) > 0 ? (x) : -(x))

#define clear1(A, X, SIZE) memset(A, X, sizeof(A[0]) * (SIZE))
#define clearall(A, X) memset(A, X, sizeof(A))
#define memcopy1(A , X, SIZE) memcpy(A , X ,sizeof(X[0])*(SIZE))
#define memcopyall(A, X) memcpy(A , X ,sizeof(X))
#define max( x, y )  ( ((x) > (y)) ? (x) : (y) )

#define rep(i,a)	for(i=0;i<a;i++)
#define FOR(i,a,b)	for(i=a;i<b;i++)

int gcd(int a,int b) {return (b==0?a:gcd(b,a%b));}
int lcm(int a,int b) {return (a*(b/gcd(a,b)));}
int fx[]={0,0,1,-1};
int fy[]={-1,1,0,0};


int main() {
	ios_base::sync_with_stdio(0);
	int i=0,j;
	int n,t;
	int d,maxx=0;
	freopen("B-large.in","r",stdin);
	freopen("B-3-large.out","w",stdout);
	
	cin>>t;

	int cnt[1005];
	int k,sz;
	
	FOR(i,1,t+1) {
//		memset(cnt, 0 ,sizeof cnt);
		long long ans,minn;
		cin>>d;

		rep(j,d) {
			cin>>cnt[j];
			maxx = max(cnt[j],maxx);
		}
		minn = maxx;
		FOR(sz,1,maxx+1) {
			ans=0;
			rep(k,d) {
				ans+= (cnt[k]-1)/sz;
			}
			ans+=sz;
			minn = min(minn, ans);
		}
			
//		cout<<"ans "<<ans<<endl;
//		if(minn > maxx)
//			minn = maxx;
		cout<<"Case #"<<i<<": "<<minn<<endl;
	}
	return 0;
}	
