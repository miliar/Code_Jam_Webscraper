
#include <bits/stdc++.h>
using namespace std;

int T;
int P,Q,N;
int H[128];
int G[128];
int d[128];
int c[128];
int f[128][1024];
int th[128];

int main() {
	freopen("inl.txt","r",stdin);
	freopen("outl.txt","w",stdout);
	scanf("%d",&T);
	for (int ww=1;ww<=T;ww++) {
		printf("Case #%d: ",ww);
		memset(f,255,sizeof(f));
		scanf("%d%d%d",&P,&Q,&N);
		f[0][1]=0;
		for (int i=1;i<=N;i++) scanf("%d%d",H+i,G+i);
		for (int i=1;i<=N;i++) {
			c[i]=(H[i]+Q-1)/Q;
			d[i]=-1;
			for (int j=0;P*j<=H[i];j++) {
				int t=H[i]-j*P;
				int tmp=(t+Q-1)/Q-1;
				if (t-tmp*Q>0 && t-tmp*Q<=P) {
					th[i]=tmp;
					d[i]=j;
					break;
				}
			}
			if (d[i]==-1) {
				th[i]=0;
				d[i]=(H[i]+P-1)/P-1;
			}
		}
		for (int i=0;i<N;i++)
			for (int j=0;j<1024;j++)
				if (f[i][j]!=-1) {
					f[i+1][j+c[i+1]]=max(f[i+1][j+c[i+1]],f[i][j]);
					//int ht=(H[i+1]-d[i+1]*P)/Q;
					int ht=th[i+1];
					if (j+ht>d[i+1])
						f[i+1][j+ht-d[i+1]-1]=max(f[i+1][j+ht-d[i+1]-1],f[i][j]+G[i+1]);
				}
		int ans=0;
		for (int i=0;i<1024;i++)
			if (f[N][i]>ans) ans=f[N][i];
		printf("%d\n",ans);
	}
	return 0;
}
