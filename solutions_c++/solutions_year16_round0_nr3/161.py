#include <bits/stdc++.h>
using namespace std;
const int N = 32;
const int J = 500;
int main() {
  printf("Case #1:\n");
  for (int i=0;i<J;i++) {
    int tmp = i;
    int ans[N];
      for (int j=0;j<N;j++) {
        if (tmp % 2 == 0) ans[j] = 0;
        else ans[j] = 1;
        tmp /= 2;
      }
    printf("1");
    for (int j=0;j<(N-2)/2;j++) printf("%d%d",ans[j],ans[j]);
    printf("1 3 4 5 6 7 8 9 10 11\n");
  }
  return 0;
}
