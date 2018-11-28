#include <bits/stdc++.h>
using namespace std;

int T;
bool vis[10];

int main() {
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);
  scanf("%d", &T);
  for(int cs = 1; cs <= T; cs++) {
    memset(vis, 0, sizeof vis);
    long long n;
    scanf("%I64d", &n);
    printf("Case #%d: ", cs);
    if(n == 0) {
      puts("INSOMNIA");
      continue;
    }
    long long tmp = n;
    for(int i = 0;; i++) {
      long long t = tmp;
      while(t) {
        vis[t % 10] = true;
        t /= 10;
      }
      bool flag = true;
      for(int i=0;i<10;i++) if(vis[i] == false) flag = false;
      if(flag == true) {
        printf("%I64d\n", tmp);
        break;
      }
      tmp += n;
    }
  }
  return 0;
}
