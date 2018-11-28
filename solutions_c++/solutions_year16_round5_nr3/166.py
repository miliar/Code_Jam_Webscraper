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
const int maxn = 1000 + 10;
double x[maxn], y[maxn], z[maxn], vx[maxn], vy[maxn], vz[maxn];
int par[maxn];
int root(int v){return par[v] < 0 ? v : par[v] = root(par[v]);}
inline bool merge(int x, int y){
	x = root(x), y = root(y);
	if(x == y)	return false;
	if(par[y] < par[x])	swap(x, y);
	par[x] += par[y];
	par[y] = x;
	return true;
}
int n, s;
inline double dis2(int i, int j){
	double X = x[i] - x[j];
	double Y = y[i] - y[j];
	double Z = z[i] - z[j];
	return X * X + Y * Y + Z * Z;
}
inline bool check(double d){
	fill(par,par + n,-1);
	double D = d * d;
	For(i,0,n)	For(j,0,i)	if(dis2(i, j) <= D)	merge(i, j);
	return root(0) == root(1);
}
int main(){
	iOS;
	int T;
	cin >> T;
	for(int ts = 1; ts <= T; ts ++){
		cout << "Case #" << ts << ": ";
		cin >> n >> s;
		For(i,0,n)
			cin >> x[i] >> y[i] >> z[i] >> vx[i] >> vy[i] >> vz[i];
		double lo = 0, hi = 1e9;
		while(hi - lo > 1e-9){
			double mid = (lo + hi)/2.;
			if(check(mid))
				hi = mid;
			else
				lo = mid;
		}
		coud(lo, 50) << endl;
	}
}
