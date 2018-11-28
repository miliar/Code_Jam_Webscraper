#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>
using namespace std;
using ll = long long;

class range {private: struct I{int x;int operator*(){return x;}bool operator!=(I& lhs){return x<lhs.x;}void operator++(){++x;}};I i,n;
public:range(int n):i({0}),n({n}){}range(int i,int n):i({i}),n({n}){}I& begin(){return i;}I& end(){return n;}};

void solve();

int main() {
  int T; cin >> T;
  for (int test : range(1, T+1)) {
    cout << "Case #" << test << ":" << endl;
    solve();
  }
}

////////////////////////////////////////////////////////////////////////////////

ll mypow(int a, int b) {
  ll ret = 1;
  for (int i : range(b)) ret *= static_cast<ll>(a);
  return ret;
}

void solve() {
  int N, J;
  cin >> N >> J;

  // N is even
  for (int i = 0; i < J; ++i) {
    string s(N / 2 - 2, '0');
    for (int x = 0, r = i; r; ) {
      s[x] = '0' + (r % 2);
      r >>= 1;
      x++;
    }
    s = "1" + s + "1";
    cout << s << s;
    for (int b = 2; b <= 10; ++b) {
      ll d = mypow(b, N / 2) + 1LL;
      cout << " " << d;
    }
    cout << endl;
  }

}
