#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <cmath>

using namespace std;

struct vertex {
	int next[28];
	bool leaf;
};
 
vertex t[102];
int sz;

void add_string (const string & s) {
	int v = 0;
	for (size_t i=0; i<s.length(); ++i) {
		char c = s[i]-'A';
		if (t[v].next[c] == -1) {
			memset (t[sz].next, 255, sizeof t[sz].next);
			t[v].next[c] = sz++;
		}
		v = t[v].next[c];
	}
	t[v].leaf = true;
}

void doTest() {
  int n, m;
  scanf("%d%d\n", &n, &m);
  char str[9][12] = {0};
  int cnt[102] = {0};
  for (int i = 0; i < n; ++i) {
    gets(str[i]);
  }
  for (int mask = 0; mask < (1 << (2 * n)); ++mask) {
    vector<int> wh[4];
    bool ok = true;
    for (int i = 0; i < n; ++i) {
      int ind = (mask >> (2 * i)) & 3;
      if (ind >= m) {
        ok = false;
        break;
      }
      wh[ind].push_back(i);
    }
    if (!ok) continue;
    int cur = 0;
    for (int i = 0; i < m; ++i) {
      if (wh[i].size() == 0) continue;
      memset (t[0].next, 255, sizeof t[0].next);
      sz = 1;
      for (int j = 0; j < wh[i].size(); ++j)
        add_string(str[wh[i][j]]);
      cur += sz;
    }
    cnt[cur]++;
  }
  for (int i = 100; i >= 0; --i)
    if (cnt[i]) {
      printf("%d %d\n", i, cnt[i]);
      break;
    }
}

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int T;
  scanf("%d", &T);
  for (int test = 1; test <= T; ++test) {
    printf("Case #%d: ", test);
    doTest();
  }
  return 0;
}