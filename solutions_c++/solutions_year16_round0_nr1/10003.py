#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text

int main() {
    int t, n, m;
    char seenArray[10];
    for (int i = 0; i < 10; i++) seenArray[i] = 0;
    int seen = 0;
    int insomnias = 0;

    cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
    for (int i = 1; i <= t; ++i) {
      cin >> n;  // read n and then m.
      n = n < 0 ? -n : n;
      if (n == 0) {
        insomnias++;
        cout << "Case #" << i << ": INSOMNIA" << endl;
        continue;
      }
      seen = 0;
      int j = 1;
      int p = 0;
      int hasBeenSeen = (i + insomnias)%2;
      while (seen < 10) {
        int m = n * (j++);
        p = m;
        while (m > 0) {
          int k = m % 10;
          if (seenArray[k] != hasBeenSeen) {
            seen++;
            seenArray[k] = hasBeenSeen;
          }
          m /= 10;
        }
      }
      cout << "Case #" << i << ": " << p << endl;
    }
    return 0;
}
