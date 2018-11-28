#include <algorithm>
#include <vector>
#include <iostream>
#include <string>
#include <functional>
#include <set>
#include <math.h>

using namespace std;

int main()
{
  int T;
  cin >> T;
  getchar();

  for (int t = 0; t < T; ++t)
  {
    int R, C, W;
    int moves(0);
    cin >> R >> C >> W;

    switch (W)
    {
      case 1: 
        moves = R*C;
        break;
      default:
        moves = R * ((int)ceil(1.0*C / W) - 1) + W;
        break;
    }
    
    cout << "Case #" << t + 1 << ": " << moves << endl;

  }
  return 0;
}

