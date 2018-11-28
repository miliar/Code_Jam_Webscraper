#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
using namespace std;

int main(int argc, char *argv[])
{
  int T;
  cin >> T;
  for (int x = 0; x < T; x++)
  {
    bool bDone = false;
    long double t;
    long long r;
    int y = 0;
    cin >> r >> t;
    while (!bDone)
    {
      t -= ((r+1)*(r+1) - (r*r));
      if (t >= 0)
      {
        y++;
      }
      else
      {
        bDone = true;
      }
      r += 2;
    }
    cout << "Case #" << (x + 1) << ": " << y << endl;
  }

  return 0;
}
