#include <cmath>
#include <cstdio>
#include <cstring>
#include <cassert>
#include <set>
#include <string>
#include <vector>
#include <algorithm>
using std::string;
using std::vector;
using std::set;

int m, n;
int x, cnt;
char buffer[111];
int id[1111];
vector<string> s;

void DFS(int p) {
  if (p == m) {
    set<string> ss[4];
    for (int i = 0; i < m; ++i) {
      string tmp;
      ss[id[i]].insert(tmp);
      for (int j = 0; j < s[i].length(); ++j) {
        tmp.push_back(s[i][j]);
        ss[id[i]].insert(tmp);
      }
    }
    int tcnt = 0;
    for (int i = 0; i < n; ++i) {
      tcnt += ss[i].size();
    }
    if (tcnt > x) {
      x = tcnt;
      cnt = 0;
    }
    if (tcnt == x) ++cnt;
    return;
  }
  for (id[p] = 0; id[p] < n; ++id[p]) {
    DFS(p + 1);
  }
}

void Work() {
  x = 0;
  cnt = 0;
  s.clear();
  scanf("%d%d", &m, &n);
  for (int i = 0; i < m; ++i) {
    scanf(" %s", buffer);
    s.push_back(buffer);
  }
  DFS(0);
  printf("%d %d\n", x, cnt);
}

int main() {
  int cases;
  scanf("%d", &cases);
  for (int i = 1; i <= cases; ++i) {
    printf("Case #%d: ", i);
    Work();
  }
  return 0;
}
