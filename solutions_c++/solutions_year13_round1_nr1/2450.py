#include <iostream>
#include <string>
#include "string.h"

using namespace std;

int main(int argc, char const *argv[])
{
  int count;
  cin >> count;
  for (int i = 0; i < count; ++i)
  {
    long r,t,n;
    n = 0;
    cin >> r >> t;
    // cout << r << t << endl;
    while(t >= 2 * r + 1) {
      ++n;
      t -= 2 * r + 1;
      r += 2;
      // cout << t  << r << n << endl;
    }
    cout <<"Case #" << i+1 << ": " << n;
    if(i +1 != count) {
      cout <<endl;
    }
  }
  return 0;
}
