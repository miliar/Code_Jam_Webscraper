#include<stdio.h>
#include<algorithm>

double A[10000], B[10000];

int main() {
  int t, T;
  int i, j, c1, c2, N;

  scanf("%d",&T);
  for(t=1;t<=T;t++) {
    scanf("%d",&N);
    for(i=0;i<N;i++) scanf("%lf",A+i);
    for(i=0;i<N;i++) scanf("%lf",B+i);
    std::sort(A,A+N);
    std::sort(B,B+N);
    c1 = c2 = 0;
    j = N-1;
    for(i=N-1;i>=0;i--) {
      if(A[j] > B[i]) {
        c1++; j--;
      }
    }
    j = N-1;
    for(i=N-1;i>=0;i--) {
      if(B[j] > A[i]) {
        c2++; j--;
      }
    }
    printf("Case #%d: %d %d\n",t,c1,N-c2);
  }
  return 0;
}
