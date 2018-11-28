#include<stdio.h>

char A[1000000];

void solve(int t) {
  int k,cnt = 0,tot = 0;
  scanf("%s %d",A,&k);
  for(int i=0;;i++) {
    if(i>=k) cnt -= A[i-k];
    if(!A[i]) break;
    A[i] = (A[i]=='-')^(cnt%2);
    cnt += A[i]; tot += A[i];
  }
  if(!cnt) 
    printf("Case #%d: %d\n",t,tot);
  else
    printf("Case #%d: IMPOSSIBLE\n",t);
}

int main() {
  int t,T;
  scanf("%d",&T);
  for(t=1;t<=T;t++) solve(t);
  return 0;
}