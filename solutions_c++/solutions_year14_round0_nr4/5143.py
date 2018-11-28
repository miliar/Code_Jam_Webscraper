#include <bits/stdc++.h>

#define each(i, c) for (auto& i : c)
#define unless(cond) if (!(cond))

using namespace std;

typedef long long int lli;
typedef unsigned long long ull;
typedef complex<double> point;

const int BIT = (1 << 10) + 1;
int memo[BIT][BIT];
int rec(int bit_a, int bit_b, const vector<double>& a, const vector<double>& b)
{
  int& ret = memo[bit_a][bit_b];
  if (ret != -1) return ret;

  const int N = a.size();
  if (bit_a == (1 << N) - 1 && bit_b == (1 << N) - 1) return 0;

  int mx = 0;
  for (int i = 0; i < N; ++i) {
    int mn = (1 << 29);
    for (int j = 0; j < N; ++j) {
      int na = bit_a | (1 << i);
      int nb = bit_b | (1 << j);
      if (na != bit_a && nb != bit_b) {
        mn = min(mn, rec(na, nb, a, b) + (a[i] > b[j]));
      }
    }
    if (mn != (1 << 29)) mx = max(mx, mn);
  }

  return ret = mx;
}

pair<int, int> small(vector<double> a, vector<double> b)
{
  sort(a.begin(), a.end());
  sort(b.begin(), b.end());

  vector<double> _a = a;
  vector<double> _b = b;

  const int N = a.size();
  pair<int, int> ret = make_pair(0, 0);

  {
    a = _a;
    b = _b;
    int cnt = 0;
    for (int i = 0; i < a.size(); ++i) {
      for (int j = 0; j < b.size(); ++j) {
        if (a[i] > b[j]) {
          ++cnt;
          b.erase(b.begin() + j);
          break;
        }
      }
    }
    ret.first = cnt;
  }

  {
    a = _a;
    b = _b;
    int cnt = 0;
    for (int i = 0; i < a.size(); ++i) {
      int idx = -1;
      for (int j = 0; j < b.size(); ++j) {
        if (a[i] < b[j]) {
          idx = j;
          break;
        }
      }
      if (idx != -1) {
        b.erase(b.begin() + idx);
      } else {
        ++cnt;
        b.erase(b.begin());
      }
    }
    ret.second = cnt;

    // fill(&memo[0][0], &memo[BIT - 1][BIT - 1] + 1, -1);
    // ret.second = rec(0, 0, a, b);
  }

  return ret;
}

int main(int argc, char *argv[])
{
  int tc;
  cin >> tc;
  while (tc--) {
    int n;
    cin >> n;
    vector<double> a(n), b(n);
    for (int i = 0; i < n; ++i) {
      cin >> a[i];
    }
    for (int i = 0; i < n; ++i) {
      cin >> b[i];
    }
    pair<int, int> p = small(a, b);
    static int cnt = 0;
    cout << "Case #" << ++cnt << ": " << p.first << ' ' << p.second << endl;
    continue;    
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());
    for (int i = 0; i < n; ++i) cout << a[i] << ' '; cout << endl;
    for (int i = 0; i < n; ++i) cout << b[i] << ' '; cout << endl;
    cout << endl;
  }
  return 0;
}
