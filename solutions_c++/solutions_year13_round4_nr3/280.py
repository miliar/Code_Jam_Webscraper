#include <cstdio>
#include <cassert>
#include <algorithm>
#include <vector>

using namespace std;

const int maxN = 2000;

int n;
int a[maxN], b[maxN], res[maxN];
int ta[maxN][maxN], tb[maxN][maxN];
vector <int> ans;

void search (int i) {
  if (i == n) {
    vector <int> cur;
    for (int i = 0; i < n; ++i) {
      cur.push_back (res[i]);
    }
    if (ans.size () == 0 || ans > cur) {
      ans = cur;
    }
  }
//  fprintf (stderr, "i=%d\n", i);
  for (int j = 0; j < n; ++j) {
    ta[i][j] = (j > 0) ? ta[i][j - 1] : 0;
    if (res[j] != -1) {
      ta[i][j] = max (a[j], ta[i][j]);
    }
  }
  for (int j = n - 1; j >= 0; --j) {
    tb[i][j] = (j < n - 1) ? tb[i][j + 1] : 0;
    if (res[j] != -1) {
      tb[i][j] = max (b[j], tb[i][j]);
    }
  }
  int pos = -1;
  for (int j = 0; j < n; ++j) {
//    fprintf (stderr, "j=%d ta[i][j]=%d tb[i][j]=%d a[j]=%d b[j]=%d\n", j, ta[i][j], tb[i][j], a[j], b[j]);
    if (res[j] == -1 && 1 + ta[i][j] == a[j] && 1 + tb[i][j] == b[j]) {
      res[j] = i;
//      fprintf (stderr, "i=%d pos=%d\n", i, j);
      search (i + 1);
      res[j] = -1;
    }
  }
  return;
}

int main () {
  int nt;
  assert (scanf ("%d", &nt) == 1);
  for (int tt = 1; tt <= nt; ++tt) {
//    fprintf (stderr, "=== tt=%d\n", tt);
    assert (scanf ("%d", &n) == 1);
    for (int i = 0; i < n; ++i) {
      assert (scanf ("%d", &a[i]) == 1);
    }
    for (int i = 0; i < n; ++i) {
      assert (scanf ("%d", &b[i]) == 1);
    }
    for (int i = 0; i < n; ++i) {
      res[i] = -1;
    }
    ans = vector <int> ();
    search (0);
    printf ("Case #%d:", tt);
    for (int i = 0; i < n; ++i) {
      printf (" %d", 1 + ans[i]);
    }
    printf ("\n");
  }
  return 0;
}
