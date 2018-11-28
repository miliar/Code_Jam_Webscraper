#include <bits/stdc++.h>
using namespace std;
#define de(x) cout << #x << " = " << x << endl
#define rep(i,a,b) for(int i=a;i<(b);++i)
#define per(i,a,b) for(int i=(b)-1;i>=(a);--i)
#define all(x) (x).begin(),(x).end()
#define sz(x) (int)(x).size()
#define mp make_pair
#define pb push_back
#define fi first
#define se second
typedef long long ll;
typedef double db;
typedef pair<int, int> pii;
typedef vector<int> vi;
const double pi = acos(-1.0), eps = 1e-8;
const int inf = ~0U >> 2 , P = 1e9 + 7;
int Pow(int x,ll t){int r=1;for(;t;t>>=1,x=(ll)x*x%P)if(t&1)r=(ll)r*x%P;return r;}
void setIO(){
	freopen("a.in","r",stdin);
	freopen("out.txt","w",stdout);
}
const int N = 111;
int T , n , m;
vi g[N];
int q[N] , in[N];
char t[20][N];int len[N];
int cnt[N];
char ss[N];
char s[N];int _ , rin[N];
bool ok(char *s,int cs){
	for(int i=0;i+len[cs]<=n;++i){
		bool ok = true;
		rep(j,0,len[cs]){
			if(s[i+j] != t[cs][j]){
				ok = false;
				break;
			}
		}
		if(ok) return 1;
	}
	return 0;
}
int sz[N];
int ttt ;
int sum[N];
void go(){
	_ = 0;
	rep(i,0,n+1) rin[i] = in[i];
	vi V;
	for(int t : g[0]) V.pb(t);
	while(sz(V)){
//		if(ttt == 1) cerr << sz(V) << "~~~" << endl;
		sum[0] = 0;
		rep(i,1,sz(V)+1) sum[i] = sum[i-1] + sz[V[i-1]];
		int t = rand() % sum[sz(V)];
		t = upper_bound(sum , sum + sz(V) + 1, t) - sum - 1;
//		if(ttt == 1) cerr << t << endl;
		int c = V[t];
		s[_++] = ss[c];
		V.erase(V.begin() + t , V.begin() + t + 1);
		for(int tt : g[c]){
			if(--rin[tt] == 0) V.pb(tt);
		}
	}
	s[_++] = 0;
//	Mp[string(s)]++;
	rep(i,0,m) if(ok(s , i)) cnt[i]++;
}
void dfs(int c,int fa){
	sz[c] = 1;
	for(auto t : g[c]) if(t != fa){
		dfs(t , c);
		sz[c] += sz[t];
	}
}
void wk(){
	scanf("%d",&n);int x;
	rep(i,0,n+1) g[i].clear() , in[i] = 0;
	rep(i,1,n+1){
		scanf("%d",&x);
		g[x].pb(i);
		in[i]++;
	}
	dfs(0 , -1);
	scanf("%s",ss + 1);
	scanf("%d",&m);
	rep(i,0,m) scanf("%s",t[i]) , len[i] = strlen(t[i]) , cnt[i] = 0;
	ttt = 0;int all = 10000;
	rep(re,0,all){
		ttt++ , go();
//		if(re == 1) cerr << re << endl;
	}
	rep(i,0,m) printf("%.10f%c",cnt[i] * 1. / all , " \n"[i + 1 == m]);
}

int main(){
	setIO();
	scanf("%d",&T);
	rep(i,1,T+1){
		cerr << i << endl;
		printf("Case #%d: ",i);
		wk();
	}
	return 0;
}
