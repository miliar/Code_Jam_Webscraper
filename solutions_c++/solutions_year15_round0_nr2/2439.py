#include <bits/stdc++.h>
using namespace std;

#define s(n)            scanf("%d",&n)
#define sl(n)           scanf("%lld",&n)
#define sf(n)           scanf("%lf",&n)
#define ss(n)           scanf("%s",n)
#define pls(x)          cout << x << " "
#define pln(x)          cout << x << "\n"
#define pis(x)          printf("%d ", x)
#define pin(x)          printf("%d\n", x)
#define pnl             printf("\n")
#define dbn             cerr << "\n"
#define dbg(x)          cerr << #x << " : " << x << " "
#define dbs(x)          cerr << x << " "
#define FOR(i,a,b)      for(int i=a;i<=b;i++)
#define rep(i,n)        FOR(i,0,n-1)
#define foreach(c,v)    for(__typeof((c).begin()) v = (c).begin();  v != (c).end(); ++v)
#define mp              make_pair
#define FF              first
#define SS              second
#define pb              push_back
#define fill(a,v)       memset(a,v,sizeof(a))
#define all(x)          x.begin(),x.end()
#define sz(v)           ((int)(v.size()))
#define INF             (int)1e9
#define LINF            (long long)1e18
#define EPS             1e-9
#define INDEX(arr,ind)  (lower_bound(all(arr),ind)-arr.begin())

typedef long long int lli;
typedef pair<int,int> pii;
typedef pair<lli,lli> pll;
typedef vector<int> vi;
typedef vector<lli> vlli;
typedef vector<pii> vii;

const int MAXN = 200015;
const int MOD  = 1000000007;

/*Main code begins now */

vi P;
bool go(int nPicks,int totalMin){
	queue<int> newP;
	rep(i,sz(P)){
		if(P[i] > totalMin) newP.push(P[i] - totalMin);
	}
	while(!newP.empty()){
		int cakes = newP.front();
		newP.pop();
		if(cakes>0 and nPicks == 0) return false;
		if(cakes > totalMin) newP.push(cakes-totalMin);
		nPicks--;
	}
	return true;
}
int main()
{
	int t,x,n;
	s(t);
	rep(q,t){
		P.clear();
		printf("Case #%d: ",q+1);
		s(n);
		rep(i,n) s(x),P.pb(x);
		sort(all(P));
		int ans = INF;
		rep(i,1001){
			int low = 1;
			int high = 1000;
			while(low < high){
				int mid = low + (high - low)/2;
				if(go(i,mid)) high = mid;
				else low = mid + 1;
			}
			ans = min(ans, i + low);
		}
		printf("%d\n",ans);
	}
	return 0;
}
