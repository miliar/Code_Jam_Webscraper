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

int t, n;
string strs[105];
int positions[105];
int counts[105];

int main() {
   ios::sync_with_stdio(false);

   freopen("in.txt", "r", stdin);
   freopen("out.txt", "w", stdout);

   cin >> t;

   for (int i = 1; i <= t; i++) {
      cin >> n;
      for (int j = 0; j < n; j++) {
         cin >> strs[j];
         positions[j] = 0;
      }
      cout << "Case #" << i << ": ";
      int sol = 0;
      bool b = true;
      while (true) {
         if (!b) break;
         if (positions[0] == strs[0].length()) {
            for (int j = 1; j < n; j++) {
               if (positions[j] < strs[j].length()) {
                  cout << "Fegla Won" << endl;
                  b = false;
                  break;
               }
            }
            break;
         }
         char c = strs[0][positions[0]];
         int total = 0;
         for (int j = 0; j < n; j++) {
            int k = positions[j];
            for (; strs[j][k] == c; k++) {

            }
            if (k - positions[j] == 0) {
               cout << "Fegla Won" << endl;
               b = false;
            } else {
               counts[j] = k - positions[j];
               total += counts[j];
               positions[j] = k;
            }
         }
         int av = (int)round((double)total / n);
         for (int j = 0; j < n; j++) {
            sol += abs(counts[j] - av);
         }
      }
      if (b) cout << sol << endl;
   }

   return 0;
}
