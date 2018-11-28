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
int sign(int a) {
  if (a < 0) return -1;
  return 1;
}
int mul[5][5] = {
  {0},
  {0, 1, 2, 3, 4},
  {0, 2,-1, 4,-3},
  {0, 3,-4,-1, 2},
  {0, 4, 3,-2,-1}
};
int multi(int a, int b) {
  if (sign(a) != sign(b))
    return -mul[abs(a)][abs(b)];
  return mul[abs(a)][abs(b)];
}
bool K[10010];
int vec[10010];
int n;
char s[10010];
char to[256];

bool solve() {
  if (n < 3) return false;
  int cur = 1;
  for (int i = n - 1; i >= 0; i--) {
    cur = multi(vec[i], cur);
    K[i] = (cur==4);
  }
  int I = 1, J;
  for (int i = 0; i < (n - 2); i++) {
    I = multi(I, vec[i]);
    if (I == 2) {
      J = 1;
      for (int j = i + 1; j < (n - 1); j++) {
	J = multi(J, vec[j]);
	if (J == 3 && K[j + 1])
	  return true;
      }
    }
  }
  return false;
}
int main() {
  to['i'] = 2;
  to['j'] = 3;
  to['k'] = 4;
  int t;
  scanf("%d", &t);
  for (int caso = 1; caso <= t; caso++) {
    int l, copies;
    scanf("%d %d", &l, &copies);
    scanf("%s", s);
    n = l * copies;
    int pos = 0;
    while (copies--) {
      forn (i, l)
	vec[pos++] = to[s[i]];
    }
    printf("Case #%d: %s\n", caso, solve()?"YES":"NO");
    DBG(caso);
  }
  return 0;
}
