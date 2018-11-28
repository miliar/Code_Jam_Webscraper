
#include <bits/stdc++.h>
using namespace std;

int T,B,W,H;
int x[1024][2];
int y[1024][2];
int g[1024][1024];
bool v[1024];
int d[1024];

int dist(int l1,int r1,int l2,int r2) {
	if (l2>=l1 && l2<=r1) return 0;
	if (r2>=l1 && r2<=r1) return 0;
	if (r1>=l2 && r1<=r2) return 0;
	if (r1>=l2 && r1<=r2) return 0;
	if (l1<l2) return l2-r1-1;
	else return l1-r2-1;
}

int main() {
	freopen("inl.txt","r",stdin);
	freopen("outl.txt","w",stdout);
	scanf("%d",&T);
	for (int ww=1;ww<=T;ww++) {
		printf("Case #%d: ",ww);
		scanf("%d%d%d",&W,&H,&B);
		x[1][0]=-1,x[1][1]=-1;
		y[1][0]=0,y[1][1]=H-1;
		x[B+2][0]=x[B+2][1]=W;
		y[B+2][0]=0,y[B+2][1]=H-1;
		for (int i=2;i<B+2;i++) scanf("%d%d%d%d",x[i],y[i],x[i]+1,y[i]+1);
		for (int i=1;i<=B+2;i++)
			for (int j=1;j<i;j++) {
				g[i][j]=g[j][i]=max(dist(x[i][0],x[i][1],x[j][0],x[j][1]),
						dist(y[i][0],y[i][1],y[j][0],y[j][1]));
			}
		memset(d,63,sizeof(d));
		memset(v,false,sizeof(v));
		d[1]=0;
		for (int i=1;i<=B+2;i++) {
			int wh=0;
			for (int j=1;j<=B+2;j++)
				if (!v[j] && (wh==0 || d[j]<d[wh]))
					wh=j;
			v[wh]=true;
			for (int j=1;j<=B+2;j++)
				if (!v[j] && d[wh]+g[wh][j]<d[j])
					d[j]=d[wh]+g[wh][j];
		}
		printf("%d\n",d[B+2]);
	}
	return 0;
}
