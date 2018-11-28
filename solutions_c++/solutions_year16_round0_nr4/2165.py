#include <iostream>
#include <cstdlib>
#include <stdio.h>
#include <math.h>
#include <sstream>

using namespace std;

int main()
{
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t)
  {
    int K, C, S;
    cin >> K >> C >> S;
    cout << "Case #" << t << ": ";
    for (int i = 1; i <=S; ++i)
    {
      cout << i << " ";
    }
    cout << endl;
  }
}
