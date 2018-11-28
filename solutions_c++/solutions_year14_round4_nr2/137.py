#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <algorithm>
#include <cassert>

using namespace std;

const int N_MAX = 1008;
int N;
int A[N_MAX];
int sorted[N_MAX];

void init() {
  cin >> N;
  for (int i = 0; i < N; i++) {
    cin >> A[i];
    sorted[i] = A[i];
  }

  sort(sorted, sorted + N);
}

void solve_case(int t) {
  init();

  int cost = 0;
  for (int i = 0; i < N; i++) {
    int num_left = N - i;

    int cur = sorted[i];
    int cur_idx = -1;
    for (int j = 0; j < num_left; j++) {
      if (cur == A[j]) {
        cur_idx = j;
        break;
      }
    }
    assert(cur_idx != -1);

    cost += min(cur_idx, num_left - cur_idx - 1);
    for (int j = cur_idx; j < num_left - 1; j++)
      A[j] = A[j + 1];
    A[num_left - 1] = cur; // for good measure
  }

  cout << "Case #" << t << ": " << cost << "\n";
}

int main() {
  int T;
  cin >> T;

  for (int i = 0; i < T; i++) {
    solve_case(i + 1);
  }

  return 0;
}
