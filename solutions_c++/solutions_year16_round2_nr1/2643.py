#include <bits/stdc++.h>

using namespace std;

#define _ << " " <<
#define trace(a) #a << "=" << a
typedef long long ll;
typedef long double ld;

vector<pair<char, int> > args = {
        {'Z', 0}, {'W', 2}, {'U', 4}, {'X', 6}, {'G', 8}, {'O', 1}, {'H', 3}, {'S', 7}, {'V', 5}, {'N', 9}
};
vector<string> numbers = {
        "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
};

string s;
map<char, int> cnt;
map<int, int> ans;

void go(char c, int d) {
  while (cnt[c] > 0)
  {
    for (int i = 0; i < numbers[d].size(); ++i)
      --cnt[numbers[d][i]];
    ++ans[d];
  }
}

string solve() {
  cin >> s;

  cnt.clear();
  int n = (int)s.size();
  for (int i = 0; i < n; ++i)
    cnt[s[i]]++;

  ans.clear();
  for (auto p : args)
    go(p.first, p.second);

  string ret = "";
  for (int i = 0; i < 10; ++i)
    for (int j = 0; j < ans[i]; ++j)
      ret += ('0' + i);

  return ret;
}

int main() {
  int t; cin >> t;
  for (int i = 1; i <= t; ++i)
    cout << "Case #" << i << ": " << solve() << endl;
  return 0;
}
