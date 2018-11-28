#include <bits/stdc++.h>
using namespace std;
const int MAXN = 65536;
typedef __int128 ll;
int pl[MAXN], m;

vector<pair<long long, vector<int>>> can;
int ok(ll n) {
  for (int i = 2; pl[i] < n && i < m; ++i) {
    if (n % i == 0) return i;
  }
  return -1;
}

void solve(long long msk, int n) {
  vector<int> d(9);
  for (int b = 2; b <= 10; ++b) {
    ll x = 0, p = 1;
    for (int i = 0; i < n; ++i) {
      if (msk >> i & 1) x += p;
      p *= b;
    }
    x = ok(x);
    if (x == -1) return;
    d[b - 2] = x;
  }
  can.push_back(make_pair(msk, d));
}

void run(int cas) {
  printf("Case #%d:\n", cas);
  int n, j; scanf("%d%d", &n, &j);
  int s = 1 << (n - 2);
  for (long long msk = 0; msk < s; ++msk) {
    solve((msk << 1) | 1 | (1ll << (n - 1)), n);
    if (can.size() == j) break;
  }
  for (int i = 0; i < j; ++i) {
    string s;
    long long m = can[i].first;
    while (m) s += char('0' + (m & 1)), m /= 2;
    reverse(s.begin(), s.end());
    printf("%s", s.c_str());
    for (auto &x: can[i].second) printf(" %d", x);
    puts("");
  }
  cerr << can.size() << std::endl;
}

int main() {
  for (int i = 2; i < MAXN; ++i) if (!pl[i]) {
    pl[m++] = i;
    for (int j = i + 1; j < MAXN; j += i) pl[j] = 1;
  }
  int T; scanf("%d", &T);
  for (int cas = 1; cas <= T; ++cas) run(cas);
  return 0;
}
