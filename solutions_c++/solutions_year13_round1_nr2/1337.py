#include <iostream>
#include <queue>
#include <cstdio>

using namespace std;

struct Node {
  int E;
  int cur;
  int gain;
  explicit Node(int E, int cur, int gain): E(E), cur(cur), gain(gain) {
  }
  void print() {
    printf("E = %d, cur = %d, gain = %d\n", E, cur, gain);
  }
};
int v[105];
int E, R, N;

int bfs() {
  queue<Node> q;
  int ret = 0;

  q.push(Node(E, 0, 0));
  while (!q.empty()) {
    Node a = q.front();
    q.pop();
    //a.print();
    ret = max(ret, a.gain);
    if (a.cur == N) {
      continue;
    }
    for (int i = 0; i <= a.E; ++i) {
      int nE = min(E, a.E - i + R);
      q.push(Node(nE, a.cur + 1, a.gain + v[a.cur] * i));
    }
  }
  return ret;
}

int main() {
  freopen("B-small-attempt0.in", "r", stdin);
  freopen("B-small-attempt0.out", "w", stdout);
  int T, cas = 1;

  cin >> T;
  while (T--) {
    printf("Case #%d: ", cas++);
    cin >> E >> R >> N;
    for (int i = 0; i < N; ++i) {
      cin >> v[i];
    }
    int ret = bfs();
    printf("%d\n", ret);
  }
  return 0;
}
