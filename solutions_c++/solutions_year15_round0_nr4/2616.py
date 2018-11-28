#include <iostream>

#include <cstdint>

using namespace std;

int main(int, char**)
{
  uint32_t T = 0;
  cin >> T;

  for (uint32_t t = 1; t <= T; t++) {
    bool richard_wins = true;
    uint32_t X, R, C;

    cin >> X >> R >> C;

    if (R == 1 && C == 1) {
      richard_wins = (X == 2) || (X == 3) || (X == 4);
    }
    else if ((R == 1 && C == 2) || (R == 2 && C == 1)) {
      richard_wins = (X == 3) || (X == 4);
    }
    else if (R == 2 && C == 2) {
      richard_wins = (X == 3) || (X == 4);
    }
    else if ((R == 1 && C == 3) || (R == 3 && C == 1)) {
      richard_wins = (X == 2) || (X == 3) || (X == 4);
    }
    else if ((R == 2 && C == 3) || (R == 3 && C == 2)) {
      richard_wins = (X == 4);
    }
    else if (R == 3 && C == 3) {
      richard_wins = (X == 2) || (X == 4);
    }
    else if ((R == 1 && C == 4) || (R == 4 && C == 1)) {
      richard_wins = (X == 3) || (X == 4);
    }
    else if ((R == 2 && C == 4) || (R == 4 && C == 2)) {
      richard_wins = (X == 3) || (X == 4);
    }
    else if ((R == 3 && C == 4) || (R == 4 && C == 3)) {
      richard_wins = false;
    }
    else if (R == 4 && C == 4) {
      richard_wins = (X == 3);
    }
    else {
      cerr << "!!!!!" << endl;
    }
    
    if (richard_wins) {
      cout << "Case #" << t << ": RICHARD" << endl;
    }
    else {
      cout << "Case #" << t << ": GABRIEL" << endl;
    }
  }
  
  return 0;
}
