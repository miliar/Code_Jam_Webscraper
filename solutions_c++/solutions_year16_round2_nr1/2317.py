#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
#include <vector>
using namespace std;

int main () {
  FILE *filein;
  FILE *fileout;
  filein = fopen ("A_in.txt", "r");
  fileout = fopen ("A_out.txt", "w");
  int T;
  fscanf(filein, "%d", &T);
  for (int i = 0; i < T; i++){
    int *digits = (int *) malloc(sizeof(int) * 10);
    int *asc = (int *) malloc(sizeof(int) * 128);
    char *word = (char *) malloc(sizeof(char) * 2001);
    for(int j = 0; j < 10; j++){
        digits[j] = 0;
    }
    for(int j = 0; j < 128; j++){
        asc[j] = 0;
    }

    fscanf(filein, "%s", word);
    //fprintf(stdout, "%s\n", word);
    char cur = word[0];
    int j = 1;
    while (cur != '\0'){
        asc[cur] += 1;
        cur = word[j];
        j++;
    }

    int zero, one, two, three, four, five, six, seven, eight, nine;
    //zero
    zero = asc[90];
    digits[0] += zero;
    asc[69] -= zero;
    asc[90] -= zero;
    asc[82] -= zero;
    asc[79] -= zero;

    //six
    six = asc[88];
    digits[6] += six;
    asc[73] -= six;
    asc[83] -= six;
    asc[88] -= six;

    //two
    two = asc[87];
    digits[2] += two;
    asc[79] -= two;
    asc[84] -= two;
    asc[87] -= two;

    //eight
    eight = asc[71];
    digits[8] += eight;
    asc[69] -= eight;
    asc[71] -= eight;
    asc[72] -= eight;
    asc[73] -= eight;
    asc[84] -= eight;

    //three
    three = asc[84];
    digits[3] += three;
    asc[84] -= three;
    asc[72] -= three;
    asc[82] -= three;
    asc[69] -= three;
    asc[69] -= three;

    //four
    four = asc[82];
    digits[4] += four;
    asc[82] -= four;
    asc[70] -= four;
    asc[79] -= four;
    asc[85] -= four;

    //five
    five = asc[70];
    digits[5] += five;
    asc[70] -= five;
    asc[73] -= five;
    asc[86] -= five;
    asc[69] -= five;

    //seven
    seven = asc[86];
    digits[7] += seven;
    asc[86] -= seven;
    asc[83] -= seven;
    asc[78] -= seven;
    asc[69] -= 2*seven;

    //nine
    nine = asc[73];
    digits[9] += nine;
    asc[73] -= nine;
    asc[69] -= nine;
    asc[78] -= 2*nine;

    // one
    one = asc[78];
    digits[1] = one;
    fprintf(fileout, "%s%d%s", "Case #", i + 1, ": ");
    for(int j = 0; j < 10; j++){
        int d = digits[j];
        for (int k = 0; k < d; k++){
            fprintf(fileout, "%d", j);
        }
    }
    fprintf(fileout, "\n");

    free(digits);
    free(asc);
    free(word);
  }
  return 0;
}

