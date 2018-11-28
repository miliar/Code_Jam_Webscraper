#include <bits/stdc++.h>

#define REP(i,n) for(int i=0;i<(int)(n);i++)
#define ALL(x) (x).begin(),(x).end()

using namespace std;

int main() {
  int T;
  cin >> T;
  REP(cas,T) {
    int x, r, c;
    cin >> x >> r >> c;
    bool flag = false;
    if (x == 1) flag = true;
    if (x == 2 && (r*c)%2 == 0) flag = true;
    if (x == 3) {
      if (min(r, c) >= 2 && (r*c)%3 == 0) flag = true;
    }
    if (x == 4) {
      if (max(r, c) >= 4 && min(r, c) >= 3 && (r*c)%4 == 0) flag = true;
    }
    if (x == 5) {
      if (max(r, c) >= 5 && min(r, c) >= 4 && (r*c)%5 == 0) flag = true;
    }
    if (x == 6) {
      if (max(r, c) >= 6 && min(r, c) >= 4 && (r*c)%6 == 0) flag = true;
    }
    if (flag) printf("Case #%d: GABRIEL\n", cas+1);
    else printf("Case #%d: RICHARD\n", cas+1);
  }
  return 0;
}
