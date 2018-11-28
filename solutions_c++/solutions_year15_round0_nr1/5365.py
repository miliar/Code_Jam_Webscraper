#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int main () {
  int T; cin >> T;
  for (int tc = 1; tc <= T; tc++) {
    int n;
    string str;
    cin >> n >> str;
    vector<int> s = vector<int>(n+1,0);

    for (int i = 0; i <= n; i++) {
      s[i] = str[i] - '0';
    }

    int ans = 0;
    int total = 0;

    for (int i = 0; i <= n; i++) {
      if (total < i) {
	int p = (i - total);
	total += p;
	ans += p;
      }
      total += s[i];
    }
    cout << "Case #" << tc << ": " << ans << endl;
  }
  return 0;
}
