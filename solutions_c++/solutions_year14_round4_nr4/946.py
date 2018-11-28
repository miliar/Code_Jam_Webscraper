#include <algorithm>
#include <cmath>
#include <functional>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <unordered_map>
#include <queue>
#include <random>
#include <set>
using namespace std;

int nx[5][100][30];
int cntTr[10];

void add(char* c, int id, int i) {
  if (*c == 0) {
    return;
  }

  int cur = (*c - 'A');
  if (nx[id][i][cur] == -1) {
    ++cntTr[id];
    nx[id][i][cur] = cntTr[id];
  }

  add(c + 1, id, nx[id][i][cur]);
}

char s[100][100];
int go[100];
int n;
int k;

int getAns() {
  memset(cntTr, 0, sizeof(cntTr));
  memset(nx, -1, sizeof(nx));
  for (int i = 0; i < n; ++i) {
    add(s[i], go[i], 0);
  }
  int r = 0;
  for (int i = 0; i < k; ++i) {
    r += cntTr[i];
    if (cntTr[i] != 0) {
      ++r;
    }
  }
  return r;
}

int main() {
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);

  int T;
  cin >> T;
  for (int tests = 0; tests < T; ++tests) {
    cout << "Case #" << tests+1 << ": ";
    scanf("%d%d\n", &n, &k);
    for (int i = 0; i < n; ++i) {
      gets(s[i]);
    }
    int cnt = 1;
    for (int i = 0; i < n; ++i) {
      cnt *= k;
    }
    int assign = 0;
    int mx = 0;
    for (int i = 0; i < cnt; ++i) {
      int x = i;
      for (int j = 0; j < n; ++j) {
        go[j] = x % k;
        x /= k;
      }

      int ans = getAns();
      if (ans > mx) {
        mx = ans;
        assign = 1;
      } else if (ans == mx) {
        ++assign;
      }
    }
    cout << mx << " " << assign << endl;
  }

  return 0;
}