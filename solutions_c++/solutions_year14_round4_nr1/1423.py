#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

int T,N,K;
int v[10100];
int resp,fim,ini;

int main(){
  scanf(" %d", &T);
  for(int u=1; u<=T; u++){
    scanf(" %d %d", &N, &K);
    for(int i=0; i<N; i++){
      scanf(" %d", &v[i]);
    }
    sort(v,v+N);
    resp = 0;
    fim = N-1;
    ini = 0;
    while(ini <= fim){
      if(v[fim]+v[ini]<=K){
        ini++;
        fim--;
      }
      else{
        fim--;
      }
      resp++;
    }
    printf("Case #%d: %d\n",u,resp);
  }
  return 0;
}
