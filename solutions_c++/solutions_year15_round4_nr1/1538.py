#include <bits/stdc++.h>

using namespace std;

#define MAXN 1005

int N, M;
char mapa[MAXN][MAXN];
bool vis[MAXN][MAXN];
int fin[MAXN][MAXN];
bool fall;
int C;
int movs[4][2] = {{-1,0},
					{0,1},
					{1,0},
					{0,-1}
				};
				
int dire(char x, int d){
	if(x == '^')
		return 0;
	else if(x == '>')
		return 1;
	else if(x == 'v')
		 return 2;
	else if(x == '<')
		return 3;
	return d;
}

bool fuera(int y, int x){
	if(x < 1 || y < 1 || x > M || y > N)
		return false;
	return true;
}

void busca(int y, int x, int d){
	if(x < 1 || y < 1 || x > M || y > N){
		fin[y][x] = max(fin[y][x], C);
		return;
	}
	//cout << y << " "<< x << " "<< d << endl;
	if(vis[y][x])
		return;
	vis[y][x] = true;
	if(mapa[y][x] != '.')
		C++;
	d = dire(mapa[y][x], d);
	busca(y + movs[d][0], x + movs[d][1], d);
	vis[y][x] = false;
}
				
int main(){
	int T;
	cin >> T;
	for(int caso = 1; caso <= T; caso++){
		printf("Case #%d: ", caso);
		cin >> N >> M;
		int ans = 0;
		for(int i = 1; i <= N; i++)
			scanf("%s", mapa[i] + 1);
		bool can = false;
		for(int i = 1; i <= N; i++){
			for(int j = 1; j <= M; j++){
				if(mapa[i][j] != '.'){
					int d = dire(mapa[i][j], -1);
					int y = i, x = j;
					y += movs[d][0];
					x += movs[d][1];
					while(mapa[y][x] == '.' && fuera(y, x)){
						y += movs[d][0];
						x += movs[d][1];
					}
					if(!fuera(y, x))
						ans++;
					bool sepuede = false;
					for(d = 0; d < 4; d++){
						y = i, x = j;
						y += movs[d][0];
						x += movs[d][1];
						while(mapa[y][x] == '.' && fuera(y, x)){
							y += movs[d][0];
							x += movs[d][1];
						}
						if(fuera(y, x))
							sepuede = true;
					}
					if(!sepuede){
						can = true;
					}
				}
				
			}
		}
		if(can)
			puts("IMPOSSIBLE");
		else
			cout << ans << endl;
	}
	return 0;
}