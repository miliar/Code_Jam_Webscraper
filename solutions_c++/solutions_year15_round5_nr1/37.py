/**
 * Author: Sergey Kopeliovich (Burunduk30@gmail.com)
 */

#include <bits/stdc++.h>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)

typedef long long ll;

const int N = 1e6 + 10;

int en, n, D, s[N], m[N], sum[N], is[N];
int as, cs, rs, am, cm, rm;
pair<int,int> e[2 * N];

void solve() {
  cin >> n >> D;
  cin >> s[0] >> as >> cs >> rs;
  cin >> m[0] >> am >> cm >> rm;
  forn(i, n - 1) {
    s[i + 1] = ((ll)s[i] * as + cs) % rs;
    m[i + 1] = ((ll)m[i] * am + cm) % rm;
  }                                   
  for (int i = 1; i < n; i++)
    m[i] %= i;
  en = 0;
  forn(i, n) {
    sum[i] = 0, is[i] = 0;
    e[en++] = {s[i], -(i + 1)};
    e[en++] = {s[i] + D, (i + 1)};
  }
  sort(e, e + en);
 
  int res = 1;
  forn(j, en) {
    if (e[j].second < 0) { // add
      int i = -e[j].second - 1;
      sum[i]++, is[i] = 1;
      int add = sum[i];
      while (i && is[i])
        sum[i = m[i]] += add;
    } else {
      int i = e[j].second - 1;
      int add = sum[i];
      sum[i]--, is[i] = 0;
      while (i) {
        i = m[i];
        sum[i] -= add;
        if (!i || !is[i])
          break;
      }
    }
    if (is[0])
      res = max(res, sum[0]);
  }
  printf("%d\n", res);
}

int main() {
  int tn;
  scanf("%d", &tn);
  forn(t, tn) {
    printf("Case #%d: ", t + 1);
    solve();
  }
  return 0;
}

