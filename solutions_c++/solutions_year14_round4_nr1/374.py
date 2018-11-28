#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cmath>
#include <fstream>
using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef vector<PII> VPII;

int main() {
  ios::sync_with_stdio(false);
  int t; cin >> t;
  for (int z = 0; z < t; ++z) {
    int n, x;
    cin >> n >> x;
    multiset<int> s;
    for (int i = 0; i < n; ++i) {
      int size;
      cin >> size;
      s.insert(size);
    }
    int res = 0;
    while (not s.empty()) {
      int min = *(s.begin());
      s.erase(s.begin());
      set<int>::iterator it = s.upper_bound(x - min);
      if (it != s.begin()) {
        --it;
        s.erase(it);
        ++res;
      }
      else {
        s.insert(min);
        break;
      }
    }
    cout << "Case #" << z + 1 << ": " << res + s.size() << endl;
  }
}