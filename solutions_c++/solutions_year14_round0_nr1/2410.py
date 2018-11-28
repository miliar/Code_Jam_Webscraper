/** 
 *
 * rais.fathin38
 */

#include <cstdio>
#include <cstring>
#include <cmath>
#include <cassert>
#include <cstdlib>
#include <cctype>
#include <ctime>

#include <iostream>
#include <iomanip>
#include <sstream>
#include <numeric>
#include <utility>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <list>
#include <bitset>
#include <complex>

using namespace std;

#define ALL(a) a.begin(), a.end()
#define SZ(a) ((int)a.size())

#define MIN(a, b) a = min(a, b)
#define MAX(a, b) a = max(a, b)

#define SHOW(x) { cerr << ">>> " << #x << " : " << x << endl; }

#define pb push_back
#define mp make_pair
#define fi first
#define se second

typedef long long LL;
typedef pair<int, int> pii;

int cnt[20];

int main() {
  int T; scanf("%d", &T);
  for (int t = 1; t <= T; t++) {
    int row, tmp;
    scanf("%d", &row); row--;
    memset(cnt, 0, sizeof(cnt));
    for (int i = 0; i < 4; i++) {
      for (int j = 0; j < 4; j++) {
        scanf("%d", &tmp);
        if (i == row) cnt[tmp]++;
      }
    }
    scanf("%d", &row); row--;
    for (int i = 0; i < 4; i++) {
      for (int j = 0; j < 4; j++) {
        scanf("%d", &tmp);
        if (i == row) cnt[tmp]++;
      }
    }
    int ans = -1, tot = 0;
    for (int i = 0; i < 20; i++) {
      if (cnt[i] == 2) {
        ans = i;
        tot++;
      }
    }
    if (tot == 0) printf("Case #%d: Volunteer cheated!\n", t);
    else if (tot == 1) printf("Case #%d: %d\n", t, ans);
    else printf("Case #%d: Bad magician!\n", t);
  }
  return 0;
}

