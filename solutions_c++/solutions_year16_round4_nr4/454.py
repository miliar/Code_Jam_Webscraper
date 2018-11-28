#pragma GCC optimize("O3")
#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx")

#include <bits/stdc++.h>

#define pb push_back
#define fi first
#define se second
#define all(v) v.begin(), v.end()

using namespace std;
using ll = int64_t;

long start;
int res;

bool tl() {
  constexpr double kTl = 3.0;
  double gone = (clock() - start) / double(CLOCKS_PER_SEC);
  return gone > kTl;
}

const int N = 25;
int mt[N];
bool used[N];

bool dfs(int u, int n, const vector<int>& masks, int c) {
  if (used[u]) return false;
  used[u] = true;
  for (int v = 0; v < n; v++) {
    if (((masks[u] >> v) & 1) && ((c >> v) & 1)) {
      if (mt[v] == -1 || dfs(mt[v], n, masks, c)) {
        mt[v] = u;
        return true;
      }
    }
  }
  return false;
}

bool matching(int n, const vector<int>& masks, int skip, int mask) {
  memset(mt, -1, sizeof(mt));
  for (int i = 0; i < n; i++) {
    if (i != skip) {
      memset(used, 0, sizeof(used));
      dfs(i, n, masks, mask);
    }
  }
  for (int i = 0; i < n; i++) {
    if ((mask >> i) & 1) {
      if (mt[i] == -1) {
        return false;
      }
    }
  }
  return true;
}

vector<int> get_bad_ppl(int n, const vector<int>& masks) {
  vector<int> bad;
  bad.reserve(n);
  for (int i = 0; i < n; i++) {
    if (matching(n, masks, i, masks[i])) {
      bad.pb(i);
    }
  }
  return bad;
}

void bfs(int n, vector<int> masks, int for_ppl, int for_tasks) {
  assert(for_ppl > 0 && for_tasks > 0);
  queue<vector<int>> current;
  current.push(masks);
  vector<pair<int,int>> taken(n);

  for (int it = 0; !tl(); it++) {
    if (it >= res) break;
    queue<vector<int>> next;
    while (!current.empty()) {
      vector<int> current_masks = current.front();
      current.pop();
      vector<int> bad = get_bad_ppl(n, current_masks);
      if (bad.empty()) {
        res = it;
        return;
      }
      fill(all(taken), pair<int,int>{0, 0});
      for (int i = 0; i < n; i++) {
        taken[i].se = i;
        for (int j = 0; j < n; j++) {
          taken[i].fi += (current_masks[j] >> i) & 1;
        }
      }
      random_shuffle(all(taken));
      sort(all(taken));
      for (int i = 0; i < min(int(bad.size()), for_ppl); i++) {
        for (int j = 0; j < for_tasks; j++) {
          int ppl = bad[i];
          int task = taken[j].se;
          if (((current_masks[ppl] >> task) & 1) == 0) {
            current_masks[ppl] |= (1 << task);
            next.push(current_masks);
            current_masks[ppl] ^= (1 << task);
          }
        }
      }
    }
    current = next;
  }
}

void solve() {
  int n;
  cin >> n;

  vector<int> masks(n);
  for (int i = 0; i < n; i++) {
    string s;
    cin >> s;
    int mask = 0;

    for (char c : s) {
      mask <<= 1;
      mask |= (c - '0');
    }

    masks[i] = mask;
  }

  res = n * n;

  start = clock();

  cerr << "new test" << endl;

  for (int s = 2; s <= 2 * n; s++) {
    for (int p = 1; p < s; p++) {
      int r = s - p;
      if (r <= n && p <= n) {
        bfs(n, masks, p, r);
        cerr << "it " << s << " " << p << " " << s << " " << res << endl;
      }
    }
  }

  cout << res << endl;
}

int main() {
  srand(time(nullptr));
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int tests;
  cin >> tests;

  for (int test = 1; test <= tests; test++) {
    cout << "Case #" << test << ": ";
    solve();
  }

  return 0;
}
