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
  
const int maxn = 1000 + 10;
int n,k,ca, ans[maxn];
std::vector<pair<int, int> > P;

int fun(int x, std::vector<PII> &a, std::vector<PII> &b){
	map<int,int> M; M.clear();
	rep(i,SZ(a)) M[a[i].X] = a[i].Y;
	int fu = 0;
	if(x<0) x = -x, fu = 1;
	// printf("x %d\n", x);
	b.clear();
	map<int,int>::ITR it;
	for(it = M.begin(); it!=M.end(); ++it){
		// printf("%d %d\n", it->X, it->Y);
		if(it->Y < 0) return 0;
		if(it->Y == 0) continue;
		if(M.count(it->X + x) == 0) return 0;
		if(x==0){
			if(it->Y % 2) return 0;
			if(it->Y > 0) b.PB(MK(it->X, it->Y / 2));	
			continue;
		}
		M[it->X + x] -= it->Y;
		if(it->Y > 0) b.PB(MK(it->X, it->Y));
	}
	// printf("??\n");
	if(fu) rep(i, SZ(b)) b[i].X += x;
	return 1;
}

int tot;
bool run(int u, vector<pair<int,int> > P){
	// printf("%d\n", u);
	// rep(i, SZ(P)) printf("%d ", P[i].X); printf("\n");
	// rep(i, SZ(P)) printf("%d ", P[i].Y); printf("\n");
	tot = u;
	if(SZ(P) == 1 && P[0].Y==1){
		return 1;
	}
	std::vector<pair<int,int> > Q;
	rep(i, SZ(P)){
		int o;
		if(o = fun(P[i].X, P, Q)){
			ans[u] = P[i].X;
			if(run(u+1, Q)) return 1;
		}
	}
	return 0;
}

int main(int argc, char const *argv[])
{
	int cas = getint();
	for(ca=0; ca < cas; ca++){
		printf("Case #%d: ", ca+1);
		n = getint();
		P.resize(n);
		rep(i,n) P[i].X = getint();
		rep(i,n) P[i].Y = getint(); 
		assert(run(0, P) == 1);
		rep(i, tot) printf("%d ", ans[i]); printf("\n");
	}	
	cerr << runtime();
	return 0;
}