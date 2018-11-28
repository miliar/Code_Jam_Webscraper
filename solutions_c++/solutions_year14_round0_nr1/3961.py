#include <iostream>

using namespace std;

bool CheckNum(int* arr, int &n);

int main ()
{
  int T, n, i, k, j, d, ans, tick;

  const int rows = 4;
  const int max_line = 8;

  int nums[rows];

  cin >> T;
  for (i = 1; i <= T; ++i)
  {
    cin >> n;
    tick = 0;
    for (k = 1; k <= rows; ++k)
    {
      if (n != k) 
        for (j = 0; j < rows; ++j)
          {
            cin >> d;
          }
      else 
      {
          for (j = 0; j < rows; ++j)
          {
            cin >> nums[j];
          }
      }
    }

    cin >> n;
    for (k = 1; k <= rows; ++k)
    {
      if (n != k) 
        for (j = 0; j < rows; ++j)
          {
            cin >> d;
          }
      else 
      {
        for (j = 0; j < rows; ++j)
        {
          cin >> d;
          if (CheckNum(nums, d))
          {
            ans = d;
            tick++;
          }
        }
      }
    }

    if(tick == 0)
      cout << "Case #" << i << ": " << "Volunteer cheated!" << endl;
    else if (tick == 1)
      cout << "Case #" << i << ": " << ans << endl;
    else cout << "Case #" << i << ": " << "Bad magician!" << endl;


  }
  
  return 0;
}

bool CheckNum(int* arr, int &n)
{
  for (int i = 0; i < 4; ++i)
  {
    if (arr[i] == n)
    {
      return true;
    }
  }
  return false;
}