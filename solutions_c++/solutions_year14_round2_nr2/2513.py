#include <iostream>
#include <cmath>

using namespace std;

int main(int, char**)
{
  int tt;
  cin >> tt;
  for(int id = 1; id <= tt; id++)
  {
    int a, b, k;
    cin >> a >> b >> k;

    int count = 0;

    int bitwise;
    for(int ia = 0; ia < a; ia++)
    {
      for(int ib = 0; ib < b; ib++)
      {
        bitwise = ia & ib;
        //cout << "A: " << ia << "|"<<ib << ": " << bitwise << endl;
        if(bitwise < k )
          count++;
      }
    }

    cout << "Case #" << id << ": " << count << endl;
  }
  return 0;
}