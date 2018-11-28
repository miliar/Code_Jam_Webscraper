#include <iostream>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;

int T,N,R,P,S;

int d[10000],e[10000],w[500];
int tot,g[3];
string f[3][20],ans;

int ge(int d) {
	if (d == 1) return 0;
	if (d == 0) return 1;
	if (d == 2) return 2;
}

void dfs(int N,int id) {
	tot = 1; d[tot] = id;
		for (int i = 1;i <= N; i++) {
			for (int j = 1;j <= tot; j++) {
				int x = ge(d[j]),y = ge((d[j]+2) % 3);
				if (x < y) {
					e[j*2-1] = d[j]; e[j*2] = (d[j]+2) % 3;
				} else {
					e[j*2-1] = (d[j]+2) % 3; e[j*2] = d[j];
				}
			}
			tot <<= 1;
			for (int j = 1;j <= tot; j++)
				d[j] = e[j];
		}
}

int main() {
	freopen("1A.in","r",stdin);
	freopen("1A.out","w",stdout);
	scanf("%d",&T);
	for (int kase = 1;kase <= T; kase++) {
		scanf("%d%d%d%d",&N,&R,&P,&S);
		bool flag = false;
		ans = "";
		f[0][0] = "R"; f[1][0] = "P"; f[2][0] = "S";
		for (int i = 1;i <= N; i++) {
			f[0][i] = min(f[0][i-1]+f[2][i-1],f[2][i-1]+f[0][i-1]);
			f[1][i] = min(f[1][i-1]+f[0][i-1],f[0][i-1]+f[1][i-1]);
			f[2][i] = min(f[2][i-1]+f[1][i-1],f[1][i-1]+f[2][i-1]);
		}
		//cout<<f[0][N]<<" "<<f[1][N]<<" "<<f[2][N]<<endl;
		for (int i = 0;i <= 2; i++) {
			memset(w,0,sizeof w);
			tot = 1<<N;
			for (int j = 1;j <= tot; j++)
				w[f[i][N][j-1]] ++;
			if (w['R'] == R && w['P'] == P && w['S'] == S) {
				if (!flag || ans > f[i][N]) ans = f[i][N];
				flag = true;
			}
		}
		if (!flag) printf("Case #%d: IMPOSSIBLE\n",kase);
		else  { printf("Case #%d: ",kase); cout<<ans<<endl; }
	}
	return 0;
}