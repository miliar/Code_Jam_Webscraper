#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <set>
using namespace std;

int main()
{
  int cases;
  cin >> cases;

  for (int z = 0; z < cases; z++)
  {
    int n;
    std::cin >> n;
    int on = n;

    cout << "Case #" << z + 1 << ": ";

    if (n != 0)
    {
      set<int> digits = set<int>();
      while (digits.size() != 10)
      {
        int cn = n;
        while (cn != 0)
        {
          digits.insert(cn % 10);
          cn /= 10;
        }

        n += on;
      }
      cout << n - on;
    }
    else
    {
      cout << "INSOMNIA";
    }

    cout << endl;
  }

  return 0;
}
