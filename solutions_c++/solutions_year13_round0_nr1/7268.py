#include <conio.h>
#include <stdio.h>
#include <stdlib.h>


FILE * saida;
FILE * input;
bool XWinner = false;
bool OWinner = false;
bool notCompleted = false;

/*
char map[4][4] = {
	{'X','X','X','T'},
	{'.','.','.','.'},
	{'O','O','.','.'},
	{'.','.','.','.'}
};
*/

char ** map;

void verify(char ** map,char target){
	int lines[4] = {0,0,0,0};
	int columms[4] = {0,0,0,0};
	int diagonals[4] = {0,0,0,0};
	
	for(int i = 0; i<4 ; i++){
		for(int j = 0; j<4 ; j++){
			char read = map[i][j];
			if(read == '.'){notCompleted = true;}
			if(read == target || read == 'T'){
				if(i == j){diagonals[0]++;}
				if(i+j == 3){diagonals[1]++;}
				lines[i]++;
				columms[j]++;
			}
		}
	}
	for(int i = 0; i<4 ; i++){
		if(lines[i]==4 || columms[i]==4 || diagonals[i]==4){
			if(target == 'X') XWinner = true;
			else OWinner = true;
		}
	}
}

void readMap(){
	char line[10];
	for(int i = 0; i<4 ; i++){
		if(fgets(line, 10, input) != NULL){
			map[i] = (char*) malloc(4*sizeof(char));
			map[i][0] = line[0];
			map[i][1] = line[1];
			map[i][2] = line[2];
			map[i][3] = line[3];	
		}
	}
	fgets(line, 10, input);
}

void printMap(){
	for(int i = 0; i<4 ; i++){
		printf("%c %c %c %c\n",map[i][0],map[i][1],map[i][2],map[i][3]);
	}
	printf("\n");
}

int main(){
	int casenum=1;
	int numgames = 0;
	char line[100];
	saida = fopen("saida.txt","w");
	input = fopen("A-large.in","r");
	map = (char**) malloc(4*sizeof(char*));
	numgames = atoi(fgets(line, 80, input));
	while(casenum <= numgames){
		readMap();
		printMap();
		verify(map,'X');
		verify(map,'O');
		if(XWinner){
			fprintf(saida,"Case #%d: X won\n",casenum);
		}else if(OWinner){
			fprintf(saida,"Case #%d: O won\n",casenum);
		}else if(notCompleted){
			fprintf(saida,"Case #%d: Game has not completed\n",casenum);
		}else{
			fprintf(saida,"Case #%d: Draw\n",casenum);	
		}
		XWinner = false;
		OWinner = false;
		notCompleted = false;
		casenum++;
	}
	getch();
	fclose(saida);
	return 0;	
}
