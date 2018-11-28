#include <bits/stdc++.h>

using namespace std;

struct RTC{~RTC(){cerr << "Time: " << clock() * 1.0 / CLOCKS_PER_SEC <<" seconds\n";}} runtimecount;
#define DBG(X) cerr << #X << " = " << X << '\n';
#define mp make_pair
#define mt make_tuple
#define pb push_back
#define eb emplace_back
#define sz(x) ((int)(x).size())
#define all(c) (c).begin(),(c).end()
#define forn(i, n) for (int i = 0; i < (n); i++)
int lim;
int bruteforce(const vector<int> &v, int acu) {
  if (v.size() == 0) return 0;
  //La respuesta no puede ser mas grande que si nunca
  //hubieramos usado minutos especiales
  if (acu >= lim) return (1<<20);
  vector<int> op1, op2;
  int maxi = 0;
  forn (i, sz(v)) {
    if (v[i] > 1)
      op1.pb(v[i] - 1);
    if (v[i] > v[maxi])
      maxi = i;
  }
  if (v[maxi] == 1) return 1;
  int ans = 1 + bruteforce(op1, acu + 1);//Normal
  int mid = v[maxi] / 2;
  for (int i = 1; i <= mid; i++) {
    op2 = v;
    op2[maxi] -= i;
    op2.pb(i);
    ans = min(ans, 1 + bruteforce(op2, acu + 1));
  }
  return ans;
}
int main() {
  int t;
  scanf("%d", &t);
  for (int caso = 1; caso <= t; caso++) {
    int n;
    scanf("%d", &n);
    vector<int> v(n);
    lim = 1;
    forn (i, n) {
      scanf("%d", &v[i]);
      lim = max(lim, v[i]);
    }
    printf("Case #%d: %d\n", caso, min(lim, bruteforce(v, 0)));
    DBG(caso);
  }
  return 0;
}
