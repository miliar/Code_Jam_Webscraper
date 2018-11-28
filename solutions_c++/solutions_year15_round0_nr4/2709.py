#include <iostream>
using namespace std;

int main() {

  int t;
  cin >> t;
  cerr << "Tests: " << t << endl;
  for (int i = 0 ; i < t ; ++i) {
    int x,r,c;
    cin >> x >> r >> c;
    cerr << "x,r,c: " << x << r << c << endl;
    
    if (r > c) {int t = r; r = c; c = t;}
    bool possible = false;

    switch (x) {
    case 1:
      possible = true;
      break;
    case 2:
      possible = ((r * c) % 2 == 0);
      break;
    case 3:
      possible = (c == 3 && r >= 2) || (c == 4 && r == 3);
      break;
    case 4:
      possible = (c == 4 && r >= 3);
      break;
    }
    cout << "Case #" << (i + 1) << ": " << (possible ? "GABRIEL" : "RICHARD") << endl;
  }
  return 0;
}

