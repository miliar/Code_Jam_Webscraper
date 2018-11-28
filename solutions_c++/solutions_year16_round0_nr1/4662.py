#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;

int main(void)
{
  FILE *in = fopen("input.txt", "r");
  FILE *out = fopen("output.txt", "w");

  int n,i,j,k,tmp;
  bool used[10];
  int count;

  fscanf(in,"%d",&n);

  for (int t=0; t<n; t++) {
    fscanf(in,"%d",&j);
    count = 0;
    for (i=0; i<10; i++)
      used[i] = false;
    if (j==0) {
      fprintf(out,"Case #%d: INSOMNIA\n",t+1);
      continue;
    }
    k=j;
    while (1) {
      tmp = k;
      while (tmp != 0){
        if (!used[tmp%10]){
          used[tmp%10] = true;
          count++;
        }
        tmp /= 10;
      }
      if (count == 10)
        break;
      k=k+j;
    }
    fprintf(out,"Case #%d: %d\n",t+1,k);
  }

  return 0;
}
