#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <string>
#include <vector>
#include <deque>
#include <map>
#include <set>

using namespace std;

#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#define pb push_back
#define mp make_pair
#define sz(x) ((int)(x).size())

typedef long long ll;

typedef vector<ll> vll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef pair<int, int> pii;

const int MAXN = 200;
char s[MAXN + 1];

void solve() {
  scanf("%s", s);
  int n = strlen(s);
  reverse(s, s + n);
  assert(n <= 20);

  vector<double> dyn(1 << n, 0), sumprob(1 << n, 0);
  int smsk = 0;
  for (int i = 0; i < n; i++)
    smsk <<= 1, smsk |= s[i] == 'X';
  dyn[smsk] = 0;
  sumprob[smsk] = 1;

  for (int m = smsk; m < (1 << n); m = (m + 1) | smsk) {
    assert(sumprob[m] > 1e-9);
//    eprintf("m=%d, %.2lf %.2lf\n", m, dyn[m], sumprob[m]);
    dyn[m] /= sumprob[m];
    if (m == (1 << n) - 1) break;

    int wait[n];
    memset(wait, 0x3f, sizeof wait);
    for (int step = 0; step < 2; step++)
    for (int i = n - 1; i >= 0; i--)
      if (!(m & (1 << i))) {
        wait[i] = 0;
      } else {
        int ne = i + 1 >= n ? 0 : i + 1;
        wait[i] = min(wait[i], wait[ne] + 1);
      }

    for (int i = 0; i < n; i++)
      assert(wait[i] < n);

    for (int i = 0; i < n; i++) {
      int ne = (i + wait[i]);
      if (ne >= n) ne -= n;

      int nm = m | (1 << ne);
      assert(m != nm);
      dyn[nm] += (dyn[m] + n - wait[i]) * sumprob[m] / n;
      sumprob[nm] += sumprob[m] / n;
    }
  }
//  eprintf("%.2lf\n", sumprob.back());
  printf("%.18lf\n", dyn.back());
}

bool endsWith(string a, string b) {
  return a.length() >= b.length() && string(a, a.length() - b.length()) == b;
}

int main(int argc, char *argv[]) {
  {
    string fn = "";
    if (argc >= 2) fn = argv[1];
    if (endsWith(fn, ".in")) fn = string(fn, 0, fn.length() - 3);
    freopen((fn + ".in").c_str(), "r", stdin);
    freopen((fn + ".out").c_str(), "w", stdout);
  }

  int TC;
  assert(scanf("%d", &TC) >= 1);
  for (int TN = 1; TN <= TC; TN++) {
    eprintf("Case #%d:\n", TN);
    printf("Case #%d: ", TN);
    try {
      solve();
    } catch (...) {
      eprintf("Catched exception at test case #%d\n", TN);
      return 1;
    }
  }
  return 0;
}
