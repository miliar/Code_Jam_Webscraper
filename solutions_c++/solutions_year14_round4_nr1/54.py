#include<bits/stdc++.h>
using namespace std;

#define REP(i,a,b) for(i=a;i<b;i++)
#define rep(i,n) REP(i,0,n)

int N, X, S[20000];
int hist[1000];

int main(){
  int i, j, k;
  int T, cnt = 0;
  int res;

  scanf("%d",&T);
  while(T--){
    fprintf(stderr,"rest %d\n",T);
    printf("Case #%d: ", ++cnt);

    scanf("%d%d",&N,&X);
    rep(i,N) scanf("%d",S+i);

    rep(i,X+1) hist[i] = 0;
    rep(i,N) hist[S[i]]++;
    res = 0;

    for(;;){
      for(i=X;i>=0;i--) if(hist[i]) break;
      if(i<0) break;
      res++;
      hist[i]--;
      for(j=X-i;j>=0;j--) if(hist[j]) break;
      if(j>=0) hist[j]--;
    }

    printf("%d\n",res);
  }

  return 0;
}
