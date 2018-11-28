#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cstring>
#include<cmath>
#include<ctime>
#include<map>
#include<string>
#include<vector>
#include<set>

using namespace std;
#define For(i,l,r) for (int i = l; i <= r; ++i)
#define Cor(i,l,r) for (int i = l; i >= r; --i)
#define Fill(a,b) memset(a,b,sizeof(a))
#define FI first
#define SE second
#define MP make_pair
#define PII pair<int,int>
#define flt double
#define INF (0x3f3f3f3f)
#define MaxN 5555
#define MaxNode 1020304
#define MD 1000000007

int v[MaxN],next[MaxN],h[MaxN],tot = 0;
void add(int b,int e) {
	v[++tot] = e; next[tot] = h[b]; h[b] = tot;
}

int in[MaxN],l[MaxN],r[MaxN],q[MaxN], a[MaxN], n;
int t[22];
void modify(int zz,int val) {
	for (int z = zz; z <= n; z += (z & -z)) t[z] = max(t[z],val);
}

int ask(int zz) {
	int ret = 0; 
	for (int z = zz; z; z -= (z & -z)) ret = max(ret, t[z]);
	return ret;
}

bool found; int tl, f[22], g[22], inq[22];
void dfs(int hd) { //cerr << hd << endl;
	if (hd == 3) {
		int z = hd;
	}
	if (q[1] == 8 && q[2] == 6) {
		int z = hd;
	}
	if (q[1] == 8 && q[2] == 6 && q[3] == 3) {
		int z = hd;
	}
	if (q[1] == 8 && q[2] == 6 && q[3] == 3 && q[4] == 1) {
		int z = hd;
	}
	if (hd > n) {
		Fill(t,0); bool fl = true;
		For(i,1,n) a[q[i]] = i;
		For(i,1,n) {
			f[i] = ask(a[i]) + 1;
			if (f[i] != l[i]) {
				return ;
			}
			modify(a[i],f[i]);
		}
		Fill(t,0);
		Cor(i,n,1) {
			g[i] = ask(a[i]) + 1;
			if (g[i] != r[i]) {
				return ;
			}
			modify(a[i],g[i]);
		}
		//For(i,1,n) printf("%d ",f[i]); puts("");
		//For(i,1,n) printf("%d ",g[i]); puts("");
		For(i,1,n) printf("%d ",a[i]); puts(""); found = true;
		return ;
	}
	if (found) return ;
	int Tot = 0; int cache[22];
	For(i,1,n) if (in[i] == 0 && !inq[i]) cache[++Tot] = i;
	//random_shuffle(cache + 1,cache + Tot + 1);
	For(i,1,Tot) {
		q[hd] = cache[i]; inq[cache[i]] = true;
		for (int z = h[cache[i]]; z; z = next[z]) {
			--in[v[z]];
		}
		dfs(hd + 1); inq[cache[i]] = false ;
		for (int z = h[cache[i]]; z; z = next[z]) {
			if (++in[v[z]] == 1) --tl;
		}
	}
}

int main() {
	freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);
	int T; cin >> T;
	For(TTT,1,T) { printf("Case #%d: ",TTT); cerr << TTT << endl;
		if(TTT==4){
			int z=TTT;
		}
		cin >> n;
		For(i,1,n) scanf("%d",&l[i]);
		For(i,1,n) scanf("%d",&r[i]); Fill(h,tot = 0); Fill(in,0);
		For(i,1,n) For(j,1,i - 1) {
			if (l[i] <= l[j]) add(i,j), ++in[j];
		}
		For(i,1,n) For(j,i + 1,n) {
			if (r[i] <= r[j]) add(i,j), ++in[j];
		}
		found = false ;
		For(i,1,n) if (in[i] == 0) {
			Fill(inq,0); inq[i] = 1;
			q[tl = 1] = i; 
			for (int z = h[i]; z; z = next[z]) {
				--in[v[z]];
			}
			dfs(2); if (found) break ;
			for (int z = h[i]; z; z = next[z]) {
				++in[v[z]];
			}
		}
		/*int hd = 0, tl = 0;
		For(i,1,n) if (in[i] == 0) q[++tl] = i;
		while (hd < tl) {
			int vex = q[++hd];
			for (int z = h[vex]; z; z = next[z]) if (--in[v[z]] == 0) q[++tl] = v[z];
		}*/
	}
	return 0;
}

