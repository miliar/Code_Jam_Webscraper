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
const int maxn = 4;
vi adj[maxn], adw[maxn];
bool mark[maxn];
bool block[maxn];
int mat[maxn][2];
inline bool dfs(int v){
	if(mark[v])	return false;
	mark[v] = true;
	rep(u, adj[v])	if(!block[u] && (mat[u][1] == -1 or dfs(mat[u][1])))
		return mat[v][0] = u, mat[u][1] = v, true;
	return false;
}
string s[maxn];
inline bool check(int v){
	memset(mat, -1, sizeof mat);
	block[v] = true;
	int ans = 0;
	rep(w, adw[v]){
		memset(mark, 0, sizeof mark);
		if(dfs(w))
			++ ans;
	}
	block[v] = false;
	return ans < (int)adw[v].size();
}
int n;
inline bool check(){
	For(i,0,n)	if(!check(i))	return false;
	return true;
}
int main(){
	iOS;
	int T;
	cin >> T;
	For(IC, 1, T+1){
		cout << "Case #" << IC << ": ";
		vector<pii> o;
		int N;
		cin >> n;
		For(i,0,n){
			cin >> s[i];
			For(j,0,n)	if(s[i][j] == '0')	o.pb({i, j});
		}
		N = o.size();
		int ans = N;
		For(mask, 0, 1 << N)if(__builtin_popcount(mask) < ans){
			For(i,0,n)	adw[i].clear(), adj[i].clear();
			For(i,0,n)	For(j,0,n)	if(s[i][j] == '1')adw[i].pb(j), adj[j].pb(i);
			For(i,0,o.size())	if((mask >> i) & 1){
				int v = o[i].x, u = o[i].y;
				adw[v].pb(u), adj[u].pb(v);
			}
			if(check())
				smin(ans, (int)__builtin_popcount(mask));
		}
		cout << ans << '\n';
	}
	return 0;
}
