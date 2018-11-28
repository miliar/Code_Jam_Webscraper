#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

map<string, string> transitions;

void init() {
  transitions["11"] = "1";
  transitions["1i"] = "i";
  transitions["1j"] = "j";
  transitions["1k"] = "k";

  transitions["i1"] = "i";
  transitions["ii"] = "-1";
  transitions["ij"] = "k";
  transitions["ik"] = "-j";

  transitions["j1"] = "j";
  transitions["ji"] = "-k";
  transitions["jj"] = "-1";
  transitions["jk"] = "i";

  transitions["k1"] = "k";
  transitions["ki"] = "j";
  transitions["kj"] = "-i";
  transitions["kk"] = "-1";
}

string getTransition(string a, string b) {
  bool negative = false;
  if (a.length() > 1) {
    a = a.substr(1);
    negative ^= true;
  }
  if (b.length() > 1) {
    b = b.substr(1);
    negative ^= true;
  }
  string res = transitions[a + b];
  if (negative) {
    if (res.length() == 1) {
      res = "-" + res;
    } else {
      res = res.substr(1);
    }
  }
  return res;
}

void solve(int testCase) {
  int l, x;
  string s;
  cin >> l >> x >> s;
  string repeated;
  for (int i = 0; i < x; ++i) {
    repeated += s;
  }
  static const string target = "ij";
  string cur = "1";
  int pos = 0;
  for (int i = 0; i < repeated.length(); ++i) {
    cur = getTransition(cur, string(1, repeated[i]));
    if (cur[0] == target[pos] && pos < target.length()) {
      ++pos;
      cur = "1";
    }
  }
  cout << "Case #" << testCase << ": ";
  if (pos == 2 && cur == "k") {
    cout << "YES\n";
  } else {
    cout << "NO\n";
  }
}

int main() {
  init();
  int testCases;
  cin >> testCases;
  for (int i = 0; i < testCases; ++i) {
    solve(i + 1);
  }
  return 0;
}
