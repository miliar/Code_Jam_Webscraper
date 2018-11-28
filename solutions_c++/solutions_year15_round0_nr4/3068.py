#include <iostream>
#include <algorithm>
#include <memory.h>
#include <cstdio>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <map>
using namespace std;
#define sz(s) int((s).size())
#define clr(a) memset(a,0,sizeof(a))
#define all(x) (x).begin(),(x).end()
#define rep(i,n) for(int(i)=0; (i)<(n);++(i))
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
typedef pair <int,int> pii;
typedef long long LL;
template <class T> inline T gcd(T a,T b){return (!b? a : gcd(b,a%b));}
template <class T> inline T ABS(T x){return ((x)>0?(x):(-(x)));}
const int N = 1 << 20;

int x, r, c;

inline bool solve_one () {
  return 0;
}

inline bool solve_two () {
  if (r == 1 && c == 1) {
    return 1;
  }
  if ((r * c) % 2 == 0) {
    return 0;
  }
  return 1;
}

inline bool solve_three () {
  if (r <= 2 && c <= 2) {
    return 1;
  }
  if (r == 3 && c == 1) {
    return 1;
  }
  if (r * c % 3 == 0) {
    return 0;
  }
  return 1;
}

inline bool solve_four () {
  if (r <= 3 && c <= 3) {
    return 1;
  }
  if (r == 4 && c <= 2) {
    return 1;
  }
  return 0;
}

int main () {
  freopen ("in.txt", "r", stdin);
  freopen ("out.txt", "w", stdout);
  cin.sync_with_stdio (0); cin.tie (0);
  int tt;
  cin >> tt;
  for (int tc = 1; tc <= tt; ++tc) {
    cout << "Case #" << tc << ": ";
    cin >> x >> r >> c;
    if (r < c) {
      swap (r, c);
    }
    bool ok;
    if (x == 1) {
      ok = solve_one ();
    } else if (x == 2) {
      ok = solve_two ();
    } else if (x == 3) {
      ok = solve_three ();
    } else if (x == 4) {
      ok = solve_four ();
    }
    cout << (ok ? "RICHARD" : "GABRIEL") << '\n';
  }
}
