#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <list>
#include <queue>
#include <set>
#include <map>
#include <numeric>
#include <utility>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

const int N = 10;
int n;

char skill[N][N];

int best;

bool check(const int *perm) {
  for (int i = 0; i < n; ++i) {
    if (skill[i][perm[i]] == '1') continue;
    bool ok = false;
    for (int j = 0; !ok && j < n; ++j) {
      if (skill[i][perm[j]] == '0') continue;
      if (skill[j][perm[j]] == '1') continue;
      ok = true;
    }
    if (!ok) return false;
  }
  return true;
}

bool operate() {
  int perm[N];
  for (int i = 0; i < n; ++i) {
    perm[i] = i;
  }
  do {
    if (!check(perm)) return false;
  } while (next_permutation(perm, perm + n));
  return true;
}

void train(int a, int b, int cost) {
  if (cost >= best) return;
  if (b >= n) {
    train(a + 1, 0, cost);
    return;
  }
  if (a >= n) {
    if (operate()) {
      best = cost;
    }
    return;
  }
  train(a, b+1, cost);
  if (skill[a][b] == '0') {
    skill[a][b] = '1';
    train(a, b+1, cost + 1);
    skill[a][b] = '0';
  }
}

void train() {
  train(0, 0, 0);
}

void solve() {
  scanf("%d", &n);
  for (int i = 0; i < n; ++i) scanf("%s", skill + i); 
  best = n * n + 1;
  train();
  printf("%d\n", best);
}

int main() {
  int t;
  scanf("%d", &t);
  for (int tc = 1; tc <= t; ++tc) {
    printf("Case #%d: ", tc);
    solve();
  }
  return 0;
}
