#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
#include <utility>

using namespace std;

int n;
int a[2005];
int b[2005];
int p[2005];

int ans[2005];

int gen (int x) {
/*  for (int i = 0; i < x; i++)
    cerr << p[i] << " ";
  cerr << endl;/**/

  if (x == n) {
//    cerr << "!";
    for (int i = n - 1; i >= 0; i--) {
      int res = 1;
      for (int j = i + 1; j < n; j++) {
        if (p[j] < p[i] && b[j] >= res) {
          res = b[j] + 1;
        }
      }
      if (res != b[i]) {
        return 0;
      }
    }
    int i;
    for (i = 0; i < n; i++) {
      if (p[i] != ans[i])
        break;
    }
    if (p[i] < ans[i]) {
      memcpy (ans, p, n * sizeof (int));
    }
    return 0;
  }

  int cnt[25];
  int pos[25];
//  int mi[25];
  for (int i = 0; i < x; i++) {
    cnt[p[i]] = a[i] + 1;
    pos[p[i]] = i;
  }
//  mi[x] = x + 1;
//  for (int i = x - 1; i >= 0; i--) {
//    mi[x] = min (mi[x + 1], cnt[i]);
//  }

  int cur = 1;
  for (int j = 0; j < x; j++) {
    p[j]++;
  }
  for (int i = 0; i <= x; i++) {
    if (cur == a[x]) {
      p[x] = i;
      int good = 1;
      for (int j = 0; j < x; j++) {
        if (p[j] > i && b[j] <= b[x]) {
          good = 0;
          break;
        }
      }
      if (good)
//      if (mi[i] >= b[x])
        gen (x + 1);
    }
    if (i < x) {
      p[pos[i]]--;

      if (cnt[i] > cur) {
        cur = cnt[i];
      }
    }
  }
/*  cerr << "out: ";
  for (int i = 0; i < x; i++)
    cerr << p[i] << " ";
  cerr << endl;/**/
  return 0;
}

int main (void) {
  int tn, nt;
  scanf ("%d", &nt);
  for (tn = 1; tn <= nt; tn++) {
    printf ("Case #%d: ", tn);
    fprintf (stderr, "Case #%d: \n", tn);

    cin >> n;
    for (int i = 0; i < n; i++)
      cin >> a[i];
    for (int i = 0; i < n; i++) {
      cin >> b[i];
      ans[i] = n + 1;
    }
/*
    n = 20;
    for (int i = 0; i < n; i++) {
      p[i] = i;
    }
    random_shuffle (p, p + n);

    for (int i = n - 1; i >= 0; i--) {
      int res = 1;
      for (int j = i + 1; j < n; j++) {
        if (p[j] < p[i] && b[j] >= res) {
          res = b[j] + 1;
        }
      }
      b[i] = res;
    }
    for (int i = 0; i < n; i++) {
      int res = 1;
      for (int j = 0; j < i; j++) {
        if (p[j] < p[i] && a[j] >= res) {
          res = a[j] + 1;
        }
      }
      a[i] = res;
      ans[i] = 21;
    }
    for (int i = 0; i < n; i++) {
      cerr << p[i] << " ";
    }
    cerr << endl;
    for (int i = 0; i < n; i++) {
      cerr << a[i] << " ";
    }
    cerr << endl;
    for (int i = 0; i < n; i++) {
      cerr << b[i] << " ";
    }
    cerr << endl;
*/
    gen (0);
    assert (ans[0] < n);
    for (int i = 0; i < n; i++) {
      cout << ans[i] + 1 << " ";
    }
    cout << endl;
  }

  return 0;
}
