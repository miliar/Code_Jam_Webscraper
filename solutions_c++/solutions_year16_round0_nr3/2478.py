#include <bits/stdc++.h>

using namespace std;

bool ps[65536];
int p[6542], sz;
map<long long, vector<int> > ans;

void gen() {
  for(int i = 2; i < 65536; ++i) {
    if(ps[i] == 0) {
      p[sz++] = i;
      for(int j = i + i; j < 65536; j += i) {
        ps[j] = 1;
      }
    }
  }
}

int getPrimeFactor(long long n) {
  for(int i = 0; i < sz && p[i] * 1LL * p[i] <= n; ++i) {
    if(n % p[i] == 0) {
      return p[i];
    }
  }
  return 0;
}

vector<int> ok(int a, int m) {
  a = (a << 1) | 1;
  m++;
  vector<int> pf;
  for(int base = 2; base <= 10; ++base) {
    long long value = 1;
    for(int i = m - 1; i >= 0; --i) {
      value = value * base + ((a >> i) & 1);
    }
    int pp = getPrimeFactor(value);
    if(pp == 0) {
      break;
    }
    pf.push_back(pp);
  }
  return pf;
}

long long get(int a, int m) {
  a = (a << 1) | 1;
  m++;
  long long value = 1;
  for(int i = m - 1; i >= 0; --i) {
    value = value * 10 + ((a >> i) & 1);
  }
  return value;
}

void solve(int n, int j) {
  int m = n - 2;
  for(int a = 0; a < (1 << m) && j > 0; ++a) {
    vector<int> pf = ok(a, m);
    if(pf.size() == 9) {
      ans[get(a, m)] = pf;
      --j;
    }
  }
}

int main() {
#ifdef DEBUG
  freopen("input.txt", "rt", stdin);
#else
  freopen("C.in", "rt", stdin);
  freopen("C.out", "wt", stdout);
#endif
  gen();
  int t; cin >> t;
  for(int tst = 1; tst <= t; ++tst) {
    int n, j; cin >> n >> j;
    solve(n, j);
    cout << "Case #" << tst << ":" << endl;
    for(const auto &item : ans) {
      cout << item.first;
      for(int x : item.second) {
        cout << " " << x;
      }
      cout << endl;
    }
  }
  return 0;
}
