#include <iostream>
#include <sstream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <map>
#include <set>

using namespace std;

int N;
map<string, int> words;
set<int> lines[200];
int GetIndex(const string& w) {
  words.emplace(w, words.size());
  return words[w];
}

int Solve1(int bits) {
  set<int> en = lines[0];
  set<int> fr = lines[1];
  for (int i = 2; i < N; ++i) {
    if (bits & (1<<(i-2))) {
      en.insert(lines[i].begin(), lines[i].end());
    } else {
      fr.insert(lines[i].begin(), lines[i].end());
    }
  }
  vector<int> both;
  set_intersection(en.begin(), en.end(), fr.begin(), fr.end(), back_inserter(both));
  return both.size();
}

int en[4048];
int fr[4048];

void Count(int cnt[], const set<int>& line, int d) {
  for (int w : line) {
    cnt[w] += d;
  }
}

int SolveR(int k) {
  if (k == N) {
    int cnt = 0;
    for (int i = 0; i < (int)words.size(); ++i) {
      if (en[i] > 0 && fr[i] > 0)
	++cnt;
    }
    return cnt;
  }
  int ans = words.size();
  Count(en, lines[k], 1);
  ans = min(ans, SolveR(k+1));
  Count(en, lines[k], -1);
  Count(fr, lines[k], 1);
  ans = min(ans, SolveR(k+1));
  Count(fr, lines[k], -1);
  return ans;
}

int Solve() {
  memset(en, 0, sizeof(en));
  memset(fr, 0, sizeof(fr));
  Count(en, lines[0], 1);
  Count(fr, lines[1], 1);
  return SolveR(2);
}

int main() {
  int nnn;
  cin >> nnn;
  for (int iii = 0; iii < nnn; ++iii) {
    words.clear();
    string st, w;
    cin >> N >> ws;
    for (int i = 0; i < N; ++i) {
      getline(cin, st);
      istringstream iss(st);
      lines[i].clear();
      while (iss >> w) {
	lines[i].insert(GetIndex(w));
      }
      // for (auto v : lines[i]) cout << v << " ";     cout << endl;
    }
    int ans = Solve();
    cout << "Case #" << iii+1 << ": " << ans << endl;
  }
}
