#include <bits/stdc++.h>
using namespace std;
int main() {
  int T;
  scanf("%d\n",&T);
  for (int ts=1;ts<=T;ts++) {
    int k,c,s;
    scanf("%d %d %d\n",&k,&c,&s);
    printf("Case #%d:",ts);

    if (c*s < k) {
      printf(" IMPOSSIBLE\n",ts);
      continue;
    }

    int tt = (k + c - 1) / c;
    for (int i=0;i<tt;i++) {
      long long ans = 0;
      for (int j=i*c;j<min((i+1)*c,k);j++) {
        ans = ans*k + j;
      }
      printf(" %I64d",ans+1);
    }
    printf("\n");
  }
}
