// {{{ template
#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<bool> vb;
typedef vector<string> vs;
typedef vector<long long> vll;
typedef vector<pii> vpii;
// }}}

const int N = 1001;

int split[N][N];
int maxi[N][N];

void init() {
  for (int i = 1; i <= 1000; i++) {
    for (int j = 0; j <= i; j++) {
      split[i][j] = 0;
    }
    for (int j = i + 1; j <= 1000; j++) {
      split[i][j] = INT_MAX / 2;
      for (int k = 1; k * 2 <= j; k++) {
        split[i][j] = min(split[i][j], split[i][k] + split[i][j - k] + 1);
      }
    }
  }
}

int main() {
  cin.sync_with_stdio(0); cin.tie(0);
  init();
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    int n;
    cin >> n;
    vi a(n);
    for (int i = 0; i < n; i++) {
      cin >> a[i];
    }
    int ans = INT_MAX;
    for (int i = 1; i <= 1000; i++) {
      int cur = 0;
      for (int j : a) {
        cur += split[i][j];
      }
      ans = min(ans, cur + i);
    }
    cout << "Case #" << t << ": " << ans << endl;
  }
  return 0;
}

