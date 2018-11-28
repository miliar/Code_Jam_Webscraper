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

int t;
double c, f, x, sol;
pair<double, double> a[2000000];

int main() {
   ios::sync_with_stdio(false);

   //freopen("in.txt", "r", stdin);
   //freopen("out.txt", "w", stdout);

   cin >> t;

   cout << fixed << setprecision(7);

   for (int i = 1; i <= t; i++) {
      cin >> c >> f >> x;

      a[0].x = c / 2.0;
      a[0].y = x / 2.0;

      for (int j = 0, b = 0; j < 2000000; j++) {
         a[j].x = a[j - 1].x + c / (2 + f * j);
         a[j].y = a[j - 1].x + x / (2 + f * j);
         if (a[j].y < a[b].y) b = j;
         if (a[j].x >= a[b].y) {
            cout << "Case #" << i << ": " << a[b].y << endl;
            break;
         }
      }
   }

   return 0;
}
