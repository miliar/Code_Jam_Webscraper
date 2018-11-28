#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <utility>
#include <vector>
using namespace std;

typedef long long ll;
typedef pair<int, int> P;
typedef vector<P> Vp;
typedef vector<int> Vi;
typedef vector<Vi> Mi;

const int INF = 1000000000;

int main() {
  int tcas;
  cin >> tcas;
  for (int cas = 1; cas <= tcas; ++cas) {
    int n, m;
    cin >> n >> m;
    Vi v(n);
    for (int i = 0; i < n; ++i) cin >> v[i];
    sort(v.begin(), v.end());
    int res = 0;
    int j = 0;
    for (int i = n - 1; i >= j; --i) {
      ++res;
      if (j < i and v[j] + v[i] <= m) ++j;
    }
    cout << "Case #" << cas << ": " << res << endl;
  }
}
