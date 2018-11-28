#include <bits/stdc++.h>
using namespace std;

int main(){
  FILE *f = fopen("B-large.in", "r");
  FILE *g = fopen("out.txt", "w");
  int n; fscanf(f, "%d", &n);

  for(int u = 1; u<=n; u++){
    char x [105];
    fscanf(f, "%s", x);
    char side = '+';
    int i = strlen(x)-1;
    int flips = 0;
    while(i >= 0){
      if(x[i] != side){
        flips++;
        side = x[i];
      }
      i--;
    }
    fprintf(g, "Case #%d: %d\n", u, flips);
  }
}
