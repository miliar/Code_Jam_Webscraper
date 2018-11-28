#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cassert>
#include <iomanip>

using namespace std;

int K, N;
const int N_MAX = 250;
double P[N_MAX];

void update_probs(double cur[], double p) {
  double new_probs[N_MAX];
  new_probs[0] = cur[0] * (1 - p);
  for (int i = 1; i < N; i++) {
    new_probs[i] = cur[i] * (1 - p) + cur[i - 1] * p;
  }
  for (int i = 0; i < N; i++)
    cur[i] = new_probs[i];
}

void init() {
  cin >> N >> K;
  for (int i = 0; i < N; i++) {
    // TODO: precision issues?
    cin >> P[i];
  }
  sort(P, P + N);
}

void solve_case(int t) {
  init();
  // best to use extremes...

  double answer = 0.0;
  for (int i = 0; i <= K; i++) {
    double yes_probs[N_MAX];
    yes_probs[0] = 1;
    for (int j = 1; j < N; j++)
      yes_probs[j] = 0;

    for (int j = 0; j < i; j++) {
      update_probs(yes_probs, P[j]);
    }
    for (int j = 0; j < (K - i); j++) {
      update_probs(yes_probs, P[N - j - 1]);
    }
    answer = max(answer, yes_probs[K/2]);
  }
  cout << "Case #" << t << ": " << fixed << setprecision(9) << answer << "\n";
}

int main() {
  int T;
  cin >> T;

  for (int i = 0; i < T; i++) {
    solve_case(i + 1);
  }

  return 0;
}
