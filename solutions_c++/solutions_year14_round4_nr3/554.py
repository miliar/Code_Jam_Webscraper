#include <iostream>
#include <queue>
#include <string>
#include <vector>
#include <cmath>
using namespace std;
typedef long long i64;
#define fu(i,m,n) for(int i=m; i<n; i++)
#define fr(i,m,n) for(typeof(m) i=m; i!=n; i++)
#define fa(i,c) fr(i,(c).begin(),(c).end())

int grid[201][600];
int flow[201][600][2][5];
int seen[201][600][2];
int cap[201][600][2][5];
int dx[]={1,0,0,-1};
int dy[]={0,1,-1,0};

int cookie;

int aug(int x, int y, int w, int W, int H, int cookie) {
	if(y==H-1 && w==1) return 1;
	if(seen[x][y][w]==cookie) return 0;
	seen[x][y][w]=cookie;
	fu(d,0,5) {
		int x2=x,y2=y,w2=w,d2=4;
		if(d==4) w2=1-w;
		else {
			x2=x+dx[d];
			y2=y+dy[d];
			w2=1-w;
			d2=3-d;
		}
	       	if(flow[x][y][w][d]-flow[x2][y2][w2][d2] < cap[x][y][w][d] && aug(x2,y2,w2,W,H,cookie)) {
			flow[x][y][w][d]++;
			//cout << x << " " << y << " " << w << " " << 1 << endl;
			return 1;
		}
	}
	//cout << x << " " << y << " " << w << " " << 0 << endl;
	return 0;
}

int main(void) {
	int T;
	cin >> T;
	for(int ts=1; ts<=T; ts++) {
		int W,H,B;
		cin >> W >> H >> B;
		memset(grid,0,sizeof(grid));
		memset(flow,0,sizeof(flow));
		memset(seen,0,sizeof(seen));
		memset(cap,0,sizeof(cap));
		cookie=0;
		fu(i,0,B) {
			int x1,y1,x2,y2;
			cin >> x1 >> y1 >> x2 >> y2;
			fu(x,x1,x2+1) fu(y,y1,y2+1) grid[x][y]=1;
		}
		fu(w,0,W) fu(h,0,H) {
			if(grid[w][h]==0) cap[w][h][0][4]=1;
			fu(d,0,4) {
				int w2=w+dx[d];
				int h2=h+dy[d];
				if(w2>=0 && w2<W && h2>=0 && h2<H) cap[w][h][1][d]=1;
			}
		}
		//fu(x,0,W) fu(y,0,H) fu(w,0,2) fu(d,0,5) cout << x << endl;
		int cnt=0;
		for(;;) {
			int flowen=0;
			fu(x,0,W) if(aug(x,0,0,W,H,++cookie)) flowen++;
			cnt+=flowen;
			if(!flowen) break;
		}
		cout << "Case #" << ts << ": " << cnt << endl;
	}
}
