#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
  int T;
  cin >> T;
  for (int ca = 1; ca <= T; ++ca) {
    int n;
    cin >> n;
    vector<pair<int, bool> > a(n);
    for (int i = 0; i < n; ++i) {
      cin >> a[i].first;
      a[i].second = false;
    }
    
    int ans = 0, left = 0, right = n-1;
    for (int i = 0; i < n; ++i) {
      int mnind = -1;
      for (int j = 0; j < n; ++j) if (!a[j].second) {
        if (mnind == -1 || a[j].first < a[mnind].first) {
          mnind = j;
        }
      }
      a[mnind].second = true;
      if (mnind-left < right-mnind) {
        for (int j = mnind; j > left; --j) {
          swap(a[j-1], a[j]);
          ++ans;
        }
        ++left;
      }
      else {
        for (int j = mnind; j < right; ++j) {
          swap(a[j], a[j+1]);
          ++ans;
        }
        --right;
      }
    }
    
    cout << "Case #" << ca << ": " << ans << endl;
  }
}

