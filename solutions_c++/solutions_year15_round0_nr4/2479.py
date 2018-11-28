#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
  int t, caseN = 1, x, r, c;
  cin >> t;
  while (t--) {
    bool richard = true;
    cin >> x >> r >> c;

    if (r*c >= x && (r*c)%x == 0) {
      richard = false;
      
      if (x == 3 && (r*c)/x == 1) {
	richard = true;
      } else if (x == 4 && ((r*c)/x == 1 || (r*c)/x == 2)) {
	richard = true;
      }
    }

    printf("Case #%d: %s\n", caseN++, (richard) ? "RICHARD" : "GABRIEL");
  }
  return 0;
}
