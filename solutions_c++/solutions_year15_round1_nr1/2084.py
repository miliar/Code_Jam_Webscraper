#include <bits/stdc++.h>

#define llong long long

using namespace std;

typedef vector<int> big;

const int MAXN = (int) 2e6 + 7;
const int INF = (int) 1e9 + 7;

int n, m;
int a[MAXN];

int main() {  
  #ifdef LOCAL
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);
  #endif

  int T;
  scanf("%d", &T);
  for (int cases = 1; cases <= T; cases++) {
    scanf("%d", &n);
    for (int i = 1; i <= n; i++) {
      scanf("%d", &a[i]);  
    }
    int ans1 = 0, ans2 = 0;
    int eat = 0;
    for (int i = 1; i < n; i++) {
      if (a[i + 1] < a[i]) {
        ans1 += a[i] - a[i + 1];
        eat = max(eat, (a[i] - a[i + 1]));
      }
    }
    for (int i = 1; i < n; i++)
      ans2 += min(a[i], eat);
          
    printf("Case #%d: %d %d\n", cases, ans1, ans2);
  }
   
      
  return 0;
}
