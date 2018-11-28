#include <bits/stdc++.h>

using namespace std;

void recur_solve(string &line, int idx, vector<string> &res, string curr) {
  if (idx == line.size()) {
    res.push_back(curr);
    return;
  }

  recur_solve(line, idx+1, res, curr+line[idx]);
  recur_solve(line, idx+1, res, line[idx]+curr);
}

string solve(string &line) {
  vector<string> res;
  string curr = "";
  recur_solve(line, 0, res, curr);
  sort(res.begin(), res.end());
  return res[res.size() - 1];
}

int main() {
  int sz;
  cin >> sz;
  for (int i = 1; i <= sz; ++i) {
    string line;
    cin >> line;
    cout << "Case #" << i << ": " << solve(line) << endl;
  }
  return 0;
}