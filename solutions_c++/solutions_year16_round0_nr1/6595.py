#include <iostream>
#include <algorithm>
#include <cassert>
#include <map>
#include <list>
#include <vector>
#include <queue>
#include <cstdio>
#include <cstring>
#include <cmath>

#ifdef _WIN32
#define lls "%I64d"
#define sll(n) scanf(lls, &(n));
#else
#define lls "%lld"
#define sll(n) scanf(lls, &(n))
#endif

#define modz 1000000007

typedef unsigned long long ull;
typedef long long ll;
#define fle(var, start, end) for (ll var = (start); var <= (end); ++var)
#define fl(var, start, end) for (ll var = (start); var < (end); ++var)
#define elf(var, end, start) for (ll var = (end); var >= (start); --var)
#define lf(var, end, start) for (ll var = (end)-1; var >= (start); --var)
#define dump(container)                                                        \
  fl(auto e : container) cout << e << " ";                                     \
  cout << endl;

template <class T> T gcd(T a, T b) {
  if (a < b)
    swap(a, b);
  return b ? gcd(b, a % b) : a;
}
template <class T> T lcm(T a, T b) { return a / gcd(a, b) * b; }

using namespace std;

ll proc(ll v) {
  if(v == 0) {
    return -1;
  }

  bool m[10] = {0};
  fle(i, 1, 9999999) {
    ll f = v * i;
    ll t = f;

    while(t) {
      m[t%10] = true;
      t /= 10;
    }

    bool done = true;
    fl(j, 0, 10) {
      if (!m[j]) {
        done = false;
        break;
      }
    }

    if(done) {
      return f;
    }
  }

  return -1;
}

int main() {
  ll T;
  cin >> T;
  fle(i, 1, T) {
    ll v;
    cin >> v;
    ll a = proc(v);
    cout << "Case #" << i << ": ";
    if (a == -1) cout << "INSOMNIA"; else cout << a;
    cout << endl;
  }
  return 0;
}
