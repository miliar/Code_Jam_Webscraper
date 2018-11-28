// codejam.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
#include <tchar.h>
#include <stdlib.h>

int _tmain(int argc, _TCHAR* argv[])
{
	FILE * file;
	fopen_s(&file, "input.in", "r");

	if (file != nullptr){
	  int cases; fscanf(file, " %d ", &cases);


	  for(int i = 0; i < cases; i++){
		  printf("Case #%d: ", i+1);

		  int a; fscanf(file, " %d ", &a);
		  int b; fscanf(file, " %d ", &b);

		  int k; fscanf(file, " %d ", &k);

		  int count = 0;
		  for(int i = 0; i < a; i++){
			  for(int j = 0; j < b; j++){
				  if ( (i & j) < k ) count++;
			  }
		  }

		  printf("%d\n", count);

	  }

      fclose(file);
	  fprintf(stderr, "done.\n");
    }

	return 0;
}

