#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cassert>

using namespace std;

int N, R, P, S;
const int PLAYERS_MAX = 4000;
char answer[PLAYERS_MAX];

// depth starts at 0
// should have named it rounds_left
bool recurse(int depth, int p,int r, int s) {
  int pr = (r + p - s) / 2; // p wins
  int ps = (p + s - r) / 2; // s wins
  int rs = (r + s - p) / 2; // r wins
  if (pr < 0 || ps < 0 || rs < 0) return false;

  if (depth == N) { // TODO
    assert(p + r + s == 1);
    if (p == 1)
      answer[0] = 'P';
    else if (r == 1)
      answer[0] = 'R';
    else
      answer[0] = 'S';
    return true;
  }

  bool possible = recurse(depth + 1, pr, ps, rs); // r and s roles are swapped
  if (!possible)
    return false;

  int jump = 1 << (depth + 1);
  /*
  cout << "jump " << jump << endl;
  for (int i = 0; i < (1 << N); i++) {
    cout << answer[i];
  }
  cout << "\n";
  */

  for (int idx = 0; idx < (1 << N); idx += jump) {
    //cout << "checking " << answer[idx] << endl;
    if (answer[idx] == 'P') {
      answer[idx] = 'P'; answer[idx + jump/2] = 'R';
    } else if (answer[idx] == 'R') { // actually corresponds to ps
      answer[idx] = 'P'; answer[idx + jump/2] = 'S';
    } else if (answer[idx] == 'S') { // actually corresponds to rs
      answer[idx] = 'R'; answer[idx + jump/2] = 'S';
    } else {
      assert(false);
    }
  }

  /*
  for (int i = 0; i < (1 << N); i++) {
    cout << answer[i];
  }
  cout << "\nend\n";
  */

  return true;
}

void init() {
  cin >> N >> R >> P >> S;
  for (int i = 0; i < PLAYERS_MAX; i++)
    answer[i] = 'X';
}

void solve_case(int t) {
  init();
  cout << "Case #" << t << ": ";

  if (!recurse(0, P, R, S)) {
    cout << "IMPOSSIBLE\n";
    return;
  }

  for (int i = 0; i < (1 << N); i++) {
    cout << answer[i];
  }
  cout << "\n";
}

int main() {
  int T;
  cin >> T;

  for (int i = 0; i < T; i++) {
    solve_case(i + 1);
  }

  return 0;
}
