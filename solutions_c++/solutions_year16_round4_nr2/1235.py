#include <bits/stdc++.h>
using namespace std;

#define st first
#define nd second
#define mp make_pair
#define pb push_back
#define cl(x, v) memset((x), (v), sizeof(x))

#define db(x) cerr << #x << " == " << x << endl
#define dbs(x) cerr << x << endl
#define _ << ", " <<

typedef long long ll;
typedef long double ld;

typedef pair<int, int> pii;
typedef pair<int, pii> piii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;

const int INF = 0x3f3f3f3f, MOD = 1e9+7, EPS = 1e-6;
const int N = 1e5+5;

int t, n, k;
ld p[300];

int main() {
  scanf("%d", &t);
  for (int tt = 1; tt <= t; ++tt) {
    scanf("%d%d", &n, &k);
    for (int i = 0; i < n; ++i) scanf("%Lf", &p[i]);

    string s;
    s.append(n-k, 0); s.append(k, 1);

    ld ma = 0;
    do {
      ld prob = 0;

      string ps;
      ps.append(k/2, 0); ps.append(k/2, 1);

      do {
        int x = 0;
        ld cp = 1;
        for (int i = 0; i < n; ++i) if (s[i]) cp *= ps[x++]?p[i]:1-p[i];
        prob += cp;
      } while (next_permutation(ps.begin(), ps.end()));
      ma = max(ma, prob);
    } while (next_permutation(s.begin(), s.end()));

    printf("Case #%d: %.8f\n",tt, (double)ma);
  }
  return 0;
}
