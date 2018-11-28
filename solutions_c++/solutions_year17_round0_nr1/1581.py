#include <bits/stdc++.h>
using namespace std;

const int N = 1e3+5;
int T, t, n, k, ans;
char s[N];

void slv() {
    scanf("%s%d", s, &k);
    n = strlen(s);
    ans = 0;

    for(int i=0; i<=n-k; ++i) if (s[i] == '-') {
      ans++;
      for(int j=0; j<k; ++j)
        s[i+j] = (s[i+j] == '-' ? '+' : '-');
    }

    for(int i=0; i<n; ++i) if (s[i] == '-') {
      printf("Case #%d: IMPOSSIBLE\n", t);
      return;
    }

    printf("Case #%d: %d\n", t, ans);
}

int main() {
  scanf("%d", &T);
  while(t++ < T) slv();
  return 0;
}
