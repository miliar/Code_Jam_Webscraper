#include<stdio.h>

char A[4][5];
int M[4][4];
int N;

int check() {
  int i, j, i2;
  for(i=0;i<N;i++) {
    int cnt = 0, tot = 0;
    for(j=0;j<N;j++) cnt+=M[i][j];
    for(i2 = 0;i2<N;i2++) {
      int cnt2 = 0;
      for(j=0;j<N;j++) cnt2+=M[i][j]*M[i2][j];
      if(cnt2 != 0 && cnt2 != cnt) return 0;
      if(cnt2 == cnt) tot++;
    }
    if(tot != cnt) return 0;
  }
  return 1;
}

void solve(int t) {
  int i, j, m, best = 1000;
  scanf("%d",&N);
  for(i=0;i<N;i++) scanf("%s",A[i]);
  
  for(m=0;m<(1<<N*N);m++) {
    int cnt = 0;
    for(i=0;i<N;i++) {
      for(j=0;j<N;j++) {
        M[i][j] = (m>>(i*N+j))&1;
        if(M[i][j] && A[i][j] == '0') cnt++;
        if(!M[i][j] && A[i][j] == '1') cnt += N*N+1;
      }
    }
    if(cnt > N*N) continue;

    if( check() ) {
      if(cnt < best) best = cnt;
    }
  }
  
  printf("Case #%d: %d\n",t,best);
}

int main() {
  int t,T;
  //freopen("/Users/sushi/Downloads/C-small-attempt1.in","r",stdin);
  scanf("%d",&T);
  for(t=1;t<=T;t++) solve(t);
  return 0;
}
