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

int t, n, r, p, s;

int main() {
  scanf("%d", &t);
  for (int tt = 1; tt <= t; ++tt) {
    printf("Case #%d: ", tt);

    scanf("%d%d%d%d", &n, &r, &p, &s);
    string st;
    for (int i = 0; i < p; ++i) st+='P';
    for (int i = 0; i < r; ++i) st+='R';
    for (int i = 0; i < s; ++i) st+='S';

    int found = 0;
    do {
      string ns = st;
      int ok = 1;
      for (int i = 0; i < n and ok; ++i) {
        for (int j = 0; j < (1<<n) and ok; j+=(1<<(i+1))) {
          if (ns[j] == ns[j+(1<<i)]) ok = 0;
          else {
            char c0 = min(ns[j], ns[j+(1<<i)]),
                 c1 = max(ns[j], ns[j+(1<<i)]);
            if (c0 == 'P' and c1 == 'R') ns[j] = 'P';
            if (c0 == 'P' and c1 == 'S') ns[j] = 'S';
            if (c0 == 'R' and c1 == 'S') ns[j] = 'R';
          }
        }
      }
      if (ok) { found = 1; break; }
    } while (next_permutation(st.begin(), st.end()));

    printf("%s\n", found?st.c_str():"IMPOSSIBLE");
  }
  return 0;
}
