#include <string>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <climits>
#include <algorithm>
#include <complex>
#include <cmath>
#include <cstdlib>
using namespace std;

#define pb push_back 
#define mp make_pair 
#define repn(i, n) for(int i = 0; i < (n); i++)

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef set<int> si;
typedef map<int, int> mii;
typedef vector<vi> vvi;
typedef map<int, mii> mimii;
typedef map<int, si> misi;
typedef map<int, pii> mipii;
typedef vector<pii> vpii;
typedef map<int, vi> mivi;


int n, m;
vi xs;

int main(int argc, char **argv) {
  int tc;
  cin >> tc;
  repn(ti, tc) {
    xs.clear();
    cin >> n;
    for (int i = 0; i < n; i++)
    {
      int t;
      cin >> t;
      xs.pb(t);
    }

    int u = 0, v = n;
    int c = 0;
    for (int i = 0; i < n; i++)
    {
      auto zt = min_element(xs.begin() + u, xs.begin() + v);
      int mz = *zt;
      int z = zt - xs.begin();
      int du = z - u;
      int dv = v - z - 1;
      if (du <= dv)
      {
        xs.erase(xs.begin() + z);
        xs.insert(xs.begin() + u, mz);
        u++;
        c += du;
      } else {
        xs.erase(xs.begin() + z);
        xs.insert(xs.begin() + v - 1, mz);
        v--;
        c += dv;
      }
    }
    printf("Case #%d: %d\n", ti + 1, c);
  }
  return 0;
}
