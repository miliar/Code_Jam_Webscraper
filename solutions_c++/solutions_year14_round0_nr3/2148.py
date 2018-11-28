#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string.h>

using namespace std;

int movx[] = {0, 0, 1,-1, 1, 1,-1,-1};
int movy[] = {1,-1, 0, 0, 1,-1, 1, -1};

//bool grid[5][5];
bool grid[10][10];
int marcX[9];
int marcY[9];
int m, R, C, poss;

int compute(int x, int y){
	int vecinos = 0;
	for(int i = 0; i < 8; i++){
		int x_prox = x + movx[i];
		int y_prox = y + movy[i];
		if( x_prox >= 0 && x_prox < R && y_prox >= 0 && y_prox < C)
			if(!grid[x_prox][y_prox])
				vecinos++;					
	}
	if(vecinos + poss + m <= R * C && vecinos != 0){
		int ii = 0;
		poss += vecinos;	
		for(int i = 0; i < 8; i++){
			int x_prox = x + movx[i];
			int y_prox = y + movy[i];
			if( x_prox >= 0 && x_prox < R && y_prox >= 0 && y_prox < C)
				if(!grid[x_prox][y_prox]){
					marcX[ii] = x_prox;
					marcY[ii] = y_prox;
					grid[x_prox][y_prox] = true;
					ii++;		
				}
		}
		for(int i = 0; i < vecinos; i++)
			compute(marcX[i], marcY[i]);
	}
}

int main(){
	ifstream input("C-small-attempt1.in");
	FILE *out;
	out = fopen("out", "w");
	int nCase = 0, i, j;
	input >> nCase;
	for(int t = 1; t <= nCase; t++){
		input >> R;
		input >> C;
		input >> m;
		bool flag = false;	
		for(i = 0; i < R; i++){
			for(j = 0; j < C; j++){
				memset(grid, false, sizeof(grid));
				poss = 1;
				grid[i][j] = true;
				compute(i,j);
				if( poss + m == R * C){
					flag = true;
					break;
				}
			}
			if(flag)
				break;
		}
		fprintf(out, "Case #%d:\n", t);
		if(flag){
			for(int ii = 0; ii < R; ii++){	
				for(int jj = 0; jj < C; jj++){
					if(ii == i && jj == j)
						fprintf(out,"c");
					else if( grid[ii][jj])
						fprintf(out,".");
					else 
						fprintf(out,"*");
				}		
				fprintf(out,"\n");
			}
		}else{	
			fprintf(out, "Impossible\n");
		}	
		if(input.eof())
			break;	
	} 		
	return 0;
}
