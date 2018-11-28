#include <bits/stdc++.h>
using namespace std;
int n, c[3], b[3];
string ss, tt;
string test(int lv, int wanted) {
  if (c[0] > b[0] || c[1] > b[1] || c[2] > b[2]) return "";
  if (lv == n) {
    c[wanted]++;
    return wanted == 0 ? "R" : wanted == 1 ? "P" : "S";
  }
  if (wanted == 0) {
    string p = test(lv + 1, 0);
    string q = test(lv + 1, 2);
    return min(p + q, q + p);
  }
  if (wanted == 1) {
    string p = test(lv + 1, 1);
    string q = test(lv + 1, 0);
    return min(p + q, q + p);
  }
  if (wanted == 2) {
    string p = test(lv + 1, 2);
    string q = test(lv + 1, 1);
    return min(p + q, q + p);
  }
}

void solve() {
  scanf("%d %d %d %d", &n, &b[0], &b[1], &b[2]);
  ss = "X";
  c[0] = c[1] = c[2] = 0;
  tt = test(0, 0);
  if (b[0] == c[0] && b[1] == c[1] && b[2] == c[2]) {
    ss = min(ss, tt);
  }
  c[0] = c[1] = c[2] = 0;
  tt = test(0, 1);
  if (b[0] == c[0] && b[1] == c[1] && b[2] == c[2]) {
    ss = min(ss, tt);
  }
  c[0] = c[1] = c[2] = 0;
  tt = test(0, 2);
  if (b[0] == c[0] && b[1] == c[1] && b[2] == c[2]) {
    ss = min(ss, tt);
  }
  if (ss == "X") {
    cout << "IMPOSSIBLE";
  } else {
    cout << ss;
  }
}
int main() {
  int T;
  scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    printf("Case #%d: ", t);
    solve();
    printf("\n");
  }
  return 0;
}


