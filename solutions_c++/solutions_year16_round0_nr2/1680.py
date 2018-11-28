#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

int main () {
  FILE *filein;
  FILE *fileout;
  filein = fopen ("B_in.txt", "r");
  fileout = fopen ("B_out.txt", "w");
  int T, groups;
  char *S = (char *)malloc(sizeof(char) * 101);
  char cur;
  fscanf(filein, "%d", &T);
  for (int i = 0; i < T; i++){
    groups = 0;
    fscanf(filein, "%s\n", S);
    //fprintf (stdout, "%s\n", S);
    int j = 0;
    cur = S[j];
    int new_group = 1;
    while (cur != '\0'){
        if (cur == '+'){
            new_group = 1;
        }else{
            if (new_group){
                groups++;
                new_group = 0;
            }
        }
        j++;
        cur = S[j];
    }
    int ans;
    if (groups == 0){
        ans = 0;
    }else if(S[0] == '+'){
        ans = 2 * groups;
    }else if (S[0] == '-'){
        ans = 2 * groups - 1;
    }else{
        ans = 0;
    }
        fprintf(fileout, "%s%d%s%d\n", "Case #", i + 1, ": ", ans);
    }
  return 0;
}
