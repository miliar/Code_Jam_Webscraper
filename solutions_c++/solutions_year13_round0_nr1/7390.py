#include<stdio.h>
#define rep(i, n) for(int i = 0 ; i<n ; i++)

char ttt[4][4];

void inline le_ttt() {
    rep(i,4)
		rep(j, 4)
			scanf(" %c", &ttt[i][j]);
}

int check_ttt(int * blank) {
	rep(i, 4) {
		int colX = 0, colO = 0;
		int linX = 0, linO = 0;
        int diagPX = 0, diagPO = 0;
        int diagSX = 0, diagSO = 0;
		
		rep(j, 4) {
			if(ttt[i][j] == '.') (*blank)++;
			
            //linha
			if(ttt[i][j] == 'X') linX++;
			if(ttt[i][j] == 'O') linO++;
			if(ttt[i][j] == 'T') linO++, linX++;
			
            //coluna
			if(ttt[j][i] == 'X') colX++;
			if(ttt[j][i] == 'O') colO++;
			if(ttt[j][i] == 'T') colO++, colX++;
            
            //diagonal principal
            if(ttt[j][j] == 'X') diagPX++;
    		if(ttt[j][j] == 'O') diagPO++;
			if(ttt[j][j] == 'T') diagPO++, diagPX++;
            
            //diagonal secundária
            if(ttt[3-j][j] == 'X') diagSX++;
        	if(ttt[3-j][j] == 'O') diagSO++;
			if(ttt[3-j][j] == 'T') diagSO++, diagSX++;
		}
		
		if(linX == 4 || colX == 4 || diagPX == 4 || diagSX == 4) return 1;
		if(linO == 4 || colO == 4 || diagPO == 4 || diagSO == 4) return 2;
	}
	
	return 0;
}

int main () {
	int n;
	
	scanf("%d", &n);
	for(int c = 1 ; c<=n ; c++) {
		le_ttt();
		
		printf("Case #%d: ", c);
		
		int blank = 0;
		int st = check_ttt(&blank);

		if(st == 1)
			printf("X won\n");
		else if(st == 2)
			printf("O won\n");
		else if(blank)
			printf("Game has not completed\n");
		else
			printf("Draw\n");
	}
	
	return 0;
}