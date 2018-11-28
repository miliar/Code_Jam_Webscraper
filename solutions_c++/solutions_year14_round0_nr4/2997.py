#include <iostream>
#include <algorithm>

using namespace std;

int N;
const int N_MAX = 2000;
double naomi[N_MAX];
double ken[N_MAX];

void init() {
  cin >> N;
  for (int i = 0; i < N; i++)
    cin >> naomi[i];
  sort(naomi, naomi + N);
  for (int i = 0; i < N; i++)
    cin >> ken[i];
  sort(ken, ken + N);
}

int deceitful_score() {
  int ken_lower = 0, ken_upper = N - 1;
  int naomi_score = 0;

  for (int i = 0; i < N; i++) {
    if (naomi[i] > ken[ken_lower]) {
      ken_lower++;
      naomi_score++;
    } else {
      ken_upper--;
    }
  }
  return naomi_score;
}

int honest_score() {
  int ken_lower = 0, ken_upper = N - 1;
  int naomi_score = 0;

  for (int i = N - 1; i >= 0; i--) {
    if (ken[ken_upper] < naomi[i]) {
      ken_lower++;
      naomi_score++;
    } else {
      ken_upper--;
    }
  }
  return naomi_score;
}

void solve_case(int t) {
  init();
  cout << "Case #" << t << ": "
       << deceitful_score() << " "
       << honest_score() << "\n";
}

int main() {
  int T;
  cin >> T;

  for (int i = 0; i < T; i++) {
    solve_case(i + 1);
  }

  return 0;
}
