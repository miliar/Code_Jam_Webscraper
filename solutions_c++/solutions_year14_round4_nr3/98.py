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
#define MaxN 1020304
#define MaxNode 1020304
#define MD 1000000007

struct Rect {
	int x[2], y[2];
	Rect() {}
	void read() {
		scanf("%d%d%d%d",&x[0], &y[0], &x[1], &y[1]);
	}
}A[1111];

int inner(int l, int r, int x) {
	return l <= x && x <= r;
}

int intersect(int l1, int r1, int l2, int r2) {
	return inner(l1,r1,l2) || inner(l1,r1,r2) || inner(l2,r2,l1) || inner(l2,r2,r1);
}

int Dist(Rect x, Rect y) {
	int xDist = INF, yDist = INF;
	if (intersect(x.x[0],x.x[1],y.x[0],y.x[1])) xDist = 0; else xDist = abs(min(x.x[1],y.x[1]) - max(x.x[0],y.x[0])) - 1;
	if (intersect(x.y[0],x.y[1],y.y[0],y.y[1])) yDist = 0; else yDist = abs(min(x.y[1],y.y[1]) - max(x.y[0],y.y[0])) - 1;
	return max(xDist,yDist);
}	
	
int n,MAP[1111][1111],d[1111];
bool vis[1111];
int main() {
	freopen("input.txt","r",stdin); //freopen("output.txt","w",stdout);
	int Tcase; cin >> Tcase;
	For(TTT,1,Tcase) {
		printf("Case #%d: ",TTT);
		int W,H;
		scanf("%d%d%d",&W,&H,&n);
		For(i,1,n) A[i].read();
		if (!n) {
			cout << W << endl;
			continue ;
		}
		int S = n + 1, T = S + 1;
		Fill(MAP,INF);
		For(i,1,n) For(j,1,n) {
			MAP[i][j] = Dist(A[i],A[j]);
		}
		For(i,1,n) MAP[S][i] = A[i].x[0];
		For(i,1,n) MAP[i][T] = W - A[i].x[1] - 1;
		Fill(d,INF);
		d[S] = 0;
		Fill(vis,0);
		For(i,1,T) {
			PII Min = MP(INF,-1);
			For(j,1,T) if (!vis[j]) Min = min(Min,MP(d[j],j));
			if (Min.SE == -1) {
				cerr << "ERROR" << endl; while(1);
			}
			int p = Min.SE;
			vis[p] = true;
			For(j,1,T) d[j] = min(d[j],d[p] + MAP[p][j]);
		}
		cout << d[T] << endl;
	}
	return 0;
}

