//James Stojic

#include <iostream>
using namespace std;
int main()
{
  int T, arr1[5][5], arr2[5][5], choice1, choice2, possible;
  int num = 0;
  cin >> T;

  for(int i = 1; i <= T; i++)
  {
    cin >> choice1;
    for(int j = 1; j <= 4; j++)
      for(int k = 1; k <= 4; k++)
        cin >> arr1[j][k];
    cin >> choice2;
    for(int j = 1; j <= 4; j++)
      for(int k = 1; k <= 4; k++)
        cin >> arr2[j][k];

    for(int j = 1; j <= 4; j++)
      for(int k = 1; k <= 4; k++)
        if(arr1[choice1][j] == arr2[choice2][k])
        {
          possible = arr1[choice1][j];
          num++;
        }
    cout << "Case #" << i << ": ";
    switch(num)
    {
      case 0: cout << "Volunteer cheated!" << endl; break;
      case 1: cout << possible << endl; break;
      default: cout << "Bad magician!" << endl; break;
    }
  num = 0;
  }
  return 0;
}
