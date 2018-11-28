#include <iostream>

using namespace std;

int populate(int t, bool digits[]) {
  while(t) {
    digits[t % 10] = true;
    t /= 10;
  }

  int counter = 0;
  for (int i = 0; i < 10; i++)
    counter += digits[i] ? 1 : 0;

  return counter;
}

int main() {
  bool digits[10];
  int total;

  cin >> total;

  for (int games = 1; games <= total; games++) {
    cout << "Case #" << games << ": ";

    int num;
    cin >> num;

    if (num == 0) cout << "INSOMNIA" << endl;
    else {
      int t = 1;
      for (int i = 0; i < 10; i++) digits[i] = false;
      while (populate(t * num, digits) < 10) {
        t++;
        if ((t * num) / t != num) cout << "overflow" << endl;
      }
      cout << t * num << endl;
    }
  }

  return 0;
}

