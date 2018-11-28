#include <iostream>
#include <bitset>

typedef long long llong;

using namespace std;

int main () {
  int testc;
  cin >> testc;

  for (int t = 1; t <= testc; t++) {
    bitset<10> vis;

    llong inum;
    cin >> inum;

    if (inum == 0) {
      cout << "Case #" << t << ": INSOMNIA" << endl;
    } else {
      llong ans = 0;
      for (int i = 1; !vis.all(); i++) {
        ans = i * inum;
        for (llong cur = i * inum; cur != 0; cur /= 10) {
          vis[cur % 10] = true;
        }
      }

      cout << "Case #" << t << ": " << ans << endl;
    }
  }
}
