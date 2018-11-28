#include <iostream>
#include <vector>

using namespace std;


int main() {
  int T;
  cin >> T;
  for (int t = 1;t <= T;t++) {
    int n;
    cin >> n;
    int ans = n;
    if (n == 0) {
      printf("Case #%d: INSOMNIA\n",t);
      continue;
    }
    vector<bool> seen = vector<bool>(10,false);
    int remain = 10;
    while (true) {
      int x = ans;
      do {
        if (!seen[x % 10]) {
          remain--;
        }
        seen[x % 10] = true;
        x = x / 10;
      } while (x > 0);
      if (remain <= 0) {
        printf("Case #%d: %d\n",t,ans);
        break;
      }
      ans += n;
    }
  }
}

