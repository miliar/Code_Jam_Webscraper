#include <algorithm>  
#include <iostream>  
#include <sstream>  
#include <string>  
#include <vector>  
#include <queue>  
#include <set>  
#include <map>  
#include <cstdio>  
#include <cstdlib>  
#include <cctype>  
#include <cmath>  
#include <list>

using namespace std;

struct swing {
	int p, x;
  bool operator < (const swing ext) const {
    return p < ext.p;
  }
};

int main() {
  long long p, ans1, ans2, x;
  long long two[51];
  long t, z, i, j, k, n;

  ios::sync_with_stdio(0);

  two[0] = 1;
  for (i = 1; i <= 50; ++i)
    two[i] = two[i-1] * 2;
  cin >> t;
  for (z = 1; z <= t; ++z) {
    cin >> n >> p;
    if (p == two[n]) {
      ans1 = p - 1;
      ans2 = p - 1;
    }
    else {
      x = two[n-1];
      j = 1;
      k = n - 2;
      while (p > x) {
        if (k < 0)
          break;
        j++;
        x += two[k];
        k--;
      }
      ans1 = two[j] - 2;
      ans2 = two[n] - 2;
      j = 1;
      k = n - 1;
      while (p < two[k]) {
        ans2 -= two[j];
        k--;
        j++;
      }
    }
    cout << "Case #" << z << ": " << ans1 << " " << ans2 << endl;
  }

  return 0;
}
