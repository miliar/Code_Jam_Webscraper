#include <cstdio>

int T, N;
char gen[3][15][5005];
int ct[3][15][3];

void re(int x, int cur, int lvl){
	if(cur == lvl + 1)return;

	int step = (1 << (cur - 1));

	for(int i = 0; i < (1 << lvl); i += 2*step){	
		int j = i;
		while(gen[x][lvl][j] == gen[x][lvl][j + step])j++;

		if(gen[x][lvl][j] > gen[x][lvl][j + step]){
			for(j = i; j < i + step; j++){
				//if(lvl == 2)printf("sdkfaksdjnf\n");
				char temp = gen[x][lvl][j];
				gen[x][lvl][j] = gen[x][lvl][j + step];
				gen[x][lvl][j + step] = temp;
			}
		}
	}
//printf("...%d %d %d\n", x, cur, lvl);
	re(x, cur + 1, lvl);
}

int main(){

	gen[0][0][0] = 'P'; gen[1][0][0] = 'R', gen[2][0][0] = 'S';
	ct[0][0][0] = 1; ct[1][0][1] = 1; ct[2][0][2] = 1;

	for(int i = 0; i < 3; i++){
		for(int j = 0; j < 12; j++){
			for(int k = 0; k < (1 << j); k++){
				if(gen[i][j][k] == 'P'){
					gen[i][j + 1][2*k] = 'P';
					ct[i][j + 1][0]++;
					/////////////////////////////////////
					gen[i][j + 1][2*k + 1] = 'R';
					ct[i][j + 1][1]++;
				} else if(gen[i][j][k] == 'R'){
					gen[i][j + 1][2*k] = 'R';
					ct[i][j + 1][1]++;
					/////////////////////////////////////
					gen[i][j + 1][2*k + 1] = 'S';
					ct[i][j + 1][2]++;
				} else {
					gen[i][j + 1][2*k] = 'P';
					ct[i][j + 1][0]++;
					/////////////////////////////////////
					gen[i][j + 1][2*k + 1] = 'S';
					ct[i][j + 1][2]++;
				}
			}

			re(i, 1, j + 1);
		}
	}

	scanf("%d", &T);
	for(int tt = 1; tt <= T; tt++){
		scanf("%d", &N);
		int a, b, c;
		scanf("%d %d %d", &b, &a, &c);

		printf("Case #%d: ", tt);

		if(ct[0][N][0] == a && ct[0][N][1] == b && ct[0][N][2] == c){
			for(int i = 0; i < (1 << N); i++)
				printf("%c", gen[0][N][i]);
			printf("\n");
		} else if(ct[1][N][0] == a && ct[1][N][1] == b && ct[1][N][2] == c){
			for(int i = 0; i < (1 << N); i++)
				printf("%c", gen[1][N][i]);
			printf("\n");
		} else if(ct[2][N][0] == a && ct[2][N][1] == b && ct[2][N][2] == c){
			for(int i = 0; i < (1 << N); i++)
				printf("%c", gen[2][N][i]);
			printf("\n");
		} else 
			printf("IMPOSSIBLE\n");
	}
}