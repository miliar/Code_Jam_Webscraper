#include <iostream>
#include <unordered_set>

using namespace std;

int main () {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);

  int test, c = 0;

  cin >> test;

  while (test > 0) {
    c++;
    test--;
    int n, i = 0;
    unordered_set<int> a;
    bool found = false;

    cin >> n;

    if (n == 0) {
      printf("Case #%d: INSOMNIA\n", c);
      continue;
    }

    while (i < 10000) {
      i++;
      int m = i * n; 

      while (m != 0) {
        int x = m % 10;
        m /= 10;

        if (a.count(x) == 0) {
          a.insert(x);
        }
      }

      if (a.size() == 10) {
        found = true;
        break;
      }
    }

    if (found) {
      printf("Case #%d: %d\n", c, (i*n));
    } else {
      printf("Case #%d: INSOMNIA\n", c);
    }
  }

  return 0;
}
