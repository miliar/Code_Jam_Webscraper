///*
#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

int W, H, B, t;
int R[105][505];
int chk[105][505];
int xx[4] = {0, -1, 0, 1};
int yy[4] = {-1, 0, 1, 0};

bool DFS(int x, int y, int ad)
{
	chk[x][y] = t;
	if( y == H-1) return true;
	ad--; if(ad == -1) ad = 3;
	for(int i = ad, ch = 0; ch != 1 || i!= ad; i = (i+1)%4, ch = 1 ){
		int px = x + xx[i], py = y + yy[i];
		if(0 > px || px >= W || 0 > py || py >= H || R[px][py] == 1 || chk[px][py] == t) continue;
		if( DFS(px, py, i) ){
			return true;
		}
	}
	return false;
}

int solve()
{
	int ans = 0;
	for(int i = 0; i < W; i++){
		if(R[i][0] == 0 && chk[i][0] != t){
			ans += DFS(i, 0, 2);
		}
	}
	return ans;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int T;
	scanf("%d", &T);

	for(t = 1; t <= T; t++){
		int sx, sy, ex, ey;
		printf("Case #%d: ", t);
		scanf("%d%d%d", &W, &H, &B);
		for(int x = 0; x < W; x++){
			for(int y = 0; y < H; y++){
				R[x][y] = 0;
			}
		}
		for(int i = 0; i < B; i++){
			scanf("%d%d%d%d", &sx, &sy, &ex, &ey);
			for(int x = sx; x <= ex; x++){
				for(int y = sy; y <= ey; y++){
					R[x][y] = 1;
				}
			}
		}
		printf("%d\n", solve());
	}
	return 0;
}

//*/