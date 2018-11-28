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
#define REP(i,n) for (int i=0;i<int(n);++i)
typedef long long lint;
typedef vector<int> VI;
typedef pair<int, int> PII;

const int MOD = 1e9 + 7;

int lcp(const string &s, const string &t) {
  int a = 0;
  while (a < SZ(s) && a < SZ(t) && s[a] == t[a]) {
    ++a;
  }
  return a;
}

int m, n, mp[8][8];
string s[8];

int col[8];
int counter[1000100];

void dfs(int i, int k) {
  if (i == m) {
    counter[k] += 1;
  } else {
    REP (c, n) {
      col[i] = c;
      int kk = k;
      int o = 0;
      REP (j, i) {
        if (col[j] == c) {
          checkMax(o, mp[j][i]);
        }
      }
      dfs(i + 1, kk - o);
    }
  }
}

void work() {
  scanf("%d%d", &m, &n);
  int k = 0;
  REP (i, m) {
    char t[16];
    scanf("%s", t);
    s[i] = string(t);
    k += SZ(s[i]) + 1;
  }
  REP (i, m) {
    REP (j, m) {
      mp[i][j] = lcp(s[i], s[j]) + 1;
    }
  }
  fill(counter, counter + 1000100, 0);
  dfs(0, k);
  for (int i = 1000100 - 1; i >= 0; --i) {
    if (counter[i]) {
      printf("%d %d\n", i, counter[i]);
      break;
    }
  }
}

int main() {
  int n_case;
  scanf("%d", &n_case);
  for (int index = 1; index <= n_case; ++index) {
    printf("Case #%d: ", index);
    work();
  }
  return 0;
}
