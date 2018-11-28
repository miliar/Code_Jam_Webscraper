#include <iostream>
#include <string>
#include <vector>
#define sz(x) ((int)((x).size()))
#define pb push_back
using namespace std;

int tn, x, n, m;

int main(int argc, char *argv[])
{
  cin >> tn;
  for (int ti = 1; ti <= tn; ++ti) {
    cin >> x >> n >> m;
    bool gwin = false;
    if ((n * m) % x == 0) {
      if (x <= 2) {
        gwin = true;
      } else if (x == 3) {
        if (n % x == 0 && m >= 2)
          gwin = true;
        if (m % x == 0 && n >= 2)
          gwin = true;
      } else if (x == 4) {
        if (n % x == 0 && m >= 3)
          gwin = true;
        if (m % x == 0 && n >= 3)
          gwin = true;
      }
    }
    if (gwin) {
      cout << "Case #" << ti << ": GABRIEL" << endl;
    } else {
      cout << "Case #" << ti << ": RICHARD" << endl;
    }
  }
  return 0;
}
