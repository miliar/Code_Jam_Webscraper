#include <iostream>
#include <string.h>
#include <vector>
#include <algorithm>
#include <math.h>

using namespace std;


int main() {

  int T;
  cin >> T;

  for (int x=1; x<=T; ++x) {

    int X, R, C;
    cin >> X >> R >> C;
    bool Gwins = false;

    if ( ( R * C ) % X == 0 ){
      switch (X) {
        case 1:
          Gwins = true; break;
        case 2:
          Gwins = true; break;
        case 3:
          if (!(R<2||C<2)) Gwins = true; break;
        case 4:
          if ( min(R,C)>=3 && max(R,C)==4 ) Gwins = true; break;
      }
    }
    cout << "Case #" << x << ": " << (Gwins ? "GABRIEL" : "RICHARD") << endl;
}
return 0;
}
