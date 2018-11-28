#include <cmath>
#include <functional>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <unordered_map>
#include <queue>
#include <set>
using namespace std;

#define FOR(i,a,b) for (int i = (a); i < (b); ++i)
#define REP(i,n) FOR(i,0,n)

int n,m,x;
char a[200][200];

void print() {
  a[n-1][m-1] = 'c';
  REP(i,n) {
    REP(j,m) {
      putchar(a[i][j]);
    }
    puts("");
  }
}

void bad() {
  puts("Impossible");
}

int main() {
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);

  int T;
  cin >> T;
  REP(tests,T) {
    cout << "Case #" << tests + 1 << ":" << endl;
    cin >> n >> m >> x;
    REP(i,n) {
      REP(j,m) {
        a[i][j] = '.';
      }
    }
    if (x == 0) {
      print();
      continue;
    }
    if (x == n*m-1) {
      REP(i,n) {
        REP(j,m) {
          a[i][j] = '*';
        }
      }
      print();
      continue;
    }
    if (min(n,m) == 1) {
      REP(i,n) {
        REP(j,m) {
          if (i*m + j < x) {
            a[i][j] = '*';
          }
        }
      }
      print();
      continue;
    }
    if (x == n*m - 2) {
      bad();
      continue;
    }
    if (min(n,m) == 2) {
      if (x%2 == 1) {
        bad();
        continue;
      }
      if (n == 2) {
        REP(i,n) {
          REP(j,x/2) {
            a[i][j] = '*';
          }
        }
      } else {
        REP(i,x/2) {
          REP(j,m) {
            a[i][j] = '*';
          }
        }
      }
      print();
      continue;
    }
    REP(i,n-2) {
      REP(j,m-2) {
        if (x > 0) {
          a[i][j] = '*';
          --x;
        }
      }
    }
    if (x == 0) {
      print();
      continue;
    }
    int sz;
    if (x % 2 == 0) {
      sz = 2;
    } else {
      sz = 3;
      a[n-3][m-3] = '.';
      ++x;
    }
    REP(i,n-sz) {
      if (x > 0) {
        x -= 2;
        a[i][m-2] = '*';
        a[i][m-1] = '*';
      }
    }
    REP(i,m-sz) {
      if (x > 0) {
        x -= 2;
        a[n-1][i] = '*';
        a[n-2][i] = '*';
      }
    }
    if (x > 0) {
      bad();
    } else {
      print();
    }
  }
  return 0;
}