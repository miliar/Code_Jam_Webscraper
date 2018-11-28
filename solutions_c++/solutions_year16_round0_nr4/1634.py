#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
using namespace std;

int main () {
  FILE *filein;
  FILE *fileout;
  filein = fopen ("D_in.txt", "r");
  fileout = fopen ("D_out.txt", "w");
  int T, K, C, S;
  fscanf(filein, "%d", &T);
  for (int i = 0; i < T; i++){
    fscanf(filein, "%d %d %d", &K, &C, &S);
    if (K == S){
        fprintf(fileout, "%s%d%s", "Case #", i + 1, ":");
        for (int j = 0; j < K; j++){
            fprintf(fileout, " %d", j + 1);
        }
        fprintf(fileout, "\n");
    }
  }
  return 0;
}


