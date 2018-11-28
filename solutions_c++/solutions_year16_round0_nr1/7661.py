#include <iostream>
#include <cstdio>

using namespace std;

int main() {
  int T = -1;
  scanf("%d", &T);
  for (int i = 0; i < T; ++i) {
    int N = -1;
    scanf("%d", &N);

    int nums[10];
    for (int j = 0; j < 10; ++j) {
      nums[j] = 0;
    }
    int startNum = N;
    int loop = 0;
    int insomnia = 1;
    int count = 0;
    int done = 0;
    while (!done) {
      int tempNum = startNum;
//      cout << "other loop" << endl;
      while (tempNum) {
        int digit = tempNum % 10;
        tempNum = tempNum / 10;
        if (nums[digit] == 0) {
//        cout << "digit from " << startNum << " and " << tempNum << ": " << digit << endl;
          nums[digit]++;
          count++;
        }
        if (count >= 10) {
          insomnia = 0;
          done = 1;
          break;
        }
      }
      if (done == 1) break;
      startNum += N;
//      cout << startNum << endl;
      loop++;
      if (loop > 1000) break;
    }
    cout << "Case #" << (i+ 1) << ": ";
    if (insomnia == 1) {
      cout << "INSOMNIA";
    } else {
      cout << startNum;
    }
    cout << endl;
  }
  return 0;
}
