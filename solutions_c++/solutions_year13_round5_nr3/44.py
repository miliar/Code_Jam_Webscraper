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

int u[2005], v[2005], mi[2005], ma[2005], r[2005], l[2005];
int d[2005];
int d2[2005];
int m, n;
int min_len;
int mark[2005];

bool check (int x) {
//  cerr << "x = " << x << " " << min_len << endl;
  if (x == 1) {
//    for (int j = 0; j < m; j++) {
//      cerr << l[j] << " ";
//    }
//    cerr << endl;

    for (int i = 0; i < n; i++) {
      d2[i] = 2000000000;
    }
    d2[1] = 0;
    for (int i = 0; i < n; i++)
      for (int j = 0; j < m; j++) {
        if (d2[u[j]] > d2[v[j]] + l[j]) {
          d2[u[j]] = d2[v[j]] + l[j];
        }
      }
//    cerr << "d2[0] = " << d2[0] << endl;
    return d2[0] >= min_len;
  }

  mark[x] = 1;
  for (int i = 0; i < m; i++) {
    if (u[i] == x && !mark[v[i]]) {
      int tmp = l[i];
      l[i] = mi[i];
      if (check (v[i])) {
        return 1;
      }
      l[i] = tmp;
    }
  }
  mark[x] = 0;
  return 0;
}

bool check2 (int v, int len) {
  min_len = len + d[v];
  return check (v);
}

int main (void) {
  int tn, nt;
  scanf ("%d", &nt);
  for (tn = 1; tn <= nt; tn++) {
    printf ("Case #%d: ", tn);
    fprintf (stderr, "Case #%d: \n", tn);

    int p;
    scanf ("%d %d %d", &n, &m, &p);
    for (int i = 0; i < m; i++) {
      scanf ("%d %d %d %d", &u[i], &v[i], &mi[i], &ma[i]);
      u[i]--, v[i]--;
    }
    for (int i = 0; i < p; i++) {
      scanf ("%d", &r[i]);
      r[i]--;
    }

    for (int i = 0; i < m; i++) {
      l[i] = mi[i];
    }
    for (int i = 0; i < n; i++) {
      d[i] = 2000000000;
    }
    d[1] = 0;
    for (int i = 0; i < n; i++)
      for (int j = 0; j < m; j++) {
        if (d[u[j]] > d[v[j]] + l[j]) {
          d[u[j]] = d[v[j]] + l[j];
        }
      }

    int ans;
    for (ans = p; ans >= 0; ans--) {
      for (int j = 0; j < m; j++) {
        l[j] = ma[j];
      }
      int len = 0;
      for (int j = 0; j < n; j++) {
        mark[j] = 0;
      }
      for (int j = 0; j < ans; j++) {
        l[r[j]] = mi[r[j]];
        len += mi[r[j]];
      }

      if (check2 (ans == p ? 1 : u[r[ans]], len)) {
        break;
      }
    }
    if (ans == p) {
      puts ("Looks Good To Me");
    } else {
      printf ("%d\n", r[ans] + 1);
    }
  }

  return 0;
}
