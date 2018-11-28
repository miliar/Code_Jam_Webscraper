#pragma comment(linker, "/STACK:256000000")
#include <stdio.h>
#include <iostream>
#include <cmath>
#include <math.h>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <map>

using namespace std;

  long long W, H;
  long long a[109][509];


int main() {
  freopen("input", "r", stdin);
  freopen("output", "w", stdout);
  std::ios_base::sync_with_stdio(false);
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) { 
    string s;
    int res = 0, stand = 0, size;
    cin >> size >> s;
    for (int i = 0 ; i < s.size(); ++i) {
      if (stand < i) {
        res += i - stand;
        stand = i;
      }
      stand += int(s[i]) - int ('0');
    }

    cout << "Case #" << t << ": ";
    cout << res << "\n";
  }
}
