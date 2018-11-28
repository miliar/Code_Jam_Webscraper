#include <iostream>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

int n, k;

long double check(vector<int>& res) {
  vector<long double> prob(n + 1, 0.0);
  prob[0] = 1.0;
  for (int i : res) {
    long double p = 1.0 * i / 100.0;
    for (int pos = n - 1; pos >= 0; --pos) {
      prob[pos + 1] += prob[pos] * p;
      prob[pos] = prob[pos] * (1.0 - p);
    }
  }
  return prob[k / 2];
}

int main() {
  cout << fixed << setprecision(8);
  int tests;
  cin >> tests;
  for (int test = 1; test <= tests; ++test) {
    cin >> n >> k;
    vector<int> pr;
    int p1, p2;
    for (int i = 0; i < n; ++i) {
      scanf("%d.%d", &p1, &p2);
      pr.push_back(p1 * 100 + p2);
    }
    sort(pr.begin(), pr.end());
    int l = 0, r = n - 1;
    int cnt = 0;
    vector<int> res;
    //while (cnt < k) {
    //  if (pr[l] <= 50 && pr[r] >= 50) {
    //    res.push_back(pr[l]);
    //    res.push_back(pr[r]);
    //    ++l;
    //    --r;
    //  } else if (pr[l] > 50) {
    //    res.push_back(pr[l]);
    //    ++l;
    //    res.push_back(pr[l]);
    //    ++l;
    //  } else {
    //    res.push_back(pr[r]);
    //    --r;
    //    res.push_back(pr[r]);
    //    --r;
    //  }
    //  cnt += 2;
    //}
    //cout << "Case #" << test << ": " << check(res) << '\n';
    long double rr = 0.0;
    for (int mask = 0; mask < (1 << n); ++mask) {
      if (__builtin_popcount(mask) != k)
        continue;
      res.clear();
      for (int i = 0; i < n; ++i)
        if ((mask >> i) & 1)
          res.push_back(pr[i]);
      rr = max(rr, check(res));
    }
    cout << "Case #" << test << ": " << rr << '\n';
  }
  return 0;
}
