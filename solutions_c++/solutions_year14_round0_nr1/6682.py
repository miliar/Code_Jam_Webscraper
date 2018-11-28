// includes, defines, typedefs //{

#include <functional>
#include <algorithm>
#include <limits.h>
#include <iostream>
#include <string.h>
#include <iomanip>
#include <fstream>
#include <bitset>
#include <time.h>
#include <vector>
#include <cmath>
#include <deque>
#include <queue>
#include <list>
#include <set>
#include <map>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<pll> vpll;
typedef vector<pii> vpii;
typedef vector<int> vi;
typedef vector<ll> vll;

#define endl '\n'
#define mp(a, b) make_pair((a), (b))
#define pb(a) push_back(a)
#define gi greater<int>()
#define gip greater<ip>()
#define y second
#define x first

//}

int t, n, m, a[4][4], b[4][4];

int main() {
   ios::sync_with_stdio(false);

   freopen("in.txt", "r", stdin);
   freopen("out.txt", "w", stdout);

   cin >> t;

   for (int i = 1; i <= t; i++) {
      cin >> n; n--;
      for (int j = 0; j < 4; j++) {
         for (int k = 0; k < 4; k++) {
            cin >> a[j][k];
         }
      }
      cin >> m; m--;
      for (int j = 0; j < 4; j++) {
         for (int k = 0; k < 4; k++) {
            cin >> b[j][k];
         }
      }
      int s = 0;
      for (int j = 0; j < 4; j++) {
         for (int k = 0; k < 4; k++) {
            if (a[n][j] == b[m][k]) {
               if (s == 0) s = a[n][j];
               else if (s > 0) s = -1;
            }
         }
      }
      if (s < 0) cout << "Case #" << i << ": Bad magician!" << endl;
      else if (s == 0) cout << "Case #" << i << ": Volunteer cheated!" << endl;
      else cout << "Case #" << i << ": " << s << endl;
   }

   return 0;
}
