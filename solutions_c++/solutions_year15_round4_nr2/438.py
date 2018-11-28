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
const int maxn = 2000;
int n;
const double eps = 1e-9;
double v,x,r[maxn],c[maxn];
int main(){
	int __T;
	cin >> __T;
	For(_TEST, 1, __T + 1){
		cout << "Case #" << _TEST << ": ";
		cin >> n >> v >> x;
		For(i,0,n)
			cin >> r[i] >> c[i];
		bool imp = 0;
		double ans = eps;
		if(n == 2){
			if((double)fabs(c[0] - c[1]) < eps)
				r[0] += r[1], n--;
			else{
				double v0 = (v * (x - c[1]))/(c[0] - c[1]);
				double v1 = v - v0;
				ans = max((double)(v0/r[0]), (double)(v1/r[1]));
				if(max(c[0], c[1]) < x or min(c[0], c[1]) > x)
					imp = 1;
			}
		}
		if(n == 1){
			if(c[0] > x or c[0] < x)
				imp = 1;
			else
				ans = v/r[0];
		}
		if(imp)
			cout << "IMPOSSIBLE\n";
		else if(n > 2)
			cout << "FUCK\n";
		else
			coud(ans,9) << endl;
		}
	return 0;
}
