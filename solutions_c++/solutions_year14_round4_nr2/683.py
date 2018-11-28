#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
  int t;
  cin >> t;
  for (int c = 1; c <= t; ++c) {
    int n;
    cin >> n;
    vector<int> data;
    for (int i = 0; i < n; ++i) {
      int x;
      cin >> x;
      data.push_back(x);
    }
    int res = 999999999;
    vector<int> pos(n);
    iota(pos.begin(), pos.end(), 0);
    do {
      int tmp = 0;
      for (int i = 0; i < n; ++i) {
        for (int j = 0; j < i; ++j) {
          if (pos[i] > pos[j]) ++tmp;
        }
      }
      int x = 1;
      while (x < n && data[pos[x-1]] < data[pos[x]]) ++x;
      while (x < n && data[pos[x-1]] > data[pos[x]]) ++x;
      if (x < n) continue;
      res = min(res, tmp);
    } while (next_permutation(pos.begin(), pos.end()));
    clog << n << " " << res << endl;
    cout << "Case #" << c << ": " << res << endl;
  }
  return 0;
}
