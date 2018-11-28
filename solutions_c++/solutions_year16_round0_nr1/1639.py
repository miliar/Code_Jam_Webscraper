#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

int main () {
  FILE *filein;
  FILE *fileout;
  filein = fopen ("A_in.txt", "r");
  fileout = fopen ("A_out.txt", "w");
  int T, N, digitCount, curM;
  fscanf(filein, "%d", &T);
  int digits[10];

    for (int i = 0; i < T; i++){
      fscanf(filein, "%d", &N);
      digitCount = 0;
      curM = 1;
      for (int j = 0; j < 10; j++){
        digits[j] = 0;
      }
      if (N == 0){
        digitCount = 10;
      }
      while (digitCount < 10){
        int curN = curM * N;
        while (curN > 0){
            int d = curN % 10;
            if (!digits[d]){
                digits[d] = 1;
                digitCount++;
            }
            curN /= 10;
        }
        curM++;
      }
      if (N * (curM - 1) == 0){
        fprintf(fileout, "%s%d%s%s\n", "Case #", i + 1, ": ", "INSOMNIA");
      }
      else{
            fprintf(fileout, "%s%d%s%d\n", "Case #", i + 1, ": ", N * (curM - 1));
      }
    }
  return 0;
}
