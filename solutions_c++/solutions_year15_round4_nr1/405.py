#include <bits/stdc++.h>
using namespace std;
template<typename T> inline void checkMin(T &a, T b) { if(b<a) a=b; }
template<typename T> inline void checkMax(T &a, T b) { if(a<b) a=b; }
#define X first
#define Y second
#define MP make_pair
#define PB push_back
#define SZ(c) int((c).size())
#define ALL(c) (c).begin(),(c).end()
#define REP(i,n) for(int i=0;i<int(n);++i)
typedef long long lint;
typedef vector<int> VI;
typedef pair<int, int> PII;

int r, c;
char mp[128][128];
int mark[128][128];

void solve() {
  scanf("%d%d", &r, &c);
  for (int i = 1; i <= r; ++i) {
    scanf("%s", &mp[i][1]);
  }

  fill(mark[0], mark[128], 0);

  int ans = 0;
  for (int i = 1; i <= r; ++i) {
    for (int j = 1; j <= c; ++j) {
      if (mp[i][j] == '.') {
        continue;
      }
      if (mp[i][j] == '<') {
        ++ans;
      }
      ++mark[i][j];
      break;
    }
    for (int j = c; j >= 1; --j) {
      if (mp[i][j] == '.') {
        continue;
      }
      if (mp[i][j] == '>') {
        ++ans;
      }
      ++mark[i][j];
      break;
    }
  }
  for (int j = 1; j <= c; ++j) {
    for (int i = 1; i <= r; ++i) {
      if (mp[i][j] == '.') {
        continue;
      }
      if (mp[i][j] == '^') {
        ++ans;
      }
      ++mark[i][j];
      break;
    }
    for (int i = r; i >= 1; --i) {
      if (mp[i][j] == '.') {
        continue;
      }
      if (mp[i][j] == 'v') {
        ++ans;
      }
      ++mark[i][j];
      break;
    }
  }

  for (int i = 1; i <= r; ++i) {
    for (int j = 1; j <= c; ++j) {
      if (mark[i][j] == 4) {
        printf("IMPOSSIBLE\n");
        return;
      }
    }
  }

  printf("%d\n", ans);
}

int main() {
  int n_case;
  scanf("%d", &n_case);
  for (int index = 1; index <= n_case; ++index) {
    printf("Case #%d: ", index);
    solve();
  }
  return 0;
}
