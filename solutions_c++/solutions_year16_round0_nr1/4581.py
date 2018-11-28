#include <cstdio>
#include <iostream>
#include <algorithm>
#include <queue>
#include <cmath>
#include <set>
using namespace std;

int main() {
  freopen("A-large.in", "r", stdin);
  freopen("file.out", "w", stdout);
  int T, n;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    cout << "Case #" << t << ": ";
    cin >> n;
    if(n == 0) {
      cout << "INSOMNIA\n";
      continue;
    }
    set<int> s;
    int i = 1;
    int num;
    while(1) {
      num = i * n;
      int tmp = num;
      while(tmp) {
        s.insert(tmp % 10);
        tmp /= 10;
      }
      if (s.size() == 10) {
        cout << num << endl;
        break;
      }
      ++i;
    }
  }
  return 0;
}
