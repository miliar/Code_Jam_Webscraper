#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
using namespace std;

int main () {
  FILE *filein;
  FILE *fileout;
  filein = fopen ("C_in.txt", "r");
  fileout = fopen ("C_out.txt", "w");
  int T;
  fscanf(filein, "%d", &T);
char *pattern = (char *) malloc (sizeof(char) * 33);
char *divisor = (char *) malloc (sizeof(char) * 17);
  for (int i = 0; i < T; i++){
    fprintf(fileout, "%s\n", "Case #1:");
    for(int j = 0; j < 500; j++){
        pattern[32] = '\0';
        pattern[0] = '1';
        pattern[1] = '1';
        pattern[30] = '1';
        pattern[31] = '1';
        int cur = j;
        for (int k = 1; k < 15; k++){
            pattern[2*k] = (!(cur % 2 == 0))?'1':'0';
            pattern[2*k + 1] = pattern[2*k];
            cur /= 2;
        }
        divisor[16] = '\0';
        divisor[0] = '1';
        divisor[15] = '1';
        for (int k = 1; k < 15; k++){
            divisor[k] = pattern[k * 2];
        }
        fprintf(fileout, "%s %d %d %d %d %d %d %d %d %d\n", pattern, 3, 4, 5, 6, 7, 8, 9, 10, 11);
    }
}
  return 0;
}

