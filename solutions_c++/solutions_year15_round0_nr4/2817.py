#include <cstdio>
#include <cstring>

bool richardWin[5][5][5];

void init(){
	memset(richardWin,false,sizeof(richardWin));
	for(int X=1;X<=4;X++){
		for(int R=1;R<=4;R++){
			for(int C=1;C<=4;C++){
				if ((X > R) && (X > C)) {
					richardWin[X][R][C] = true;
				}
				if ((R*C) % X != 0 ) {
					richardWin[X][R][C] = true;
				}
				if (X==1) {
					richardWin[X][R][C] = false;
				}
			}	
		}
	}
	
	richardWin[2][1][2] = false;
	richardWin[2][1][4] = false;
	richardWin[2][2][1] = false;
	richardWin[2][2][2] = false;
	richardWin[2][2][3] = false;
	richardWin[2][2][4] = false;
	richardWin[2][3][2] = false;
	richardWin[2][3][4] = false;
	richardWin[2][4][1] = false;
	richardWin[2][4][2] = false;
	richardWin[2][4][3] = false;
	richardWin[2][4][4] = false;
	richardWin[3][1][3] = true;
	richardWin[3][2][3] = false;
	richardWin[3][3][1] = true;
	richardWin[3][3][2] = false;
	richardWin[3][3][3] = false;
	richardWin[3][3][4] = false;
	richardWin[3][4][3] = false;
	richardWin[4][1][4] = true;
	richardWin[4][2][4] = true;
	richardWin[4][3][4] = false;
	richardWin[4][4][1] = true;
	richardWin[4][4][2] = true;
	richardWin[4][4][3] = false;
	richardWin[4][4][4] = false;
}

int main() {
	init();
	int tc; scanf("%d",&tc);
	for (int d=1 ; d<=tc ;d++){
		int X,R,C; scanf("%d %d %d",&X,&R,&C);
		printf("Case #%d: ",d);
		if(richardWin[X][R][C]) {
			printf("RICHARD\n");
		}
		else {
			printf("GABRIEL\n");
		}

	}
	return 0;
}