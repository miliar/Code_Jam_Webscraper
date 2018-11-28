#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <iostream>
#include <string>
using namespace std;

int r[13][3], p[13][3], s[13][3];
char ans[81920];

// void make2(int l, int r, char x) {
//   if (l == r - 1) {
//     ans[l] = x;
//     return;
//   }
//   int mid = (l+r)/2;
//   if (x == 'R') {
//     if (mid == l + 1) {
//       make2(l, mid, 'R');
//       make2(mid, r, 'S');
//     } else {
//       make2(l, mid, 'S');
//       make(mid, r, 'P');
//     }
//   } else if (x == 'P') {
//     make(l, mid, 'P');
//     make(mid, r, 'R');
//   } else if (x == 'S') {
//     make(l, mid, 'P');
//     make(mid, r, 'S');
//   } 
// }

string make(int l, int r, char x) {
  if (l == r - 1) {
    if (x == 'R') return "R";
    if (x == 'S') return "S";
    if (x == 'P') return "P";
  }
  int mid = (l+r)/2;
  if (x == 'R') {
    string ll = make(l, mid, 'R');
    string rr = make(mid, r, 'S');
    if (ll < rr) return ll+rr;
    else return rr + ll;
  } else if (x == 'P') {
    string ll = make(l, mid, 'P');
    string rr = make(mid, r, 'R');
    if (ll < rr) return ll+rr;
    else return rr + ll;
    // make(l, mid, 'P');
    // make(mid, r, 'R');
  } else if (x == 'S') {
    string ll = make(l, mid, 'P');
    string rr = make(mid, r, 'S');
    if (ll < rr) return ll+rr;
    else return rr + ll;
    // make(l, mid, 'P');
    // make(mid, r, 'S');
  } 
}

int main() {
  int T, tmp, N, R, P, S;
  scanf("%d", &T);
  memset(r, sizeof(r), 0);
  memset(p, sizeof(p), 0);
  memset(s, sizeof(s), 0);
  r[0][0] = 1;
  p[0][1] = 1;
  s[0][2] = 1;
  for (int i = 1; i < 13; ++i) {
    for (int j = 0; j < 3; ++j) {
      r[i][j] = r[i-1][j] + s[i-1][j];
    }
    for (int j = 0; j < 3; ++j) {
      p[i][j] = p[i-1][j] + r[i-1][j];
    }
    for (int j = 0; j < 3; ++j) {
      s[i][j] = p[i-1][j] + s[i-1][j];
    }
  }

  for (int I = 1; I <= T; ++I) {
    scanf("%d%d%d%d", &N, &R, &P, &S);
    printf("Case #%d: ", I);
    if (R == p[N][0] && P == p[N][1] && S == p[N][2]) {
      string tmp = make(0, 1<<N, 'P');
      printf("%s", tmp.c_str());

      // make2(0, 1<<N, 'P');
      // for (int i = 0; i < (1<<N); ++i) printf("%c", ans[i]);
    } else if (R == r[N][0] && P == r[N][1] && S == r[N][2]) {
      string tmp = make(0, 1<<N, 'R');
      printf("%s", tmp.c_str());

      // make2(0, 1<<N, 'R');
      // for (int i = 0; i < (1<<N); ++i) printf("%c", ans[i]);
    } else if (R == s[N][0] && P == s[N][1] && S == s[N][2]) {
      string tmp = make(0, 1<<N, 'S');
      printf("%s", tmp.c_str());

      // make2(0, 1<<N, 'S');
      // for (int i = 0; i < (1<<N); ++i) printf("%c", ans[i]);
    } else {
      printf("IMPOSSIBLE");
    }
    printf("\n");
  }
}
