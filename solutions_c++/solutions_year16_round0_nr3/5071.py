#include <bits/stdc++.h>

#define each(i, c) for (auto& i : c)
#define unless(cond) if (!(cond))

using namespace std;

typedef long long int lli;
typedef unsigned long long ull;
typedef complex<double> point;

template<typename P, typename Q>
ostream& operator << (ostream& os, pair<P, Q> p)
{
  os << "(" << p.first << "," << p.second << ")";
  return os;
}

lli divisor(lli n)
{
  for (lli i = 2; i * i <= n; ++i) {
    if (n % i == 0) {
      return i;
    }
  }
  return -1;
}

bool is_prime(lli n)
{
  return divisor(n) == -1;
}

lli conv_base(lli m, lli base)
{
  lli sum = 0;
  lli w = 1;
  while (m) {
    sum += w * (m % 10);
    m /= 10;
    w *= base;
  }
  return sum;
}

lli base2(lli m)
{
  string s;
  while (m) {
    s += '0' + (m % 2) ;
    m /= 2;
  }
  reverse(s.begin(), s.end());
  sscanf(s.c_str(), "%lld", &m);
  return m;
}

int main(int argc, char *argv[])
{
  int tc;
  cin >> tc;
  while (tc--) {
    int n, j;
    cin >> n >> j;
    vector<lli> v;
    for (int bit = (1 << (n - 1)); bit < (1 << n); ++bit) {
      if (bit & 1) v.push_back(base2(bit));
    }
    map<lli, vector<lli>> jamcoin;
    each (m, v) {
      cerr << m << endl;
      vector<lli> u;
      for (int base = 2; base <= 10; ++base) {
        lli x = conv_base(m, base);
        if (!is_prime(x)) u.push_back(divisor(x));
      }
      if (u.size() == 9) jamcoin[m] = u;
      if (jamcoin.size() == j) break;
    }
    cout << "Case #1:" << endl;
    each (i, jamcoin) {
      cout << i.first ; each (j, i.second) cout << ' ' << j; cout << endl;
    }
  }
  return 0;
}
