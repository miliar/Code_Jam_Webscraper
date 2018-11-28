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
const int maxn = 210, mod = 1e7 + 9;
bool mp[mod + 100];
vector<int> v[maxn];
inline int hs(string s, int p){
	int ans = 0;
	rep(c, s){
		ans = (1LL * p * ans)%mod;
		ans = (ans + c)%mod;
	}
	return ans;
}
inline int hhash(string s){
	int a = hs(s, 701), b = hs(s, 721);
	return (1LL * a * b)%mod;
}
int main(){
	int __T;
	cin >> __T;
	For(_TEST, 1, __T + 1){
		cout << "Case #" << _TEST << ": ";
		int n;
		cin >> n;
		string s;
		getline(cin, s);
		For(i,0,n){
			v[i].clear();
			getline(cin, s);
			stringstream ss;
			ss << s << endl;
			while(ss >> s){
				v[i].pb(hhash(s));
			}
		}
		int ans = 1e9;
		For(mask, 0, 1 << n)	if((mask & 3) == 1){
			int cnt = 0;
			For(i,0,n)	if((mask >> i) & 1)
				rep(a, v[i])
					mp[a] = 1;
			For(i,0,n)	if(!((mask >> i) & 1))
				rep(a, v[i])if(mp[a]){
					++ cnt;
					mp[a] = 0;
				}
			For(i,0,n)	if((mask >> i) & 1)
				rep(a, v[i])
					mp[a] = 0;
			smin(ans, cnt);
		}
		cout << ans << endl;
		
	}
	return 0;
}
