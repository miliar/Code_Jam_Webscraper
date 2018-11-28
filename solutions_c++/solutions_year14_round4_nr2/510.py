#include <iostream>
#include <algorithm>
#include <map>
using namespace std;

int a[1010];

int main() {
  int t; cin >> t;
  for (int c = 1; c <= t; c++) {
    int n; cin >> n;
    map<int, int> pos;
    for (int i = 0; i < n; i++) {
      cin >> a[i];
      pos[a[i]] = i;
    }
    sort(a, a+n);

    int left = 0, right = n-1, res = 0;
    for (int i = 0; i < n; i++) {
      int cl = pos[a[i]] - left, cr = right - pos[a[i]];
      if (cl < cr) {
        for (int j = i+1; j < n; j++)
          if (pos[a[j]] >= left && pos[a[j]] <= pos[a[i]]) pos[a[j]]++;
        pos[a[i]] = left++;
        res += cl;
      } else {
        for (int j = i+1; j < n; j++)
          if (pos[a[j]] >= pos[a[i]] && pos[a[j]] <= right) pos[a[j]]--;
        pos[a[i]] = right--;
        res += cr;
      }
    }
    cout << "Case #" << c << ": " << res << endl;
  }
  return 0;
}
