#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <queue>
#include <algorithm>
#include <iomanip>
#include <map>
#include <set>
#include <math.h>
#include <stack>
#include <deque>
#include <numeric>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <bitset>
#include <functional>

#define all(x) x.begin(),x.end()
#define mpair make_pair
using namespace std;
typedef long long ll;
typedef long double ld;
const ld epsylon = 1e-9;
int main() {
  freopen("google.in", "r", stdin);
  freopen("google.out", "w", stdout);
  int nt;
  cin >> nt;
  for (int it = 1; it <= nt; it++) {
    int n, x;
    cin >> n >> x;
    vector<int> a;
    for (int i = 0; i < n;++i){
      int temp;
      cin >> temp;
      a.push_back(temp);
    }
    sort(all(a));
    multiset<int> s;
    int ans = 0;
    for (int i = (int)a.size() - 1; i >= 0 ; --i) {
      multiset<int>::iterator it = s.lower_bound(a[i]);

      if (it == s.end()) {
        if ( x - a[i] > 0) {
          s.insert(x - a[i]);
        }
        ans++;
      } else {
        s.erase(it);
      }
    }
    cout << "Case #" << it << ": " << ans << endl;
  }
  return 0;
}
