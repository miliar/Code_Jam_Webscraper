#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#define MOD 1000000007
int poss[10];
int find(int n) {
  if (n == 0) return 0;
  int c = 10;
  for (int i = 0; i < 10; i++) poss[i] = 0;
  for (int it = 1; it <= 100; it++) {
    int j = it * n;
    while (j > 0) {
      if (0 == poss[j % 10]) {
	poss[j % 10] = 1;
	c--;
      }
      j /= 10;
    }
    if (c == 0) return it * n;
  }
  return 0;
}
int main() {
  ios_base::sync_with_stdio(false);
  int t; cin >> t;
  for (int i = 1; i <= t; i++) {
    cout << "Case #" << i << ": ";
    int n; cin >> n;
    int ans = find(n);
    if (ans == 0) cout << "INSOMNIA";
    else cout << ans;
    cout << '\n';
  }
  return 0;
}
