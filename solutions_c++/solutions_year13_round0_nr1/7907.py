#include <cstdio>
#include <cstdlib>
#include <vector>
#include <string.h>
#include <assert.h>

using namespace std;

int check(int startIdx, int endIdx, char * Data, char symbol) {
  //check row
  for (int j = 0; j < 4; j++) {
    if ((Data[startIdx*16  +j*4] == symbol || Data[startIdx*16  +j*4] == 'T') &&
	(Data[startIdx*16+1+j*4] == symbol || Data[startIdx*16+1+j*4] == 'T') &&
	(Data[startIdx*16+2+j*4] == symbol || Data[startIdx*16+2+j*4] == 'T') &&
	(Data[startIdx*16+3+j*4] == symbol || Data[startIdx*16+3+j*4] == 'T'))
      {return 1;}
  }
  //check col
  for (int j = 0; j < 4; j++) {
    if ((Data[startIdx*16    +j] == symbol || Data[startIdx*16    +j] == 'T') &&
        (Data[startIdx*16+1*4+j] == symbol || Data[startIdx*16+1*4+j] == 'T') &&
        (Data[startIdx*16+2*4+j] == symbol || Data[startIdx*16+2*4+j] == 'T') &&
        (Data[startIdx*16+3*4+j] == symbol || Data[startIdx*16+3*4+j] == 'T'))
      {return 1;}
  }
  //check two diagonals
  if ((Data[startIdx*16   ] == symbol || Data[startIdx*16   ] == 'T') &&
      (Data[startIdx*16+ 5] == symbol || Data[startIdx*16+ 5] == 'T') &&
      (Data[startIdx*16+10] == symbol || Data[startIdx*16+10] == 'T') &&
      (Data[startIdx*16+15] == symbol || Data[startIdx*16+15] == 'T'))
    {return 1;}
  if ((Data[startIdx*16+ 3] == symbol || Data[startIdx*16+ 3] == 'T') &&
      (Data[startIdx*16+ 6] == symbol || Data[startIdx*16+ 6] == 'T') &&
      (Data[startIdx*16+ 9] == symbol || Data[startIdx*16+ 9] == 'T') &&
      (Data[startIdx*16+12] == symbol || Data[startIdx*16+12] == 'T'))
    {return 1;}
  
  return 0;
}

int main (int argc, char ** argv) {
  FILE * pFile = fopen(argv[1], "r");
  FILE * oFile = fopen("p_A_output", "w");
  int T = 0;
  fscanf(pFile, "%d ", &T);
  char * Data = new char[T*16];
  printf("T = %d\n", T);

  int i = 0;
  while (i < T) {
    fscanf(pFile, "%c%c%c%c ", &Data[i*16], &Data[i*16+1], &Data[i*16+2], &Data[i*16+3]);
    fscanf(pFile, "%c%c%c%c ", &Data[i*16+4], &Data[i*16+5], &Data[i*16+6], &Data[i*16+7]);
    fscanf(pFile, "%c%c%c%c ", &Data[i*16+8], &Data[i*16+9], &Data[i*16+10], &Data[i*16+11]);
    fscanf(pFile, "%c%c%c%c ", &Data[i*16+12], &Data[i*16+13], &Data[i*16+14], &Data[i*16+15]);
    
    i++;
  }
  //printf("-------------------\n");
  //for (i = 0; i < T*16; i++)printf("%c", Data[i]);
  
  int count_empty = 0;
  int j;
  for (i = 0; i < T; i++) {
    count_empty = 0;
    for (j = i * 16; j < (i+1)*16; j++)
      if (Data[j] == '.') count_empty++;
    
    if (check(i, i+1, Data, 'X'))
      fprintf(oFile, "Case #%d: X won\n", i+1);
    else if (check(i, i+1, Data, 'O'))
      fprintf(oFile, "Case #%d: O won\n", i+1);
    else if (count_empty == 0)
      fprintf(oFile, "Case #%d: Draw\n", i+1);
    else
      fprintf(oFile, "Case #%d: Game has not completed\n", i+1);
  }    
  
  delete[] Data;
  
  return 0;
}
