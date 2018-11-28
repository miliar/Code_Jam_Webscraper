#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <iomanip>
#include <algorithm>

using namespace std;

int main()
{
  ifstream in("/home/eric30/Eric/googlecodejam/2014/qualification/A-small-attempt0.in");
  ofstream out("/home/eric30/Eric/googlecodejam/2014/qualification/a.out");

  if (in.is_open()) {
    int cases;
    in >> cases;

    for (int c = 1; c <= cases; ++c) {
      int ans;
      in >> ans;

      int cards[16];
      for (int i = 0; i < 16; ++i) {
        in >> cards[i];
      }

      int candidates[4];
      for (int i = 0; i < 4; ++i) {
        candidates[i] = cards[(ans - 1) * 4 + i];
      }

      // Second round begins
      int secondRoundRow[4];
      in >> ans;

      for (int i = 0; i < 16; ++i) {
        int n;
        in >> n;

        for (int j = 0; j < 4; ++j) {
          if (candidates[j] == n) {
            secondRoundRow[j] = i / 4;
            break;
          }
        }
      }

      // Check if there is only one candidate at row |ans|
      int count = 0;
      int magicNumber = 0;
      for (int i = 0; i < 4; ++i) {
        if (secondRoundRow[i] == ans - 1) {
          ++count;
          magicNumber = candidates[i];
        }
      }

      if (count == 1) {
        out << "Case #" << c << ": " << magicNumber << endl;
      } else if (count == 0) {
        out << "Case #" << c << ": Volunteer cheated!" << endl;
      } else {
        out << "Case #" << c << ": Bad magician!" << endl;
      }
    }
  }

  return 0;
}
