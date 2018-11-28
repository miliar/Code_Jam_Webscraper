#include <bits/stdc++.h>

using namespace std;

const int MAX_N = 5;

void print_answer(int case_id, int answer) {
  printf("Case #%d: %d\n", case_id, answer);
}

int n;
string graph[MAX_N];

bool can_operate[MAX_N][MAX_N];
bool is_taken[MAX_N];

bool rec(int pos, const vector<int> &p) {
  if (pos == n) {
    return true;
  }

  int v = p[pos];

  bool gflag = false;
  for (int i = 0; i < n; i++) {
    if (!can_operate[v][i] || is_taken[i]) {
      continue;
    }

    gflag = true;

    is_taken[i] = true;
    bool flag = rec(pos + 1, p);
    is_taken[i] = false;

    if (!flag) {
      return false;
    }
  }

  return gflag;
}

void solve(int case_id) {
  cin >> n;
  for (int i = 0; i < n; i++) {
    cin >> graph[i];
  }

  int answer = MAX_N * MAX_N;

  for (int mask = 0; mask < (1 << (n * n)); mask++) {
    int cost = 0;
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        int k = i * n + j;

        int b = (mask >> k) & 1;
        int c = graph[i][j] - '0';

        if (b == 0 && c == 0) {
          // do nothing
        } else if (b == 0 && c == 1) {
          cost = MAX_N * MAX_N;
        } else if (b == 1 && c == 0) {
          cost += 1;
        } else {
          // do nothing
        }

        can_operate[i][j] = b;
      }
    }

    if (cost > answer) {
      continue;
    }

    vector<int> p(n);
    for (int i = 0; i < n; i++) {
      p[i] = i;
    }

    bool flag = true;

    do {
      if (!rec(0, p)) {
        flag = false;
      }
    } while (next_permutation(p.begin(), p.end()));

    // cerr << mask << " " << cost << " " << flag << "\n";

    if (flag) {
      answer = min(answer, cost);
    }
  }

  print_answer(case_id, answer);
}

int main() {
  int cases; cin >> cases;

  for (int i = 1; i <= cases; i++) {
    solve(i);
  }

  return 0;
}