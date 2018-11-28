#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
using namespace std;

int main() {
  freopen("a.in","r",stdin);
  freopen("a.out","w",stdout);
  int t;
  cin >> t;
  int caset = 0;
  while (t > 0) {
    --t;
    caset ++;
    int n1, n2, ans1, a;
    cin >> n1;
    int ans[20];
    ans1 = 0;
    memset(ans, 0, sizeof(ans));
    for (int i = 0; i < 4; ++i)
      for (int j = 0; j < 4; ++j)
      {
        cin >> a;
        if (i == n1 - 1)
          ans[a] = 1;
      }
    cin >> n2;
    for (int i = 0; i < 4; ++i)
      for (int j = 0; j < 4; ++j) {
        cin >> a;
        if (i == n2 - 1)
          if (ans[a]) {
            if (ans1) {
              ans1 = -1; continue;
            }
            else
              ans1 = a;
          }
      }
    if (ans1 == -1) cout << "Case #" << caset << ": Bad magician!\n";
    else if (ans1 == 0) cout << "Case #" << caset << ": Volunteer cheated!\n";
    else cout << "Case #" << caset << ": " << ans1 << endl;
  }
  return 0;
}
