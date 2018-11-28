#include <bits/stdc++.h>
using namespace std;

int t, n;
int v[10], c;
int ans;

int main() {
  scanf("%d", &t);
  for (int tt = 1; tt<=t; tt++) {
    memset(v,0,sizeof(v));
    c = 0;
    printf("Case #%d: ",tt);
    scanf("%d", &n);
    if (n==0) {
      printf("INSOMNIA\n");
      continue;
    }
    for(int i = 1; c<10; i++) {
      int aux = i*n;
      while(aux) {
        if (!v[aux%10]) v[aux%10]=1, c++, ans = i*n;
        aux/=10;
      }
    }
    printf("%d\n", ans);
  }
}
