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
typedef pair<ll, ll>pii;
typedef vector<int> vi;
typedef complex<ll> point;
template <class T>  inline void smax(T &x,T y){ x = max((x), (y));}
template <class T>  inline void smin(T &x,T y){ x = min((x), (y));}
template <typename T> using os =  tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;
string s;
inline void flip(int i){
	reverse(s.begin(), s.begin() + i + 1);
			For(j,0,i+1)
				s[j] = '+' + '-' - s[j];
}
int main(int argc, char ** argv){
	iOS;
	int T;
	cin >> T;
	For(test, 1, T + 1){
		cout << "Case #" << test << ": ";
		cin >> s;
		int t = '+' + '-';
		int ans = 0;
		rof(i,s.size()-1,-1){
			if(s[i] == '+')
				continue;
			++ ans;
			if(!i)
				break ;
			if(s[0] == '+'){
				++ ans;
				int j = i;
				while(s[j] == '-')
					-- j;
				flip(j);
			}
			flip(i);
		}
		cout << ans << '\n';
	}
	return 0;
}
