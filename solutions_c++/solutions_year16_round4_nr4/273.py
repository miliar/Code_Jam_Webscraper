#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>
using namespace std;

typedef pair<int, int> pii;

const int inf = 1000 << 20;

const int MAXN = 30;
const int MAXK = 14; // <= 12
int DP[1 << MAXK][MAXN];
int T;
int N, K;
pii guys[MAXK];

int getDP(int msk, int special) {
  if (msk == 0) return special; // each special -- loner is 1
  int &ret = DP[msk][special];
  if (ret) return ret - 1;

  ret = inf;
  for(int i = msk; i > 0; i = i & (i - 1) & msk) {
    // take {i} + necessary special guys
    int a = 0;
    int b = 0;
    for(int j = 0; j < K; ++j) {
      if (i & (1 << j)) {
        a += guys[j].first;
        b += guys[j].second;
      }
    }
    int nspecial = special;
    if (a < b) {
      // need help
      nspecial -= b - a;
      a = b;
    }
    if (nspecial >= 0) {
      int rem = msk & ~i;
      int val = getDP(rem, nspecial) + a * a;
      if (val < ret) ret = val;
    }
  }
  return ret++;
}

int solve(vector<pii> v) {
  int special = 0;
  K = 0;
  for(int i = 0; i < int(v.size()); ++i) {
    if (v[i] == pii(1, 0)) {
      ++special;
    } else {
      guys[K] = v[i];
      ++K;
    }
  }
  memset(DP, 0, sizeof(DP));
  return getDP((1 << K) - 1, special);
}


int adj[MAXN][MAXN];
bool visx[MAXN];
bool visy[MAXN];

void floodx(int x, int &a, int &b);
void floody(int y, int &a, int &b) {
  if (visy[y]) return;
  visy[y] = 1;
  ++b;
  for(int i = 0; i < N; ++i) {
    if (adj[i][y]) {
      floodx(i, a, b);
    }
  }
}

void floodx(int x, int &a, int &b) {
  if (visx[x]) return;
  visx[x] = 1;
  ++a;
  for(int i = 0; i < N; ++i) {
    if (adj[x][i]) {
      floody(i, a, b);
    }
  }
}

int main() {
  cin >> T;
  for(int t = 1; t <= T; ++t) {
    cin >> N;
    int pre = 0;
    for(int i = 0; i < N; ++i) {
      string s; cin >> s;
      for(int j = 0; j < N; ++j) {
        adj[i][j] = s[j] == '1';
        pre += adj[i][j];
      }
    }
    for(int i = 0; i < N; ++i) {
      visx[i] = visy[i] = 0;
    }
    vector<pii> v;
    for(int i = 0; i < N; ++i) {
      if (!visx[i]) {
        int a = 0, b = 0;
        floodx(i, a, b);
        v.push_back(pii(a, b));
      }
    }
    int ans = solve(v) - pre;
    cout << "Case #" << t << ": " << ans << "\n";
  }
}

