#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

#define clr(x) memset((x), 0, sizeof(x))
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define sz size()
#define For(i, st, en)  for(int i=(st); i<=(int)(en); i++)
#define Forn(i, st, en) for(int i=(st); i<=(int)(en); i++)
#define Ford(i, st, en) for(int i=(st); i>=(int)(en); i--)
#define forn(i, n) for(int i=0; i<(int)(n); i++)
#define ford(i, n) for(int i=(n)-1; i>=0; i--)
#define fori(it, x) for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); it++)

template <class _T> inline _T sqr(const _T& x) { return x * x; }
template <class _T> inline string tostr(const _T& a) { ostringstream os(""); os << a; return os.str(); }
template <class _T> inline istream& operator << (istream& is, const _T& a) { is.putback(a); return is; }

// Types
typedef long double ld;
typedef signed   long long i64;
typedef signed   long long ll;
typedef unsigned long long u64;
typedef unsigned long long ull;
typedef set < int > SI;
typedef vector < ld > VD;
typedef vector < int > VI;
typedef vector < bool > VB;
typedef vector < string > VS;
typedef map < string, int > MSI;
typedef pair < int, int > PII;

// Constants
const ld PI = 3.1415926535897932384626433832795;
const ld EPS = 1e-11;

//#define debug(...)
#define debug printf

int R, C;
char board[101][101];

bool inRegion(int r, int c) {
  return r >= 0 && r < R && c >=0 && c < C;
}

bool search(int r, int c, int vr, int vc) {
  r += vr;
  c += vc;
  while (inRegion(r, c)) {
    if (board[r][c] != '.') return true;
    r += vr;
    c += vc;
  }
  return false;
}

int count() {
  int cnt = 0;

  // up.
  for (int c = 0; c < C; ++c) {
    int r = 0;
    while (board[r][c] == '.') {
      if (!inRegion(r, c)) break;
      r++;
    }

    if (inRegion(r, c) && board[r][c] == '^') {
      if (search(r, c, 0, -1) || search(r, c, 0, 1) || search(r, c, 1, 0)) {
        //printf("up %d %d\n", r, c);
        cnt++;
      } else {
        return -1;
      }
    }
  }

  // down.
  for (int c = 0; c < C; ++c) {
    int r = R-1;
    while (board[r][c] == '.') {
      if (!inRegion(r, c)) break;
      r--;
    }

    if (inRegion(r, c) && board[r][c] == 'v') {
      if (search(r, c, 0, -1) || search(r, c, 0, 1) || search(r, c, -1, 0)) {
        //printf("down %d %d\n", r, c);
        cnt++;
      } else {
        return -1;
      }
    }
  }

  // left.
  for (int r = 0; r < R; ++r) {
    int c = 0;
    while (board[r][c] == '.') {
      if (!inRegion(r, c)) break;
      c++;
    }

    if (inRegion(r, c) && board[r][c] == '<') {
      if (search(r, c, 1, 0) || search(r, c, 0, 1) || search(r, c, -1, 0)) {
        //printf("left %d %d\n", r, c);
        cnt++;
      } else {
        return -1;
      }
    }
  }

  // right.
  for (int r = 0; r < R; ++r) {
    int c = C-1;
    while (board[r][c] == '.') {
      if (!inRegion(r, c)) break;
      c--;
    }

    if (inRegion(r, c) && board[r][c] == '>') {
      if (search(r, c, 1, 0) || search(r, c, 0, -1) || search(r, c, -1, 0)) {
        //printf("right %d %d\n", r, c);
        cnt++;
      } else {
        return -1;
      }
    }
  }

  return cnt;
}

int main() {
    int caseN;
    scanf("%d", &caseN);

    for (int cc = 1; cc <= caseN; ++cc) {
        printf("Case #%d: ", cc);

        cin >> R >> C;
        for (int i = 0; i < R; ++i) {
          scanf("%s", board[i]);
          //cout << board[i] << endl;
        }
        int cnt = count();
        if (cnt == -1) {
          cout << "IMPOSSIBLE";
        } else {
          cout << cnt;
        }

        printf("\n");
    }

    return 0;
}
