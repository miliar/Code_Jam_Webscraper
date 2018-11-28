#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <tuple>
#include <string>
using namespace std;

string num[] = {"ZERO", "TWO", "FOUR", "SIX", "EIGHT", "ONE", "FIVE", "SEVEN", "THREE", "NINE"};
int mapn[] = {0, 2, 4, 6, 8, 1, 5, 7, 3, 9};

int count(string& x, char a) {
  int c = 0;
  for (int i = 0; i < x.size(); ++i) {
    if (x[i] == a) {
      ++c;
    }
  }
  return c;
}

void fill(int* a, string& x) {
  for (int i = 0; i < x.size(); ++i) {
    ++a[x[i] - 'A'];
  }
}

int has(string& x, string& n) {
  int ox[26] = {0};
  int on[26] = {0};

  fill(ox, x);
  fill(on, n);

  int m = 100000;
  for (int i = 0; i < 26; ++i) {
    if (on[i] == 0) {
      continue;
    }
    if (ox[i] >= on[i]) {
      int t = ox[i] / on[i];
      m = min(t, m);
    } else {
      return 0;
    }
  }

  for (int i = 0; i < 26; ++i) {
    for (int j = 0; j < m * on[i]; ++j) {
      x[x.find(i + 'A')] = 'Q';
    }
  }
  return m;
}

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cout << "Case #" << t << ": ";
    string code;
    cin >> code;
    vector<int> ans;
    for (int i = 0; i < 10; ++i) {
      int occ = has(code, num[i]);
      for (int j = 0; j < occ; ++j) {
        ans.push_back(mapn[i]);
      }
    }
    sort(ans.begin(), ans.end());
    for (int i = 0; i < ans.size(); ++i) {
      cout << ans[i];
    }

    cout << endl;
  }
}

