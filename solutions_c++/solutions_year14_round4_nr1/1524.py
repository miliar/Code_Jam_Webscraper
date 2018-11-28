#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;
typedef pair<int,int> ii;

int main() {
  int t;
  scanf(" %d", &t);
  for(int i = 0; i < t; ++i) {
    int n, x;
    scanf(" %d %d", &n, &x);
    int s[10001];
    for(int j = 0; j < n; ++j) {
      scanf(" %d", &s[j]);
    }
    bool used[10001] = {0};
    int ans = 0;
    for(int a = 0; a < n; ++a) {
      if(used[a]) continue;
      int best = -1;
      for(int b = a + 1; b < n; ++b) {
	if(used[b]) continue;
	if(s[a] + s[b] <= x && (best == -1 || s[b] > s[best])) {
	  best = b;
	}
      }
      if(best != -1) {
	used[best] = true;
      }
      ++ans;
    }
    printf("Case #%d: %d\n", i + 1, ans);
  }
  return 0;
}
