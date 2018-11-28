#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
  int T, N, x;
  int chk[10];

  cin >> T;
  for (int i = 1; i <= T; ++i) {
    cin >> N;

    x = 0;
    for (int j = 0; j < 10; ++j) chk[j] = 0;

    for (int j = 0;; ++j) {
      x += N;

      int y = x;
      do {
        chk[y % 10] = 1;
        y /= 10;
      } while (y);

      if (accumulate(chk, chk + 10, 0) == 10) {
        cout << "Case #" << i << ": " << x << endl;
        break;
      } else if (j >= 1E8 || x >= 1E10) {
        cout << "Case #" << i << ": INSOMNIA" << endl;
        break;
      }
    }
  }
  
  return 0;
}
