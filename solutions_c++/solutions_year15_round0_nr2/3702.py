#include <bits/stdc++.h>
using namespace std;

#define INF 2000000000
#define MOD 1000000007

typedef long long LL;
typedef pair<int, int> ii;

const int N = 1005; 
int d, p[N];

inline int get(int n, int maxh) {  // ciel(n / maxh) - 1
  int cl = (n + maxh - 1) / maxh;
  return cl - 1;
}

int main() { 
  int T, qq;
  for(cin >> T, qq = 1; qq <= T; ++qq) {
    printf("Case #%d: ", qq);
    cin >> d;
    for(int i = 0; i < d; ++i) {
      cin >> p[i];
    }
    int ans = INF, t;
    for(int maxh = 1; maxh <= 1000; ++maxh) {
      t = maxh;
      for(int i = 0; i < d; ++i) {
        t += get(p[i], maxh);         // number of total splits to make each element <= maxh
      }
      ans = min(ans, t);
    }
    cout << ans << "\n";
  }
  
  return 0;
}

