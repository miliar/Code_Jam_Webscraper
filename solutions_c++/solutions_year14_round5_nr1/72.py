#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <utility>
#include <vector>
using namespace std;

typedef long long ll;
typedef pair<int, int> P;
typedef vector<P> Vp;
typedef vector<ll> Vll;
typedef vector<int> Vi;
typedef vector<Vi> Mi;

const int INF = 1000000000;

ll bin1(const Vll& sum, int i) {
  int n = sum.size() - 1;
  int e = 0, d = i;
  ll r = -1;
  while (e <= d) {
    int m = (e + d)/2;
    if (sum[m] < sum[i] - sum[m] or sum[m] < sum[n] - sum[i]) e = m + 1;
    else {
      r = sum[m];
      d = m - 1;
    }
  }
  return r;
}

ll bin2(const Vll& sum, int i) {
  int n = sum.size() - 1;
  int e = 0, d = i;
  ll r = -1;
  while (e <= d) {
    int m = (e + d)/2;
    if (sum[i] - sum[m] < sum[m] or sum[i] - sum[m] < sum[n] - sum[i]) d = m - 1;
    else {
      r = sum[i] - sum[m];
      e = m + 1;
    }
  }
  return r;
}

ll bin3(const Vll& sum, int i) {
  int n = sum.size() - 1;
  int e = 0, d = i;
  while (e <= d) {
    int m = (e + d)/2;
//     cerr << "m=" << m << endl;
    if (sum[n] - sum[i] < sum[m]) {
//       cerr << "A" << endl;
      d = m - 1;
    }
    else if (sum[n] - sum[i] < sum[i] - sum[m]) {
//       cerr << "B" << endl;
      e = m + 1;
    }
    else {
//       cerr << "C" << endl;
      return sum[n] - sum[i];
    }
  }
  return -1;
}

int main() {
  cout.setf(ios::fixed);
  cout.precision(10);
  int tcas;
  cin >> tcas;
  for (int cas = 1; cas <= tcas; ++cas) {  
    int n, p, q, r, s;
    cin >> n >> p >> q >> r >> s;
    Vll v(n);
    for (int i = 0; i < n; ++i) v[i] = (i*ll(p) + q)%r + s;
//     cerr << "v:";
//     for (int i = 0; i < n; ++i) cerr << " " << v[i];
//     cerr << endl;
    Vll sum(n + 1, 0);
    for (int i = 0; i < n; ++i) sum[i + 1] = sum[i] + v[i];
    ll minim = sum[n];
//     int ii = -1;
    for (int i = 0; i <= n; ++i) {
//       cerr << "i=" << i << endl;
      ll t1 = bin1(sum, i);
      ll t2 = bin2(sum, i);
      ll t3 = bin3(sum, i);
//       if (i == 5) cerr << "t1=" << t1 << " t2=" << t2 << " t3=" << t3 << endl;
//       int b = minim;
      if (t1 != -1) minim = min(minim, t1);
      if (t2 != -1) minim = min(minim, t2);
      if (t3 != -1) minim = min(minim, t3);
//       if (minim != b) ii = i;
    }
    cout << "Case #" << cas << ": " << (sum[n] - minim)/double(sum[n]) << endl;
//     cerr << ii << endl;
  }
}
