#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>

using namespace std;

void flip(string& s, int k) {
  string s_copy = s;
  for (int i = 0; i < k; i++) {
    char c = s_copy[k - i - 1];
    if (c == '+') {
      c = '-';
    } else {
      c = '+';
    }
    s[i] = c;
  }
}

int solveSimple(string s) {
  int n = s.size();
  int answer = 0;

  for (int i = n - 1; i >= 0; --i) {
    if (s[i] == '+') {
      continue;
    }
    if (s[0] == '+') {
      for (int j = 0; j < n; j++) {
        if (s[j] == '+') {
          s[j] = '-';
        } else {
          break;
        }
      }
      ++answer;
    }
    flip(s, i + 1);
    ++answer;
  }

  return answer;
}

void solveCase() {
  string s;
  cin >> s;

  int answer = solveSimple(s);

  cout << answer;
  cerr << answer;
}

#define NAME "B-large"
//#define NAME "B-small-attempt2"
//#define NAME "test"

int main() {
  freopen(NAME ".in", "rt", stdin);
  freopen(NAME ".out", "wt", stdout);
  int T;
  cin >> T;
  for (int i = 1; i <= T; i++) {
    cout << "Case #" << i << ": ";
    cerr << "Case #" << i << ": ";
    solveCase();
    cout << endl;
    cerr << endl;
  }
  return 0;
}
