#include <cstdio>
char T[6][6];

int hor(int x){
	if(T[x][0]!='.' && T[x][0] == T[x][1] && T[x][1] == T[x][2] && T[x][2] == T[x][3]) return T[x][0];
	if(T[x][1]!='.' && T[x][0] == 'T' && T[x][1] == T[x][2] && T[x][2] == T[x][3]) return T[x][3];
	if(T[x][0]!='.' && T[x][0] == T[x][1] && T[x][1] == T[x][2] && T[x][3]=='T') return T[x][0];

	return 0;
}

int ver(int y){
	if(T[0][y]!='.' && T[0][y] == T[1][y] && T[1][y] == T[2][y] && T[2][y] == T[3][y]) return T[0][y];
	if(T[1][y]!='.' && T[0][y] == 'T' && T[1][y] == T[2][y] && T[2][y] == T[3][y]) return T[3][y];
	if(T[0][y]!='.' && T[0][y] == T[1][y] && T[1][y] == T[2][y] && T[3][y]=='T') return T[0][y];

	return 0;
}

int diag1(){	
	if(T[0][0]!='.' && T[0][0] == T[1][1] && T[1][1] == T[2][2] && T[2][2] == T[3][3]) return T[0][0];
	if(T[1][1]!='.' && T[0][0] == 'T' && T[1][1] == T[2][2] && T[2][2] == T[3][3]) return T[3][3];
	if(T[0][0]!='.' && T[0][0] == T[1][1] && T[1][1] == T[2][2] && T[3][3]=='T') return T[0][0];

	return 0;
}

int diag2(){	
	if(T[0][3]!='.' && T[0][3] == T[1][2] && T[1][2] == T[2][1] && T[2][1] == T[3][0]) return T[0][3];
	if(T[1][2]!='.' && T[0][3] == 'T' && T[1][2] == T[2][1] && T[2][1] == T[3][0]) return T[3][0];
	if(T[0][3]!='.' && T[0][3] == T[1][2] && T[1][2] == T[2][1] && T[3][0]=='T') return T[1][2];

	return 0;
}

int gana(){
	int i, j;
	int res;
	for(i = 0; i < 4; i++){
		if(res = hor(i)){
			if(res == 'X') return 1;
			if(res == 'O') return 2;
		}
		if(res = ver(i)){
			if(res == 'X') return 1;
			if(res == 'O') return 2;
		}
	}
	
	if(res = diag1()) {
			if(res == 'X') return 1;
			if(res == 'O') return 2;
	}

	if(res = diag2()) {
			if(res == 'X') return 1;
			if(res == 'O') return 2;
	}

	for(i = 0; i < 4; i++)
		for(j = 0; j < 4; j++)
			if(T[i][j] == '.')return 4;

	return 3;
}

int main(){
	int n;
	int i, j, k;
	int res;

	scanf("%d", &n);
	getchar();
	for(i = 1; i <= n; i++){
		for(j = 0; j < 4; j++){
			scanf("%s", T[j]);
		}
		
		res = gana();
		printf("Case #%d: ", i);
		switch(res) {
			case 1 : 
				printf("X won\n");
				break;
			case 2 :
				printf("O won\n");
				break;
			case 3 : 
				printf("Draw\n");
				break;
			case 4 :
				printf("Game has not completed\n");
				break;
		}
	}

return 0;}
