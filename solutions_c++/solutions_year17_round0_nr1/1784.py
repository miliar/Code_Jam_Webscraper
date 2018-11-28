#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>

using namespace std;

int K;

long solve(string S, int i) {
    if (i == 0) {
  bool cant = true;
      for (int p=0; p<S.size(); p++) {
        if (S[p] != '+') {
          cant = false;
        }
      }
      if (cant) {
        return 0;
      }
    }

  // final stage
  if ((i+K) == S.size()) {
    int minus = 0, plus = 0;
    for (int j=i; j<S.size(); j++) {
      if (S[j] == '-') {
        minus++;
      } else {
        plus++;
      }
      if (minus != 0 && plus != 0) {
        return -1;
      }
    }
    if (minus != 0) {
      return 1;
    } else {
      return 0;
    }
  }

  // no flip
  long solution1 = -1;
  if (S[i] == '+') {
    solution1 = solve(S, i+1);
  }

  // flip
  long solution2 = -1;
  if (S[i] == '-') {
    for (int j=i; j<i+K; j++) {
      if (S[j] == '-') {
        S[j] = '+';
      } else {
        S[j] = '-';
      }
    }

    solution2 = solve(S, i+1);
  }

  if (solution1 == -1 && solution2 == -1) {
    return -1;
  } else if (solution1 == -1) {
    return solution2+1;
  } else if (solution2 == -1) {
    return solution1;
  } else {
    return min(solution1, solution2+1);
  }
}

int main() {
  int T;
  cin >> T;
  for (int i=1; i<=T; i++) {
    string S;
    cin >> S;

    cin >> K;

    long result = solve(S, 0);

    if (result == -1) {
      cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;
    } else {
      cout << "Case #" << i << ": " << result << endl;
    }
  }

  return 0;
}
