#include<cstdio>
#include<algorithm>
#include<stack>
#include<queue>
#include<vector>
#include<string>
#include<string.h>
#include<cstdlib>
#include<ctime>
#include<cmath>
#include<map>
#include<set>
#include<iostream>
#include<sstream>
#include<sys/time.h>
#define fi first
#define se second
#define rep(i,n) for(int i = 0; i < n; i++)
#define rrep(i,n) for(int i = 1; i <= n; i++)
#define drep(i,n) for(int i = n-1; i >= 0; i--)
#define gep(i,g,j) for(int i = g.head[j]; i != -1; i = g.e[i].next)
#define each(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();it++)
#define rng(a) a.begin(),a.end()
#define maxs(x,y) x = max(x,y)
#define mins(x,y) x = min(x,y)
#define pb push_back
#define sz(x) (int)(x).size()
#define pcnt __builtin_popcount
#define snuke srand((unsigned)clock()+(unsigned)time(NULL))
using namespace std;
typedef long long int ll;
typedef pair<int,int> P;
typedef vector<int> vi;

const int MX = 100005, INF = 1000010000;
const ll LINF = 1000000000000000000ll;
const double eps = 1e-10;
const int dx[] = {-1,0,1,0}, dy[] = {0,-1,0,1}; //<^>v

// Mod int
const int mod = 1000000007;
struct mint;
mint ex(mint a, ll tms);
struct mint{
	ll x;
	mint():x(0){}
	mint(ll x):x(x){}
	mint operator+=(mint a){ if((x+=a.x)>=mod) x-=mod; return *this;}
	mint operator-=(mint a){ if((x+=mod-a.x)>=mod) x-=mod; return *this;}
	mint operator*=(mint a){ (x*=a.x)%=mod; return *this;}
	mint operator/=(mint a){ (x*=ex(a,mod-2).x)%=mod; return *this;}
	mint operator+(mint a){ return mint(*this) += a;}
	mint operator-(mint a){ return mint(*this) -= a;}
	mint operator*(mint a){ return mint(*this) *= a;}
	mint operator/(mint a){ return mint(*this) /= a;}
};
mint ex(mint a, ll tms){
	if(!tms) return 1;
	mint res = ex(a,tms/2);
	res *= res;
	return (tms&1)?res*a:res;
}
struct invs:vector<mint>{
	invs(){}
	invs(int mx):vector<mint>(mx,0){
		(*this)[1] = 1;
		for(int i=2;i<=mx;i++) (*this)[i] = (*this)[mod%i]*(mod-mod/i);
	}
};
struct ex2:vector<mint>{
	ex2(){}
	ex2(int mx):vector<mint>(mx){
		(*this)[0] = 1;
		for(int i=1;i<=mx;i++) (*this)[i] = (*this)[i-1]*2;
	}
};
struct comb{
	vector<mint> f, g;
	comb(){}
	comb(int mx):f(mx+1),g(mx+1){
		f[0] = 1;
		rrep(i,mx) f[i] = f[i-1]*i;
		g[mx] = ex(f[mx],mod-2);
		for(int i=mx;i>0;i--) g[i-1] = g[i]*i;
	}
	mint c(int a, int b){ return f[a]*g[b]*g[a-b];}
};
//

vi em(26,-1);
struct Trie {
	vi d, e;
	vector<vi> to;
	comb c;
	int wo, n;
	mint ans;
	Trie(){ d.pb(0); to.pb(em); wo = 0; ans = 1; c = comb(105);}
	void add(string& s){
		int l = sz(s);
		int i = 0;
		rep(j,l){
			if(to[i][s[j]-'A'] == -1){
				to[i][s[j]-'A'] = sz(d);
				d.pb(0);
				to.pb(em);
			}
			i = to[i][s[j]-'A'];
			if(j == l-1) d[i] = 1;
		}
	}
	int sol(int v){
		vi a;
		rep(i,26){
			int u = to[v][i];
			if(u == -1) continue;
			a.pb(sol(u));
		}
		if(d[v]) a.pb(1);
		int s = 0;
		rep(i,sz(a)) s += a[i];
		s = min(s,n);
		wo += s;
		mint x = 0, y;
		rrep(i,s){
			y = 1;
			rep(j,sz(a)){
				if(i < a[j]){
					y = 0;
					break;
				}
				y *= c.c(i,a[j]);
			}
			x = (y*c.c(s,i)) - x;
			//printf("%d %d : %lld %lld\n",v,i,y.x,x.x);
		}
		ans *= x;
		return s;
	}
};

int main(){
	int ts;
	scanf("%d",&ts);
	rrep(ti,ts){
		int n, m;
		scanf("%d%d",&m,&n);
		string s;
		Trie t;
		rep(i,m){
			cin >> s;
			t.add(s);
		}
		t.n = n;
		t.sol(0);
		printf("Case #%d: %d %lld\n",ti,t.wo,t.ans.x);
	}
	
	return 0;
}





