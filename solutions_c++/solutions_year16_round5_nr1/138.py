#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cassert>

using namespace std;

const int N_MAX = 210000;
int N;
string S;
char stack[N_MAX];

void init() {
  cin >> S;
  N = S.length();
  for (int i = 0; i < N; i++)
    stack[i] = '.';
}

void solve_case(int t) {
  init();

  int k = 0;
  for (int i = 0; i < N; i++) {
    if (k > 0 && S[i] == stack[k - 1]) {
      k--;
    } else {
      stack[k] = S[i];
      k++;
    }
  }

  assert(k % 2 == 0);
  int penalty = (k / 2) * 5;
  cout << "Case #" << t << ": " << (N * 5 - penalty) << "\n";
}

int main() {
  int T;
  cin >> T;

  for (int i = 0; i < T; i++) {
    solve_case(i + 1);
  }

  return 0;
}
