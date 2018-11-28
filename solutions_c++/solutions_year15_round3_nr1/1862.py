
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;


void main()
{
  int t, T;
  cin >> T;
  for (t = 1; t <= T; t++)
  {
    unsigned R, C, W;
    cin >> R;
    cin >> C;
    cin >> W;
    cout << "Case #" << t << ": " << R * ((C / W) + (W - 1) + ((C % W)?1:0)) << '\n';
  }
}

