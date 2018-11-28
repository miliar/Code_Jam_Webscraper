#include <bits/stdc++.h>

using namespace std;

set<string> vis;
vector<string> jc;
vector<vector<long long>> vals;
set<long long> primes;

void go2(string s) {
  vector<long long> t;
  vector<long long> nums;
  for (int b = 2; b <= 10; b++) {
    long long val = 0;
    long long ss = 1;
    for (int i = s.size() - 1; i >= 0; i--) {
      if (s[i] == '1') val += ss;
      ss *= b;
    }
    nums.push_back(val);
    if (primes.count(val)) return;
  }

  bool hit = false;
  for (long long val : nums) {
    for (long long vv : primes) {
      if (val % vv == 0) {
        hit = true;
        t.push_back(vv);
        break;
      }
    }
  }

  if (!hit) return;
  if (t.size() != 9) return;
  jc.push_back(s);
  vals.push_back(t);
}

int p = 0;
void go(string s) {
  if (jc.size() >= 50) return;
  if (s.size() == 15){
    s += "1";
    p++;
    //cout << s << endl;
    if (vis.count(s)) return;
    vis.insert(s);

    go2(s);
    return;
  }

  go(s + "0");
  go(s + "1");
}

int main () {
  ifstream f("primes");
  string line;
  while(getline(f, line)) {
    istringstream iss(line);
    int p;
    while (iss >> p) {
      primes.insert(p);
    }
  }
  go("1");
  cout << "Case #1:" << endl;
  for (int i = 0; i < jc.size(); i++) {
    cout << jc[i] << " ";
    for (int p = 0; p < vals[i].size(); p++) {
      cout << vals[i][p];
      if (p != vals[i].size()-1) cout << " ";
    }
    cout << endl;
  }
  return 0;
}
