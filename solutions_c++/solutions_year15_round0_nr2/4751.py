#include <iostream>
using namespace std;

int n;
int num[1002];

int main() {
  int cas;
  cin >> cas;
  for (int cc=1;cc<=cas;cc++) {
    cin >> n;
    int m = 0;
    for (int i=0;i<n;i++) {
      cin >> num[i];
      m = max(m, num[i]);
    }

    int ans = 1000;
    for (int i=1;i<=m;i++) {
      int tmp = i;
      for (int j=0;j<n;j++) {
        tmp += (num[j] + i - 1) / i - 1;
      }
      ans = min(ans, tmp);
    }

    cout << "Case #" << cc << ": " << ans << endl;
  }
  return 0;
}

