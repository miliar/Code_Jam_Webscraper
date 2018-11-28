#include <stdlib.h>
#include <stdio.h>
#include <iostream>

using namespace std;

int main()
{
  int T;
  cin >> T;
  for (int counter = 1; counter <= T; counter++) {
    int count[17];
    for (int i = 1; i <= 16; i++) {
      count[i] = 0;
    }

    for (int i = 0; i < 2; i++) {
      int row;
      cin >> row;
      for (int j = 1; j <= 4; j++) {
        for (int k = 1; k <= 4; k++) {
          int temp;
          cin >> temp;
          if (j == row) {
            count[temp]++;
          }
        }
      }
    }

    int ans = 0;
    int total = 0;
    for (int i = 1; i <= 16; i++) {
      if (count[i] == 2) {
        ans = i;
        total++;
      }
    }
    cout << "Case #" << counter << ": ";
    if (total == 0) {
      cout << "Volunteer cheated!";
    }
    else if (total == 1) {
      cout << ans;
    }
    else {
      cout << "Bad magician!";
    }
    cout << "\n";
  }

  return 0;
}

