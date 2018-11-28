#include <stdlib.h>
#include <iostream>
#include <vector>
#include <algorithm>

// PRS

using namespace std;

string fix(string S)
{
  if (S == "IMPOSSIBLE") {
    return S;
  }
  if (S.length() <= 1) {
    return S;
  }
  string A = "";
  string B = "";
  for (int i = 0; i < S.length() / 2; i++) {
    A += S[i];
    B += S[S.length() / 2 + i];
  }
  A = fix(A);
  B = fix(B);
  if (lexicographical_compare(A.begin(), A.end(), B.begin(), B.end())) {
    return A + B;
  }
  return B + A;
}

string solve(int N, int R, int P, int S)
{
  if (N == 0) {
    if (R == 1) {
      return "R";
    }
    if (P == 1) {
      return "P";
    }
    if (S == 1) {
      return "S";
    }
  }
  if (R > P + S || P > R + S || S > P + R) {
    // more than half
    return "IMPOSSIBLE";
  }
  int PR = (R + P + S) / 2 - S;
  int SP = (R + P + S) / 2 - R;
  int RS = (R + P + S) / 2 - P;

  string ans = solve(N - 1, RS, PR, SP);
  if (ans == "IMPOSSIBLE") {
    return "IMPOSSIBLE";
  }
  else {
    string temp = "";
    for (int i = 0; i < ans.length(); i++) {
      if (ans[i] == 'R') {
        temp += "RS";
      }
      if (ans[i] == 'P') {
        temp += "PR";
      }
      if (ans[i] == 'S') {
        temp += "SP";
      }
    }
    return temp;
  }
}

int main()
{
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    int N, R, P, S;
    cin >> N >> R >> P >> S;
    cout << "Case #" << t << ": " << fix(solve(N, R, P, S)) << "\n";
  }
  return 0;
}

