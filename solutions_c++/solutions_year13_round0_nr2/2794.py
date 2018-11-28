#include <cstdio>
#include <algorithm>
#define INF 0x3f3f3f3f
#define fr(i, a, b) for(int i = (a); i < (b); ++i)

using namespace std;

typedef pair<int, int> ii;

int grid[110][110];
int n, m;
int menL[110];
int menC[110];
int mark[110];

bool checaLinha(int i, int num){
	fr(j, 0, m) if(grid[i][j] > num) return false;
	return true;
}

bool checaColuna(int j, int num){
	fr(i, 0, n) if(grid[i][j] > num) return false;
	return true;
}

int main(){
	int TC;
	scanf("%d", &TC);
	bool ok;
	for(int cases = 1; TC--; ++cases){
		scanf("%d %d", &n, &m);
		ok = true;
		memset(menL, INF, sizeof menL);
		memset(menC, INF, sizeof menC);
		memset(mark, false, sizeof mark);
		fr(i, 0, n) fr(j, 0, m){
			scanf("%d", &grid[i][j]);
			menL[i] = min(menL[i], grid[i][j]);
			menC[j] = min(menC[j], grid[i][j]);
		}
		fr(i, 0, n) fr(j, 0, m){
			if(grid[i][j] == menL[i]){
				if(!checaLinha(i, menL[i]) && !checaColuna(j, menL[i])){
					ok = false; 
					break;
				}
			} else if(grid[i][j] == menC[j]){
				if(!checaLinha(i, menC[j]) && !checaColuna(j, menC[j])){
					ok = false;
					break;
				}
			}
		}
		if(ok) printf("Case #%d: YES\n", cases);
		else printf("Case #%d: NO\n", cases);
	}
	return 0;
}