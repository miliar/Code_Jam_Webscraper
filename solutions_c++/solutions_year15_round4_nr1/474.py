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
const int maxn = 150;
string s[maxn];
inline bool v(char c){return c != '.';}
int n, m;
inline bool imp(int x,int y){
	int t = 0;
	if(!v(s[x][y]))
		return false;
	For(i,0,n)
		if(v(s[i][y]))
			++ t;
	For(i,0,m)
		if(v(s[x][i]))
			++ t;
	return (t == 2);
}
int main(){
	int __T;
	cin >> __T;
	For(_TEST, 1, __T + 1){
		cout << "Case #" << _TEST << ": ";
		cin >> n >> m;
		For(i,0,n)
			cin >> s[i];
		int ans = 0;
		bool im = 0;
		For(i,0,n)
			For(j,0,m)if(v(s[i][j])){
				if(s[i][j] == '<'){
					++ ans;
					if(imp(i, j))	im = 1;
				}
				break ;
			}
		For(i,0,n)
			rof(j,m-1,-1)if(v(s[i][j])){
				if(s[i][j] == '>'){
					++ ans;
					if(imp(i, j))	im = 1;
				}
				break ;
			}
		For(j,0,m)
			For(i,0,n)if(v(s[i][j])){
				if(s[i][j] == '^'){
					++ ans;
					if(imp(i, j))	im = 1;
				}
				break ;
			}
		For(j,0,m)
			rof(i,n-1,-1)if(v(s[i][j])){
				if(s[i][j] == 'v'){
					++ ans;
					if(imp(i, j))	im = 1;
				}
				break ;
			}
		if(im)
			puts("IMPOSSIBLE");
		else
			cout << ans << endl;
	}
	return 0;
}
