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
    int n;
    cin >> n;
    Vi v(n);
    for (int i = 0; i < n; ++i) cin >> v[i];
    int res = 0;
    for (int i = 0; i < n; ++i) {
      int a = 0, b = 0;
      for (int j = 0; j < i; ++j)
        if (v[j] > v[i]) ++a;
      for (int j = i + 1; j < n; ++j)
        if (v[j] > v[i]) ++b;
      res += min(a, b);
    }
    cout << "Case #" << cas << ": " << res << endl;
  }
}
