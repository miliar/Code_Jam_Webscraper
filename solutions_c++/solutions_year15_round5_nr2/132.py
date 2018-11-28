#include <bits/stdc++.h>

using namespace std;

void solve() {
  long long n, k;
  cin >> n >> k;
  vector<long long> sum(n - k + 1);
  for (long long i = 0; i < n - k + 1; ++i) cin >> sum[i];
  vector<long long> mn, mx;
  long long r2 = 0;
  long long c1 = 0;
  for (long long i = 0; i < k; ++i) {
    long long a = 0, b = 0, c = 0;
    for (long long j = i; j + 1 < n - k + 1; j += k) {
      //cerr << j << endl;
      c += sum[j + 1] - sum[j];
      a = min(a, c);
      b = max(b, c);
      ++c1;
    }
    mn.emplace_back(a);
    mx.emplace_back(b);
    r2 = max(r2, b - a);
    //cerr << a << " " << b << endl;
  }
  assert(c1 == n - k);
  long long ss = sum[0];
  for (long long i = 0; i < k; ++i) {
    mx[i] -= mn[i];
    ss += mn[i];
    //cerr << mx[i] << endl;
  }
  //cerr << ss << endl;
  long long kk = ss / k;
  ss -= kk * k;
  while (ss < 0) ss += k;
  while (ss >= k) ss -= k;
  long long r1 = *max_element(mx.begin(), mx.end());
  assert(r1 == r2);
  priority_queue<long long, vector<long long>, greater<long long>> que;
  for (long long i = 0; i < k; ++i) que.push(mx[i]);
  for (long long i = 0; i < ss; ++i) {
    long long now = que.top();
    que.pop();
    que.push(now + 1);
  }
  long long res = 0;
  while (!que.empty()) {
    long long now = que.top();
    que.pop();
    res = max(res, now);
  }
  assert(r1 == res || r1 + 1 == res);
  cout << res;
}

int main() {
  int t;
  cin >> t;
  //#pragma omp parallel for
  for (int i = 0; i < t; ++i) {
    cout << "Case #" << i + 1 << ": ";
    solve();
    cout << endl;
  }
}
