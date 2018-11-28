#include <iostream>

using namespace std;

int main() {
  int cases;
  cin >> cases;

  for (int c = 1; c <= cases; c++) {
    int smax;
    cin >> smax;

    int peopleStanding = 0;
    int friends = 0;
    for (int i = 0; i <= smax; i++) {
      char s;
      cin >> s;
      int n = s - 48; // cast
      if (n > 0) {
        friends += (peopleStanding + friends >= i) ? 0 : i - friends - peopleStanding;
        peopleStanding += n;
      }
    }

    cout << "Case #" << c << ": " << friends << endl;
  }
}
