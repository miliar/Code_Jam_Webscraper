#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <set>
#include <queue>

using namespace std;

#define forn(i, n) for(int i = 0; i < (n); ++i)

int n;

struct MASK {
  int data[4];

  void init() {
    fill(data, data + 4, 0);
  }

  void set(int index, int value) {
    data[index >> 5] |= 1 << (index & 31);
    data[index >> 5] ^= (1 ^ value) << (index & 31);
  }

  int get(int index) const {
    return (data[index >> 5] >> (index & 31)) & 1;
  }

  vector<int> compr() const {
    vector<int> compr;
    compr.push_back(get(0));
    for (int i = 1; i < n; ++i) {
      if (get(i) != get(i - 1)) {
        compr.push_back(get(i));
      }
    }
    return compr;
  }

};

inline bool operator<(const MASK& a, const MASK& b) {
  // return a.compr() < b.compr();
  if (a.data[0] != b.data[0]) return a.data[0] < b.data[0];
  if (a.data[1] != b.data[1]) return a.data[1] < b.data[1];
  if (a.data[2] != b.data[2]) return a.data[2] < b.data[2];
  return a.data[3] < b.data[3];
}

int solve_fast(string s) {
  n = s.size();
  int first = (s[0] == '-' ? 0 : 1);
  int len = 1;
  for (int i = 1; i < n; ++i) {
    if (s[i] != s[i - 1]) {
      len++;
    }
  }
  if (first == 0) {
    return 1 + (len - 1) / 2 * 2;
  } else {
    if (len == 1) {
      return 0;
    }
    return ((len - 2) / 2  + 1) * 2;
  }
}

void solve() {
  string s;
  cin >> s;
  n = s.size();
  MASK init;
  init.init();
  for (int i = 0; i < n; ++i) {
    init.set(i, (s[i] == '+'));
  }
  
  map<MASK, int> ops;
  queue<MASK> q;


  ops[init] = 0;
  q.push(init);

  vector<vector<int>> ans;

  while (!q.empty()) {
    MASK top = q.front();
    q.pop();
    int d = ops[top];
    auto x = top.compr();
    ans.push_back({x[0], (int) x.size(), d});
    // cout << x[0] << ' ' << x.size() << ' ' << d << endl;
    // auto compr = top.compr();
    // for (int i = 0; i < compr.size(); ++i) {
      // cout << compr[i];
    // }
    // cout << endl;
    for (int i = 0; i < n; ++i) {
      MASK next = top;
      for (int l = 0, r = i; l < r; ++l, --r) {
        int x = next.get(l);
        int y = next.get(r);
        next.set(l, y);
        next.set(r, x);
      }
      for (int j = 0; j <= i; ++j) {
        next.set(j, next.get(j) ^ 1);
      }
      auto it = ops.find(next);
      if (it == ops.end()) {
        ops[next] = d + 1;
        q.push(next);
      }
    }
  }
  sort(ans.begin(), ans.end());
  ans.erase(unique(ans.begin(), ans.end()), ans.end());
  for (int i = 0; i < ans.size(); ++i) {
    cout << ans[i][0] << ' ' << ans[i][1] << ' ' << ans[i][2] << endl;
  }
}

int main() {
  // freopen("in.txt", "r", stdin);
  freopen("B-large.in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  ios_base::sync_with_stdio(false);
  int t;
  cin >> t;
  for (int i = 0; i < t; ++i) {
    cout << "CASE #" << i + 1 << ": ";

    string s;
    cin >> s;
    cout << solve_fast(s) << endl;
  }

  return 0;
}