#include <bits/stdc++.h>
using namespace std;

#define fo(x,y,z) for(int x=y;x<z;x++)
#define A first
#define B second
typedef long long ll;
typedef pair<int, int> pp;

int tc, r, c, dx[] = {1,-1,0,0}, dy[] = {0,0,1,-1}, ans;
bool pos = 1;
char m[105][105];

void go(int x, int y){
	int dir;
	if(m[x][y] == 'v') dir = 0;
	else if(m[x][y] == '^') dir = 1;
	else if(m[x][y] == '>') dir = 2;
	else dir = 3;
	bool con = 0, cost = 0;
	fo(i,0,4){
		int nx = x+dx[i], ny = y+dy[i];
		while(nx >= 0 && ny >= 0 && nx < r && ny < c){
			if(m[nx][ny] != '.'){
				if(i == dir) cost = 1;
				con = 1;
				break;
			}
			nx = nx+dx[i]; ny = ny+dy[i];
		}
	}
	if(!con) pos = 0;	
	if(!cost) ans++;
}
	

int main(){
	scanf("%d", &tc);
	fo(x,1,tc+1){
		printf("Case #%d: ", x);
		scanf("%d %d", &r, &c);
		ans = 0; pos = 1;
		fo(i,0,r) scanf(" %s ", m[i]);
		fo(i,0,r){
			fo(j,0,c){
				if(m[i][j] != '.'){
					go(i,j);
				}
			}
		}

		if(!pos) printf("IMPOSSIBLE\n");
		else printf("%d\n", ans);
	}
	return 0;
}

	
