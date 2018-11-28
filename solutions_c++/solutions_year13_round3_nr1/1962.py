#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <algorithm>

using namespace std;

string in;
int n;

set<char> vowels = {'a','e','i','o','u'};

bool ok(const string& s) {
  int k = 0;
  for (int i = 0; i < s.size(); ++i) {
    if (vowels.count(s[i]) == 0)
      ++k;
    else {
      if (k >= n) return true;
      k = 0;
    }
  }
  return k >= n;
}

int solve() {
  int ret = 0;
  for (int i = 0; i < in.size()-n+1; ++i) {
    for (int j = i+n-1; j < in.size(); ++j) {
      if (ok(in.substr(i, j-i+1)))
        ++ret;
    }
  }
  return ret;
}

int main(void) {
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cin >> in >> n;
    cout << "Case #" << t << ": " << solve() << endl;
  }
}
