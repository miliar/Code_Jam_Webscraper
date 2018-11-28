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

int t, a, b, k, sol;

int main() {
   ios::sync_with_stdio(false);

   freopen("in.txt", "r", stdin);
   freopen("out.txt", "w", stdout);

   cin >> t;

   for (int i = 1; i <= t; i++) {
      cin >> a >> b >> k;
      sol = 0;
      for (int j = 0; j < a; j++) {
         for (int q = 0; q < b; q++) {
            if ((j & q) < k) {
               sol++;
            }
         }
      }
      cout << "Case #" << i << ": " << sol << endl;
   }

   return 0;
}
