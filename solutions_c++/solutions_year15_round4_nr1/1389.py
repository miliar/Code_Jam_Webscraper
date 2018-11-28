#include <cstdio>

char map[105][105];

int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int t;
	scanf("%d\n",&t);
	for(int u = 1; u <= t; u++){
		int r, c;
		scanf("%d %d\n",&r,&c);
		for(int i = 1; i <= r; i++){
			for(int j = 1; j<= c; j++){
				scanf("%c",&map[i][j]);
			}
			scanf("\n");
		}
		int out = 0;
		bool possible = true;
		for(int i = 1; i <= r && possible; i++){
			for(int j = 1; j <= c && possible; j++){
				if(map[i][j] != '.'){
					int valid = 0;
					for(int k = 1; k <= r; k++){
						if(k == i) continue;
						if(map[k][j] != '.'){
							if(k > i){
								valid |= 1;
							}
							else{
								valid |= 2;
							}
						}
					}
					for(int k = 1; k <= c; k++){
						if(k == j) continue;
						if(map[i][k] != '.'){
							if(k > j){
								valid |= 4;
							}
							else{
								valid |= 8;
							}
						}
					}
					if(!valid) possible = false;
					if(map[i][j] == '^' && !(valid & 2)) out++;
					if(map[i][j] == 'v' && !(valid & 1)) out++;
					if(map[i][j] == '>' && !(valid & 4)) out++;
					if(map[i][j] == '<' && !(valid & 8)) out++;
				}
			}
		}
		printf("Case #%d: ",u);
		if(!possible) printf("IMPOSSIBLE\n");
		else printf("%d\n",out);
	}
	return 0;
}

