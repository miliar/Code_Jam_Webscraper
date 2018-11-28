#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <unordered_map>
#include <string>

using namespace std;

int N, R, P, S;

unordered_map<string, string> t;

bool check(string s) {
  while (s.length() > 0) {
    if (s.length() == 1) {
      return true;
    }

    string p = "";

    for (int i=0; i<s.length(); i+=2) {
      if (s[i] == s[i+1]) {
        return false;
      }

      string current = "";
      current += s[i];
      current += s[i+1];

      p += t[current];
    }

    s = p;
  }

  return false;
}

string solve() {
  // P , R , S
  string s = "";
  for (int i=0; i<P; i++) {
    s += "P";
  }
  for (int i=0; i<R; i++) {
    s += "R";
  }
  for (int i=0; i<S; i++) {
    s += "S";
  }

  vector<string> solutions;

  sort(s.begin(), s.end());

  do {
    if (check(s)) {
      solutions.push_back(s);
    }

  } while(std::next_permutation(s.begin(), s.end()));

  if (solutions.size() == 0) {
    return "IMPOSSIBLE";
  } else {
    sort(solutions.begin(), solutions.end());

    return solutions[0];
  }
}

int main() {
  t["PS"] = "S";
  t["SP"] = "S";
  t["PR"] = "P";
  t["RP"] = "P";
  t["RS"] = "R";
  t["SR"] = "R";

  int c;

  cin >> c;

  for (int i=0; i<c; i++) {

    cin >> N >> R >> P >> S;

    string result = solve();

    cout << "Case #" << (i+1) << ": " << result << endl;
  }

  return 0;
}
