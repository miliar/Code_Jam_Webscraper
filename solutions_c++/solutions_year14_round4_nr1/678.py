#include <iostream>
#include <set>
using namespace std;

int main()
{
  int t;
  cin >> t;
  for (int c = 1; c <= t; ++c) {
    int n, x;
    cin >> n >> x;
    multiset<int, greater<int>> data;
    for (int i = 0; i < n; ++i) {
      int s;
      cin >> s;
      data.insert(s);
    }
    int res = 0;
    while (!data.empty()) {
      ++res;
      int a = *data.begin();
      data.erase(data.begin());
      auto it = data.lower_bound(x-a);
      if (it != data.end()) {
        data.erase(it);
      }
    }
    cout << "Case #" << c << ": " << res << endl;
  }
  return 0;
}
