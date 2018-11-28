#include <iostream>
#include <iomanip>
#include <stdio.h>
#include <set>
#include <vector>
#include <map>
#include <cmath>
#include <algorithm>
#include <memory.h>
#include <string>
#include <sstream>
#include <queue>
#include <set>
using namespace std;
typedef long long ll;

const int N = 128;
int a[N][N];

int main()
{
#ifdef _ZZZ_
  freopen("in.txt","r",stdin);
  freopen("out.txt","w",stdout);
#endif
  int T;
  cin >> T;
  for(int tt = 1; tt <= T; ++ tt) {
    int n, m;
    cin >> n >> m;
    for(int i = 1; i <= n; ++ i) {
      for(int j = 1; j <= m; ++ j) {
        cin >> a[i][j];
      }
    }
    int maxr[N] = {0}, maxc[N] = {0};
    for(int i = 1; i <= n; ++ i) {
      for(int j = 1; j <= m; ++ j) {
        maxr[i] = max(maxr[i], a[i][j]);
        maxc[j] = max(maxc[j], a[i][j]);
      }
    }
    bool yes = true;
    for(int i = 1; yes && i <= n; ++ i) {
      for(int j = 1; j <= m; ++ j) {
        if (a[i][j] == maxr[i] || a[i][j] == maxc[j]) {
        } else {
          yes = false;
          break;
        }
      }
    }
    printf("Case #%d: %s\n", tt, yes ? "YES" : "NO");

  }

  return 0;
}










