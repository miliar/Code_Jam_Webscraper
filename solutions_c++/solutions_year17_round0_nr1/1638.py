#include <bits/stdc++.h>

using namespace std;

int main() {
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  
  int tests;
  cin >> tests;
  for (int test = 0; test < tests; test++) {
    string s;
    int k;
    
    cin >> s >> k;
    vector<int> turn(s.size(), 0);
    for (int i = 0; i < s.size(); i++) {
      if (s[i] == '+') {
	turn[i] = 1;
      }
    }

    int cnt = 0;
    for (int i = 0; i <= s.size() - k; i++) {
      if (!turn[i]) {
	cnt++;
	for (int j = i; j < i + k; j++) {
	  turn[j] = !turn[j];
	}
      }
    }

    int good = 1;
    for (int i = s.size() - k + 1; i < s.size(); i++) {
      if (!turn[i]) {
	good = 0;
      }
    }

    cout << "Case #" << (test + 1) << ": ";
    if (!good) {
      cout << "IMPOSSIBLE\n";
    } else {
      cout << cnt << "\n";
    }
  }
  return 0;
}
