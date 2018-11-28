#include <iostream>
#include <vector>
using namespace std;

int main(void)
{
  int T;
  cin >> T;
  vector<int> v1(4);
  vector<int> v2(4);
  for (int i = 0; i < T; i++)
  {
    int ans1;
    cin >> ans1;
    for (int j = 0; j < 4; j++)
    {
      if (j == ans1 - 1)
      {
        for (int k = 0; k < 4; k++)
          cin >> v1[k];
      }
      else
      {
        int spam;
        for (int k = 0; k < 4; k++)
          cin >> spam;
      }
    }
    int ans2;
    cin >> ans2;
    for (int j = 0; j < 4; j++)
    {
      if (j == ans2 - 1)
      {
        for (int k = 0; k < 4; k++)
          cin >> v2[k];
      }
      else
      {
        int spam;
        for (int k = 0; k < 4; k++)
          cin >> spam;
      }
    }

    int counter = 0;
    int lastFound = -1;
    for (int j = 0; j < 4; j++)
    {
      for (int k = 0; k < 4; k++)
      {
        if (v1[j] == v2[k])
        {
          lastFound = v1[j];
          counter++;
        }
      }
    }

    switch (counter)
    {
    case 0:
      cout << "Case #" << i + 1 << ": Volunteer cheated!\n";
      break;
    case 1:
      cout << "Case #" << i + 1 << ": " << lastFound << endl;
      break;
    default:
      cout << "Case #" << i + 1 << ": Bad magician!\n";
    }
  }
  return 0;
}