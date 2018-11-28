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

ll proc(string S) {
  //bool s[100] = 0;
  //fl(i, 0, S.length()) s[i] = (S[i] == '+');

  // greedy 1: ignore last few +'s +---++++, because you won't do better by flipping some -'s there
  // greedy 2: the top must be -, the more the better +-+-+-+-+++++++, i.e. flip all +'s at the top, the only way to remove - in the middle is to flip whole stack

  ll count = 0;

  ll r = S.length();

  while(true) {

    while((r > 0) && S[r-1] == '+') r--;
    if(r == 0) {
      return count;
    }

    ll l = 0;
    while((l < S.length()) && S[l] == '+') l++;

    if (l > 0) {
      // flip head
      fl(i, 0, l) {
        S[i] = '-';
      }
      count ++;
    } else {
      // flip stack
      string K("");
      fl(i, 0, r) {
        K.insert(0, 1, S[i] == '+' ? '-' : '+');
      }
      fl(i, 0, r) {
        S[i] = K[i];
      }
      count ++;
    }
  }
  return count;
}

int main() {
  ll T;
  cin >> T;
  fle(i, 1, T) {
    string S;
    cin >> S;
    cout << "Case #" << i << ": ";
    cout << proc(S);
    cout << endl;
  }
  return 0;
}
