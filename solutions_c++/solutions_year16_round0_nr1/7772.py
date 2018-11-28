#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;
    for (int t = 0; t < n; t++) {

      bool seenDigits[10];
      for (int i = 0; i < 10; i++) {
        seenDigits[i] = false;
      }

      long long start;
      cin >> start;

      if (start == 0) {
        cout << "Case #" << t+1 << ": " << "INSOMNIA\n";
        continue;
      }


      int x = 1;
      while (true) {
          long long current = x * start;
          //cout << current << "\n";
          while (current > 0) {
            //cout << current % 10;
            seenDigits[current % 10] = true;
            current = current / 10;
          }

          if (seenDigits[0] && seenDigits[1] && seenDigits[2] && seenDigits[3] && seenDigits[4] && seenDigits[5] && seenDigits[6] && seenDigits[7] && seenDigits[8] && seenDigits[9]) {
              cout << "Case #" << t+1 << ": " << x * start << "\n";
              break;
          }
          x++;
      }
    }

    return 0;
}