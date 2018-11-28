#include <cstdio>
#include <iostream>
#include <set>
using namespace std;

int main() {
  int T;
  scanf("%d",&T);

  for (int casen = 1; casen <= T; casen++) {
    printf("Case #%d: ", casen);
    long long n;
    cin >> n;

    if (n == 0) {
      printf("INSOMNIA\n");
    }
    else {
      set<int> digits;
      for (int i = 1; ; i++) {
        long long t = i * n;
        while (t) {
          digits.emplace(t % 10);
          t /= 10;
        }
        if (digits.size() == 10) {
          cout << i * n << endl;
          break;
        }
      }
    }
  }

  return 0;
}
