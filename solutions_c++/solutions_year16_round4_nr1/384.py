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
int w[3][3];
// P R S
string g = "PRS";
const int mx = 13;
vector<vi> al[13];
int l[3];
void go(int lvl , vi v){
	al[lvl].pb(v);
	if(lvl == 12)	return ;
	vi u;
	rep(a, v){
		int b = l[a];
		u.pb(a);
		u.pb(b);
	}
	for(int l = 1; l < u.size(); l <<= 1){
		vector<vi> V;
		for(int i = 0; i < u.size(); i += l){
			vi e;
			For(j,0,l)	e.pb(u[i + j]);
			V.pb(e);
		}
		for(int i = 0;i < V.size(); i += 2)
			if(V[i] > V[i+1])	swap(V[i], V[i+1]);
		u.clear();
		rep(e, V)
			rep(a, e)
			u.pb(a);
	}
	go(lvl+1, u);
}
int main(){
	iOS;
	memset(w, -1, sizeof w);
	w[0][1] = w[1][0] = 0;
	w[0][2] = w[2][0] = 2;
	w[1][2] = w[2][1] = 1;
	For(i,0,3)	For(j,0,3)	if(w[i][j] == i)	l[i] = j;
	For(i,0,3)
		go(0, vi(1, i));
	For(i,0,13)	sort(all(al[i]));
	int T;
	cin >> T;
	For(IC, 1, T+1){
		cout << "Case #" << IC << ": ";
		bool fnd = 0;
		int n;
		int cnt[3];
		cin >> n;
		cin >> cnt[1] >> cnt[0] >> cnt[2];
		rep(v, al[n]){
			bool ok = 1;
			For(i,0,3)	if(count(all(v), i) != cnt[i]){ok = 0; break;}
			if(ok){
				fnd = 1;
				rep(i, v)	cout << g[i];
				cout << endl;
				break ;
			}
		}
		if(!fnd)
			cout << "IMPOSSIBLE" << endl;
	}
	return 0;
}
