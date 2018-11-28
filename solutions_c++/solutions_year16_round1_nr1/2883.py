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

void proc(string s) {
  list<char> a;
  a.push_back(s[0]);
  fl(i, 1, s.length()) {
    if(s[i] >= a.front()) {
      a.push_front(s[i]);
    }else{
      a.push_back(s[i]);
    }
  }
  for(auto e:a) {
    cout << e;
  }
}

int main() {
  ll T;
  cin >> T;
  string s;
  fle(i, 1, T) {
    cin >> s;
    cout << "Case #" << i << ": ";
    proc(s);
    cout << endl;
  }
  return 0;
}
