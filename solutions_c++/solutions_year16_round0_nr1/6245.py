#include <iostream>
#include <vector>
#include <map>
using namespace std;

int main() {
  int caseNum = 0;
  cin >> caseNum;

  for (int c = 0; c < caseNum; c++) {
    int N = 0;
    cin >> N;
    if (!N) {
      cout << "Case #" << c+1 << ": INSOMNIA";
      if (c != caseNum-1) {
        cout << endl;
      }
      continue;
    }

    int met[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    int done = 0;
    int num = N;
    while (done < 10) {
      int now = num;

      while (now) {
        int digit = now % 10;
        if (!met[digit]) {
          met[digit] = 1;
          done++;
        }
        now /= 10;
      }

      num += done >= 10 ? 0 : N;
    }

    cout << "Case #" << c+1 << ": " << num;
    if (c != caseNum-1) {
      cout << endl;
    }
  }

  return 0;
}
