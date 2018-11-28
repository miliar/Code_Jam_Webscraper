#include <stdio.h>
#include <math.h>
#include <string.h>
#include <algorithm>
using namespace std;

int main(void) {
  int t,n,i,j,l;
  char init[101];
  int sol[101][2];

  FILE *in = fopen("input.txt","r");
  FILE *out = fopen("output.txt","w");

  fscanf(in,"%d",&t);

  for (int p=0; p<t; p++) {
    fscanf(in,"%s",init);
    l = strlen(init);
    if (init[0] == '-') {
      sol[0][1] = 0;
      sol[0][0] = 1;
    }
    else {
      sol[0][1] = 1;
      sol[0][0] = 0;
    }
    for (i=1; i<l; i++){
      if (init[i] == '-') {
        sol[i][1] = min(sol[i-1][1], sol[i-1][0] + 2);
        sol[i][0] = min(sol[i-1][1]+1, sol[i-1][0] + 3);
      }
      else {
        sol[i][0] = min(sol[i-1][0], sol[i-1][1] + 2);
        sol[i][1] = min(sol[i-1][0]+1, sol[i-1][1] + 3);
      }
    }
    fprintf(out,"Case #%d: %d\n", p+1, sol[l-1][0]);
  }
}
