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

lli g(pair<string, string> p)
{
  return labs(atol(p.first.c_str()) - atol(p.second.c_str()));
}

pair<string, string> f(string a, string b)
{
  enum { A, B, D };
  int state = D;
  const int N = a.size();
  for (int i = 0; i < N; ++i) {
    if (state == D) {
      if (a[i] == '?' && b[i] == '?') a[i] = b[i] = '0';
      else if (a[i] == '?') a[i] = b[i];
      else if (b[i] == '?') b[i] = a[i];
    } else if (state == A) {
      if (a[i] == '?' && b[i] == '?') { a[i] = '9'; b[i] = '0'; }
      else if (a[i] == '?') a[i] = '9';
      else if (b[i] == '?') b[i] = '0';
    } else if (state == B) {
      if (a[i] == '?' && b[i] == '?') { a[i] = '0'; b[i] = '9'; }
      else if (a[i] == '?') a[i] = '0';
      else if (b[i] == '?') b[i] = '9';
    }
    if (state == D && a[i] != b[i]) state = a[i] < b[i] ? A : B;
  }

  return make_pair(a, b);
}

int main(int argc, char *argv[])
{
  int tc;
  cin >> tc;
  while (tc--) {
    string a, b;
    cin >> a >> b;
    const int N = a.size();
    pair<string, string> p = f(a, b);
    lli diff =  g(p);

    for (int i = 0; i < N; ++i) {
      if (a[i] == '?') {
        for (char c = '0'; c <= '9'; ++c) {
          a[i] = c;
          pair<string, string> q = f(a, b);
          lli d = g(q);
          if (diff > d) { diff = d; p = q; }
          if (diff == d) { p = min(p, q); }
        }
        a[i] = '?';
      }
    }
    for (int i = 0; i < N; ++i) {
      if (b[i] == '?') {
        for (char c = '0'; c <= '9'; ++c) {
          b[i] = c;
          pair<string, string> q = f(a, b);
          lli d = g(q);
          if (diff > d) { diff = d; p = q; }
          if (diff == d) { p = min(p, q); }
        }
        b[i] = '?';
      }
    }
    for (int i = 0; i < N; ++i) {
      for (int j = 0; j < N; ++j) {
        unless (a[i] == '?' && b[j] == '?') continue;
        for (char c = '0'; c <= '9'; ++c) {
          for (char d = '0'; d <= '9'; ++d) {
            a[i] = c;
            b[j] = d;
            pair<string, string> q = f(a, b);
            lli D = g(q);
            if (diff > D) { diff = D; p = q; }
            if (diff == D) { p = min(p, q); }
          }
        }
        a[i] = b[j] = '?';
      }
    }
    
    static int t = 0;
    cout << "Case #" << ++t << ": " << p.first << ' ' << p.second << endl;
  }
  return 0;
}
