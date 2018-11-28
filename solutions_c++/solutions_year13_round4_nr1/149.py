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

pair <pair <long long, long long>, long long> a[1005];

map <long long, int> ma;
long long inv[2005];

long long cnt[2005];

long long mod = 1000002013;

long long get (int l, int r) {
  if (l >= r) {
    return 0;
  }
  int mi = l;
  for (int i = l; i < r; i++) {
    if (cnt[i] < cnt[mi]) {
      mi = i;
    }
  }

  long long size = cnt[mi];
  for (int j = l; j < r; j++)
    cnt[j] -= size;
  size %= mod;

  long long len = inv[r] - inv[l];
  long long res = (len * (len - 1) / 2) % mod;
  res = (res * size) % mod;
  return (get (l, mi) + get (mi + 1, r) + res) % mod;
}

int main (void) {
  int tn, nt;
  scanf ("%d", &nt);
  for (tn = 1; tn <= nt; tn++) {
    printf ("Case #%d: ", tn);
    fprintf (stderr, "Case #%d: \n", tn);

    long long n;
    int m;
    cin >> n >> m;

    set <long long> s;
    long long res = 0;
    for (int i = 0; i < m; i++) {
      cin >> a[i].first.first >> a[i].first.second >> a[i].second;
      s.insert (a[i].first.first);
      s.insert (a[i].first.second);
      long long l = a[i].first.second - a[i].first.first;
      res = (res - (((l * (l - 1) / 2) % mod) * a[i].second) % mod) % mod;
    }
    memset (cnt, 0, sizeof (cnt));
    n = 0;
    for (set <long long>::iterator p = s.begin(); p != s.end(); ++p) {
      inv[n] = *p;
      ma[*p] = n++;
    }
    assert (n == s.size());
    for (int i = 0; i < m; i++) {
      int l = ma[a[i].first.first];
      int r = ma[a[i].first.second];
      for (int j = l; j < r; j++)
        cnt[j] += a[i].second;
    }

    printf ("%d\n", (int)(((get (0, n - 1) + res) % mod + mod) % mod));
  }

  return 0;
}
