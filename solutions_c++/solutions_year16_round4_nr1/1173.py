#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <string>
#include <cstring>

using namespace std;

int N, R, P, S;
int n;
string rps = "RPS";

string Expand(const string& s) {
  string r;
  for (char c : s) {
    if (c == 'R') { r.push_back('S'); r.push_back('R'); }
    if (c == 'S') { r.push_back('P'); r.push_back('S'); }
    if (c == 'P') { r.push_back('P'); r.push_back('R'); }
  }
  return r;
}

bool Count(const string& s) {
  map<char, int> cnt;
  for (char c : s) ++cnt[c];
  return (cnt['P'] == P && cnt['S'] == S && cnt['R'] == R);
}

void Swap(string& s) {
  for (int i = 0; i < N; ++i) {
    int size = 1<<i;
    for (int j = 0; j < (int)s.size(); j += size*2) {
      string s0 = s.substr(j, size);
      string s1 = s.substr(j+size, size);
      if (s0 > s1) s = s.substr(0, j) + s1 + s0 + s.substr(j+size*2);
    }
  }
}

string Solve() {
  vector<string> r;
  for (char c : rps) {
    string seq(1, c);
    for (int i = 0; i < N; ++i) {
      n = i;
      seq = Expand(seq);
    }
    Swap(seq);
    if (Count(seq)) r.push_back(seq);
  }
  if (r.empty()) return "IMPOSSIBLE";
  return *std::min_element(r.begin(), r.end());
}

int main() {
  int nnn;
  cin >> nnn;
  for (int iii = 0; iii < nnn; ++iii) {
    cin >> N >> R >> P >> S;
    cout << "Case #" << iii+1 << ": " << Solve() << endl;
  }
}
