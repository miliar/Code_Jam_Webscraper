#include <algorithm>
#include <cstring>
#include <stdio.h>
#include <queue>
#include <string>
#include <iostream>

using namespace std;

char buf[128];

int to_int(const string& s) {
  int n = s.length();
  int ret = 0;
  for (int i = 0; i < n; i++) {
    if (s[i] == '+') {
      ret |= (1 << i);
    }
  }
  return ret;
}

int flip(int n, int cur, int i) {
  for (int j = 0; j + j <= i; j++) {
    int k = i - j;
    bool p = bool(cur & (1 << j));
    bool q = bool(cur & (1 << k));
    if (p) {
      cur &= ~(1 << k);
    } else {
      cur |= (1 << k);
    }

    if (q) {
      cur &= ~(1 << j);
    } else {
      cur |= (1 << j);
    }
  }
  return cur;
}

int brute_force() {
  queue<int> q;
  string start = string(buf);
  int n = start.length();
  int dist[1 << n];
  memset(dist, -1, sizeof(dist));
  int x = to_int(start);
  dist[x] = 0;
  q.push(x);

  while (!q.empty()) {
    int cur = q.front();
    q.pop();
    if (cur == (1 << n) - 1) {
      return dist[cur];
    }
    for (int i = 0; i < n; i++) {
      int next = flip(n, cur, i);
      if (dist[next] == -1) {
        dist[next] = dist[cur] + 1;
        q.push(next);
      }
    }
  }

  return -1;
}

int solve() {
  return -1;
}

int main() {
  int T; scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    scanf("%s", buf);
    int r1 = brute_force();
    int r2 = solve();
    printf("Case #%d: ", t);
    printf("%d\n", r1);
  }
}
