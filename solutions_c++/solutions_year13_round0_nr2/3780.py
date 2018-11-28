#include <cstdio>

#define MAX 110

int cc;

int w, h, map[MAX][MAX];
bool chk[MAX][MAX];

void input(){
	scanf("%d%d", &h, &w);

	int i, j;
	for(i=0; i<h; i++){
		for(j=0; j<w; j++){
			scanf("%d", &map[i][j]);
			chk[i][j] = false;
		}
	}
}

void solve(){
	int i, j, min;
	for(min=1; min<=100; min++){
		for(i=0; i<h; i++){
			for(j=0; j<w; j++)
				if(map[i][j] > min)
					break;

			if(j == w){
				for(j=0; j<w; j++)
					if(map[i][j] == min)
						chk[i][j] = true;
			}
		}

		for(j=0; j<w; j++){
			for(i=0; i<h; i++)
				if(map[i][j] > min)
					break;
			
			if(i == h){
				for(i=0; i<h; i++)
					if(map[i][j] == min)
						chk[i][j] = true;
			}
		}
	}

	for(i=0; i<h; i++){
		for(j=0; j<w; j++){
			if(!chk[i][j]){
				puts("NO");
				return;
			}
		}
	}

	puts("YES");
	return;
}

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	scanf("%d", &t);
	
	for(cc=1; cc<=t; cc++){
		printf("Case #%d: ", cc);

		input();
		solve();
	}

	return 0;
}