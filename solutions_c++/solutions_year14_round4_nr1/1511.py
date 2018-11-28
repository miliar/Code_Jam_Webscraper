#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
  int ncases;
  cin >> ncases;
  for (int ncase = 1; ncase <= ncases; ++ncase) {
    int n, x;
    cin >> n >> x;
    int a;
    vector<int> v;
    while (n-- && cin >> a) {
      v.push_back(a);
    }
    sort(v.begin(), v.end());
    
    int i = 0, j = v.size() - 1;
    int ans = 0;
    while (i < j) {
      if (v[j] + v[i] <= x) {
	++i, --j;
      } else {
	--j;
      }
      ++ans;
    }
    if (i == j) {
      ++ans;
    }

    cout << "Case #" << ncase << ": " << ans << endl;
  }
}
