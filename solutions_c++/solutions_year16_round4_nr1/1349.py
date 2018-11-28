#include <bits/stdc++.h>

using namespace std;

char wins[256];
char loses[256];

string makeSetup(int n, char winner) {
  if (n == 0) {
    return string("") + winner;
  } else {
    string a = makeSetup(n - 1, winner);
    string b = makeSetup(n - 1, loses[winner]);

    if (a < b) {
      return a + b;
    } else {
      return b + a;
    }
  }
}

int count(string s, char c) {
  int result = 0;
  for (char i: s) {
    if (i == c) result++;
  }

  return result;
}

string solve() {
  int n, r, p, s;
  cin >> n >> r >> p >> s;

  vector<string> possible;

  vector<char> winners {'R', 'P', 'S'};

  for (char winner: winners) {
    string ans = makeSetup(n, winner);
    if (r == count(ans, 'R') && p == count(ans, 'P') && s == count(ans, 'S')) {
      possible.push_back(ans);
    }
  }

  sort(possible.begin(), possible.end());

  if (possible.size()) {
    return possible[0];
  } else {
    return "IMPOSSIBLE";
  }
}

int main() {
  wins['R'] = 'P';
  loses['R'] = 'S';

  wins['P'] = 'S';
  loses['P'] = 'R';

  wins['S'] = 'R';
  loses['S'] = 'P';

  int t;
  cin >> t;

  for (int c = 1; c <= t; c++) {
    cout << "Case #" << c << ": "<< solve() << endl;
  }
}
