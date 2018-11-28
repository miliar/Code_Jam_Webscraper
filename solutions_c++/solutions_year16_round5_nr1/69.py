#include <iostream>
#include <stack>
#include <string>

using namespace std;

namespace {

int Solve(string S) {
  const int N = S.size();
  int res = 0;
  stack<char> s;
  for (int i = 0; i < N; ++i) {
    if (s.size() == N - i || s.size() > 0 && s.top() == S[i]) {
      res += s.top() == S[i];
      s.pop();
    } else {
      ++res;
      s.push(S[i]);
    }
  }
  return 5 * res;
}

}

int main(void) {
  int T;
  cin >> T;
  for (int i = 1; i <= T; ++i) {
    string S;
    cin >> S;
    cout << "Case #" << i << ": " << Solve(S) << endl;
  }

  return 0;
}
