#include <iostream>
#include <string>
#include <vector>

using namespace std;

namespace {

const string kImpossible = "IMPOSSIBLE";

string Solve(int R, int P, int S) {
  const int N = R + P + S;
  if (min(R, min(P, S)) != N / 3) return kImpossible;
  if (max(R, max(P, S)) != N / 3 + 1) return kImpossible;
  vector<int> v(1, 0);
  while (v.size() < N) {
    vector<int> w;
    for (int a : v) {
      w.push_back(a);
      w.push_back((a + 1) % 3);
    }
    v = w;
  }
  vector<int> counts(3);
  for (int a : v) ++counts[a];
  vector<char> m(3);
  for (int i = 0; i < 3; ++i) {
    if (counts[i] == R) {
      m[i] = 'R';
      R = -1;
      continue;
    }
    if (counts[i] == P) {
      m[i] = 'P';
      P = -1;
      continue;
    }
    if (counts[i] == S) {
      m[i] = 'S';
      S = -1;
      continue;
    }
  }
  string res;
  for (int a : v) res.push_back(m[a]);
  for (int i = 1; i < N; i *= 2) {
    for (int j = 0; j < N; j += i * 2) {
      if (res.substr(j, i) > res.substr(j + i, i)) {
        for (int k = 0; k < i; ++k) swap(res[j + k], res[j + i + k]);
      }
    }
  }
  return res;
}

}

int main(void) {
  int T;
  cin >> T;
  for (int i = 1; i <= T; ++i) {
    int N, R, P, S;
    cin >> N >> R >> P >> S;
    cout << "Case #" << i << ": " << Solve(R, P, S) << endl;
  }

  return 0;
}
