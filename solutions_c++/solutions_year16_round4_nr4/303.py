#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

int T,N;

char ch[10][10];
int tot,d[10][10],ans;
bool fg[10];

int main() {
	freopen("4.in","r",stdin);
	freopen("4.out","w",stdout);
	scanf("%d",&T);
	for (int kase = 1;kase <= T; kase++) {
		scanf("%d",&N);
		tot = 0;
		for (int i = 0;i < N; i++) {
			scanf("%s",ch[i]);
		}
		int w = 1<<(N*N); ans = N*N;
		for (int i = 0;i < w; i++) {
			int g = i;
			bool flag = true;
			int ttt = 0;
			for (int j = 0;j < N; j++)
				for (int k = 0;k < N; k++) {
					d[j][k] = g&1;
					if (ch[j][k]-'0' > d[j][k]) flag = false;
					if (ch[j][k]-'0' < d[j][k]) ttt ++;
					g >>= 1;
				}
			if (flag) {
				for (int j = 0;j < N; j++) {
					int p = 0;
					for (int k = 0;k < N; k++) 
						p += d[j][k];
					if (p == 0) flag = false;
					if (p == N) continue;
					bool ff = false;
					int gk = 0,sk = 0;
					for (int k = 0;k < N; k++) {
						if (d[j][k] == 1) {
							bool ww = true;
							for (int l = 0;l < N; l++) 
								if (l != j && d[l][k] == 1) {
									gk |= 1<<l;
								}
							sk ++;
						}
					}
					int nk = 0;
					for (int k = 0;k < N; k++)
						if ((gk>>k) & 1) nk++;
					if (nk >= sk) flag = false; 
				}
			}
			if (flag){  ans = min(ans,ttt);  }
		}
		printf("Case #%d: %d\n",kase,ans);
	}
	return 0;
}