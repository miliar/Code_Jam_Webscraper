#include <bits/stdc++.h>
#define pb push_back
#define REP(i,n) for (int i=0; i<(int)(n); ++i)
#define ALL(x) x.begin(), x.end()
#define chmax(a, b) a = max(a, b)
#define chmin(a, b) a = min(a, b)

using namespace std;

typedef pair<char, char> pcc;
typedef long long ll;
typedef long double ld;
const int INF = 1 << 29;

int L, X;
vector<vector<int> > table = {
  {0, 1, 2, 3},
  {1, 4, 3, 6},
  {2, 7, 4, 1},
  {3, 2, 5, 4}
};

int f(int crt, char c) {
  int t = 3;
  if (c == 'i') t = 1;
  if (c == 'j') t = 2;
  int minus = ((crt >= 4) + (table[crt % 4][t] >= 4)) % 2 == 1;
  return 4 * minus + table[crt % 4][t] % 4;
}

int main(void) {
  int TestCase, TC = 0;
  cin >> TestCase;
  while(TestCase != TC) {
    cout << "Case #" << ++TC << ": ";
    cin >> L >> X;
    string tmp, s; cin >> tmp;
    REP(i, X) s += tmp;
    int cmp = 0, crt = 0;
    REP(i, L * X) {
      crt = f(crt, s[i]);
      if (cmp == 0 && crt % 4 == 1) { crt -= 1; cmp++; }
      if (cmp == 1 && crt % 4 == 2) { crt -= 2; cmp++; }
      if (cmp == 2 && crt % 4 == 3) { crt -= 3; cmp++; }
    }
    if (cmp == 3 && crt == 0) cout << "YES" << endl;
    else cout << "NO" << endl;
  }
  return 0;
}
