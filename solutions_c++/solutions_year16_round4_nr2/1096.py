#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define FOR(i,l,r) for(int i=(l);i<=(r);i++)

//#define DEBUG
#ifdef DEBUG
#define print(...) fprintf(stderr, __VA_ARGS__)
#else
#define print(...) 
#endif
template<typename T,typename S>inline bool upmin(T&a,const S&b){return a>b?a=b,1:0;}
template<typename T,typename S>inline bool upmax(T&a,const S&b){return a<b?a=b,1:0;}
#define mmo(a,b) (((a)=1ll*(a)*(b)%mo)<0?(a)+=mo:(a))  //<--
#define buli(x) (__builtin_popcountll(x))
#define bur0(x) (__builtin_ctzll(x))
#define bul2(x) (63-__builtin_clzll(x))

using namespace std;
typedef long long LL;


int n,k;
double P[201];
double f[2][201][201];
double ans;
void solve(int d) {
	int z=0; FOR (i,0,k) FOR (j,0,k) f[z][i][j]=0;
	int _k=k>>1;
	int i=1;
	f[0][0][0]=1;
	while (d) {
		if (d&1) {
			z=!z;
			for (int p=0;p<=_k;p++)
				for (int q=0;q<=_k;q++) {
					if (!p&&!q) continue;
					f[z][p][q]=0;
					if (p>0) f[z][p][q]+=P[i]*f[!z][p-1][q];
					if (q>0) f[z][p][q]+=(1-P[i])*f[!z][p][q-1];
				}
		}
		d>>=1;
		i++;
	}
	ans=max(ans,f[z][_k][_k]);
}
int main() {
	int T; scanf("%d",&T);
	for (int tt=1;T--;tt++) {
		scanf("%d%d",&n,&k);
		for (int i=1;i<=n;i++) scanf("%lf",&P[i]);

		int nn=(1<<n)-1;
		ans=0;
		for (int i=0;i<=nn;i++) if (buli(i)==k) solve(i);

		printf("Case #%d: %.7f\n",tt,ans);
	}
	return 0;
}
