#include <iostream>
#include <vector>
#include <stdio.h>
#include <algorithm>
using namespace std;


vector<int> initList(vector<int> myList)
{
  for (int i = 0; i < 10; i++)
  {
    myList.push_back(i);
  }

  return myList;
}

int main()
{
  int t, n;
  cin >> t; // read number of test cases
  for (int i = 1; i <= t; i++)
  {
    cin >> n; // read in the number n

    std::vector<int> list (0, 0);
    list = initList(list);
    int x = -1;
    int factor = 1;

    if (n != 0)
    {
      // counting the sheep in new N
      int newN = n;
      while (!list.empty())
      {
        int num = newN % 10;
        if (find(list.begin(), list.end(), num) != list.end());
        {
          list.erase(std::remove(list.begin(), list.end(), num), list.end());
        }

        if (newN >= 10)
        {
          newN = newN / 10;
        }

        else
        {
          if (!list.empty())
          {
            factor++;
            newN = n * factor;
          }
        }
      }
    }

    if (list.empty())
    {
        x = n * factor;
    }

    if (x < 0)
    {
      cout << "Case #" << i << ": " << "INSOMNIA" << endl;
    }
    else
    {
      cout << "Case #" << i << ": " << x << endl;
    }
  }
}
