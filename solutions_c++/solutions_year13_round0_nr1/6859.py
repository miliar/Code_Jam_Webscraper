#include <stdio.h>
#define MAX_R 5


int main()
{
	FILE* input = fopen("A-large.in", "r");

	FILE* output = fopen("Alarge.out", "w");
	int t,k;
	fscanf(input,"%d",&t);
	for(k=0 ; k<t ; k++){

		int i,j,x=0,o=0, cnt=0;
		char ttt[MAX_R][MAX_R]={0};
		for(i=0 ; i<4 ; i++){
			fscanf(input,"%s",ttt[i]);
		}
		int left_x=0, left_o=0, left_t=0;
		int right_x=0, right_o=0, right_t=0;
		for(i=0 ; i<4 ; i++){
			int col_x=0, col_o=0, col_t=0;
			int row_x=0, row_o=0, row_t=0;

			if(ttt[i][i] == 'X') left_x++;
			else if(ttt[i][i] == 'O') left_o++;
			else if(ttt[i][i] == 'T') left_t++;

			if(ttt[i][3-i] == 'X') right_x++;
			else if(ttt[i][3-i] == 'O') right_o++;
			else if(ttt[i][3-i] == 'T') right_t++;


			for(j=0 ; j<4 ; j++){
				if(ttt[i][j] == 'X') row_x++;
				else if(ttt[i][j] == 'O') row_o++;
				else if(ttt[i][j] == 'T') row_t++;

				if(ttt[j][i] == 'X') col_x++;
				else if(ttt[j][i] == 'O') col_o++;
				else if(ttt[j][i] == 'T') col_t++;

				if(ttt[i][j] != '.') cnt++;
			}
			if(((col_x + col_t) == 4) || (row_x + row_t) == 4){
				x++;
			}
			if((col_o + col_t == 4) || (row_o + row_t) == 4){
				o++;
			}

		}
		if(((left_x + left_t) == 4) || (right_x + right_t) == 4){
			x++;
		}
		if((left_o + left_t == 4) || (right_o + right_t) == 4){
			o++;
		}
		fprintf(output,"Case #%d: ",k+1);

		if(x>=1)
			fprintf(output,"X won\n");

		else if(o>=1)
			fprintf(output,"O won\n");

		else{
			if(cnt==16) fprintf(output,"Draw\n");
			else fprintf(output,"Game has not completed\n");
		}
	}
	return 0;
}