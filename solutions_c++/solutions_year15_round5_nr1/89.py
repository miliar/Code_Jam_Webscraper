#include "cstdio"
#include "iostream"
#include "algorithm"
#include "cmath"
#include "cstring"
#include "cstdlib"
#include "climits"
#include "cassert"
#include "bitset"
#include "complex"
#include "queue"
#include "vector"
#include "queue"
#include "set"
#include "map"
#define runtime() ((long double)clock() / CLOCKS_PER_SEC)
#define rep(i, n) for(int i=0; i<n; i++)
#define repp(i, a, b) for(int i=a; i<a+b; i++)
using namespace std;
#define SZ(x) ((int)(x).size())
#define PB push_back
#define MK make_pair
#define X first
#define Y second
#define ll long long
#define ull unsigned long long
#define ITR iterator
#define LB lower_bound
#define UB upper_bound
#define PII pair<int, int>
#define CLR(a) memset(a, 0, sizeof(a))
int getint(){
    int s = 0, o = 1;
    char c;
    for(c = getchar(); c<'0'||c>'9';c = getchar()) if(c=='-') o = -1;
    for(;c>='0'&&c<='9'; c = getchar()) s *=10, s+=c-'0';
    return s*o;
}
  
const int maxn = 1000000 + 10;

long long s[maxn], m[maxn];
long long As, Cs, Rs, Am, Cm, Rm;
int n, low, ans, timer, cnt, D;
int vis[maxn];
std::vector<int> e[maxn];
int ca;
pair<int,int> P[maxn];

// void dfs(int u){
// 	rep(i, SZ(e[u])){
// 		int v = e[u][i];
// 		P[v].X = min((int)s[v], P[u].X);
// 		P[v].Y = max((int)s[v], P[u].Y);
// 		dfs(v);
// 	}
// }

void bfs(){
	static int que[maxn];
	int l = 0, r = 1;
	que[0] = 0;
	while(l<r){
		int u = que[l++];
		rep(i, SZ(e[u])){
			int v = e[u][i];
			P[v].X = min((int)s[v], P[u].X);
			P[v].Y = max((int)s[v], P[u].Y);
			que[r++] = v;			
		}
	}
}

bool cmp(pair<int,int> a, pair<int,int> b){
	return a.Y < b.Y;
}

priority_queue<int> Q;

void run(){
	rep(i,n) e[i].clear();
	repp(i,1,n-1) e[m[i] % i].PB(i);
	ans = 0;
	P[0] = MK(s[0], s[0]);
	// dfs(0);
	bfs();
	sort(P, P+n, cmp);
	while(!Q.empty()) Q.pop();
	int now = 0;
	for(int l = s[0] - D, r = s[0]; l <= s[0]; ++l, ++r){
		while(now < n && P[now].Y <= r) Q.push(-P[now++].X);
		while(!Q.empty() && -Q.top() < l) Q.pop();
		ans = max(ans, SZ(Q));
	}
	printf("%d\n", ans);
}
int main(int argc, char const *argv[])
{
	int cas = getint();
	for(ca=0; ca < cas; ca++){
		printf("Case #%d: ", ca+1);
		n = getint(), D = getint();
		cin >> s[0] >> As >> Cs >> Rs >> m[0] >> Am >> Cm >> Rm;
		rep(i,n-1){
			s[i+1] = (s[i] * As + Cs) % Rs;
			m[i+1] = (m[i] * Am + Cm) % Rm;
			// printf("%lld %lld\n", s[i+1], m[i+1]);
		}
		run();
	}	
	cerr << runtime();
	return 0;
}