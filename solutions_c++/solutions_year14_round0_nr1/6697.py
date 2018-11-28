// codejam.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
#include <stdlib.h>

int * getRow(FILE * file, int row, int * buf ){
	int discard;

	row--; //0 init

	for(int i = 1; i <= 16; i++){
		if( i > row * 4 && i <= row * 4 + 4 )
			fscanf(file, " %d ", &buf[i - (row * 4 + 1)]);
		else
			fscanf(file, " %d ", &discard);
	}

	return buf;
}

int main(int argc, char * argv[])
{
	FILE * file;
	fopen_s(&file, "input.in", "r");

	if (file != nullptr){
	  int cases; fscanf(file, " %d ", &cases);

	  int * first = (int *) calloc(4, sizeof(int));
	  int * second = (int *) calloc(4, sizeof(int));


	  for(int i = 0; i < cases; i++){
		  int row1; fscanf(file, " %d ", &row1);
		  first = getRow(file, row1, first);
		  int row2; fscanf(file, " %d ", &row2);
		  second = getRow(file, row2, second);
		  
		  char result[40];
		  int times = 0, match = 0;

		  for(int j = 0; j < 4; j++){
			  for(int k = 0; k < 4; k++){
				  if( first[j] == second[k]){
					  times++;
					  match = first[j];
				  }
			  }
		  }

		  if(times == 1)
			  sprintf(result, "%d", match);
		  else if(times)
			  sprintf(result, "Bad magician!");
		  else
			  sprintf(result, "Volunteer cheated!");

		  printf("Case #%d: %s\n", i+1, result);
	  }

      fclose(file);
	  free(first);
	  free(second);
    }

	return 0;
}

