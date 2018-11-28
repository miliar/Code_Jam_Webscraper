#include<bits/stdc++.h>
using namespace std;

#define PB                      push_back
#define MP                      make_pair
#define ALL(v)                  v.begin(),v.end()
#define SZ(v)					(int)v.size()
#define CLR(v, d)               memset(v, d, sizeof(v))

const int OO = (int) 2e9;
const double EPS = 1e-9;

int main() {
  freopen("in.txt", "rt", stdin);
  freopen("out.txt", "wt", stdout);

  int t, a, b, k;
  cin >> t;
  for (int tt = 0; tt < t; tt++) {
    cin >> a >> b >> k;
    int ans = 0;
    for (int i = 0; i < a; i++)
    for (int j = 0; j < b; j++)
    if ((i & j) < k)
    ans++;
    printf("Case #%d: %d\n", tt + 1, ans);

  }
  return 0;
}
