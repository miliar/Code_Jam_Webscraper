#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

int N, v[1000];
double naomi[1000], ken[1000];

int war(){
  int i, j=0, cnt=0;

  for(i=0; i<N; i++){
    while(j < N && ken[j] < naomi[i]) j++;
    if(j>=N) cnt++;
    j++;
  }

  return cnt;
}

int deceitfulWar(){
  int M=N, jn=N-1, jk=N-1, cnt=0;

  while(M--){
    if(naomi[jn] > ken[jk]){
      jn--;
      jk--;
      cnt++;
    } else {
      jk--;      
    }
  }

  return cnt;
}

int main(){
  
  int t, T, i;

  scanf("%d", &T);
  for(t=1; t<=T; t++){
    scanf("%d", &N);
    for(i=0; i<N; i++) scanf("%lf", &naomi[i]);
    for(i=0; i<N; i++) scanf("%lf", &ken[i]);
    sort(naomi, naomi+N);
    sort(ken, ken+N);
    printf("Case #%d: %d %d\n", t, deceitfulWar(), war());
  }
  
  return 0;
}
