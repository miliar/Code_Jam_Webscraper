#include <bits/stdc++.h>
using namespace std;
int main(){
  FILE *f = fopen("A-large.in", "r");
  FILE *g = fopen("out.txt", "w");
  int n; fscanf(f, "%d", &n);
  for(int u = 1; u<=n; u++){
    fprintf(g, "Case #%d: ", u);
    int in; fscanf(f, "%d", &in);
    if(in == 0){
      fprintf(g, "INSOMNIA\n");
      continue;
    }
    bool seen [10] = {0};
    int in_cpy = in;
    while(true){
      int i = in;
      while(i > 0){
        seen[i % 10] = 1;
        i /= 10;
      }
      in += in_cpy;
      bool done = 1;
      for(int i = 0; i<10; i++){
        if(!seen[i])
          done = 0;
      }
      if(done){
        fprintf(g, "%d\n", in-in_cpy);
        break;
      }
    }
  }
  
}
