#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
using namespace std;
#define Foreach(i, c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define For(i,a,b) for(int (i)=(a);(i) < (b); ++(i))
#define rof(i,a,b) for(int (i)=(a);(i) > (b); --(i))
#define rep(i, c) for(auto &(i) : (c))
#define x first
#define y second
#define pb push_back
#define PB pop_back()
#define iOS ios_base::sync_with_stdio(false)
#define sqr(a) (((a) * (a)))
#define all(a) a.begin() , a.end()
#define error(x) cerr << #x << " = " << (x) <<endl
#define Error(a,b) cerr<<"( "<<#a<<" , "<<#b<<" ) = ( "<<(a)<<" , "<<(b)<<" )\n";
#define errop(a) cerr<<#a<<" = ( "<<((a).x)<<" , "<<((a).y)<<" )\n";
#define coud(a,b) cout<<fixed << setprecision((b)) << (a)
#define L(x) ((x)<<1)
#define R(x) (((x)<<1)+1)
#define umap unordered_map
#define double long double
typedef long long ll;
typedef pair<int,int>pii;
typedef vector<int> vi;
typedef complex<double> point;
template <typename T> using os =  tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;
template <class T>  inline void smax(T &x,T y){ x = max((x), (y));}
template <class T>  inline void smin(T &x,T y){ x = min((x), (y));}
const int maxn = 220, mid = maxn/2;
double dp[maxn][maxn], p[maxn];
int n, k;
bool mark[maxn];
double ans;
inline double go(){
	memset(dp, 0, sizeof dp);
	dp[n][mid] = 1.;
	For(i,0,n){
		int p = i-1;
		if(p < 0)	p = n;
		if(mark[i])
			For(j,0,maxn){
				if(j)
					dp[i][j] += dp[p][j-1] * ::p[i];
				if(j + 1 < maxn)
					dp[i][j] += dp[p][j+1] * (1.-::p[i]);
			}
		else
			For(j,0,maxn)	dp[i][j] = dp[p][j];
	}
	smax(ans, dp[n-1][mid]);
	return dp[n-1][mid];
}
int main(){
	iOS;
	int T;
	cin >> T;
	For(IC, 1, T+1){
		cout << "Case #" << IC << ": ";
		cin >> n >> k;
		For(i,0,n)	cin >> p[i];
		sort(p, p + n);
		ans = 0;
		vi v;
		For(i,0,n)	v.pb(i);
		For(tof,0,n+3){
			For(i,0,n)	mark[v[i]] = i < k;
			go();
			rotate(v.begin(), v.end()-1,v.end());
		}
		/*For(i,0,n)
			For(j,1,k){
				memset(mark, 0, sizeof mark);
				for(int cur = i, cnt = 0; cnt < j; cur = (cur + 1) % n, ++ cnt)
					mark[cur] = true;
				For(l,0,n)	if(!mark[i]){
					int left = k-j;
					int cur = l;
					while(left){
						if(!mark[cur])	mark[cur] = true, -- left;
						cur = (cur + 1) % n;
					}
					go();
					memset(mark, 0, sizeof mark);
					for(int cur = i, cnt = 0; cnt < j; cur = (cur + 1) % n)
					mark[cur] = true;
				}
			}*/
		go();
		cout << fixed << setprecision(100) << ans << endl;
	}
	return 0;
}
