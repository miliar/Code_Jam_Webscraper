#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>
using namespace std;

const int MAXN = 222;

double P[MAXN];
int T;
int N, K;

double ans = 0;
double V[MAXN];

double ar[MAXN];
void check() {
  for(int i = 0; i <= K; ++i) {
    ar[i] = 0;
  }
  ar[0] = 1;
  for(int i = 0; i < K; ++i) {
    for(int j = K; j >= 0; --j) {
      double p = ar[j] * V[i];
      ar[j + 1] += p;
      ar[j] -= p;
    }
  }

  if (ar[K / 2] > ans) {
    ans = ar[K / 2];
  }
}

int main() {
  cin >> T;
  for(int t = 1; t <= T; ++t) {
    cin >> N >> K;
    for(int i = 0; i < N; ++i) {
      cin >> P[i];
    }
    sort(P, P + N);
    for(int i = 0; i < K; ++i) {
      V[i] = P[i];
    }
    ans = 0;

    check();
    for(int i = K - 1; i >= 0; --i) {
      V[i] = P[i + N - K];
      check();
    }
    cout << "Case #" << t << ": ";
    cout << fixed << setprecision(9) << ans << "\n";
  }
}

