#include <iostream>

using namespace std;

int main()
{
  int t;
  cin >> t;
  for (int i = 1; i <= t; i++)
  {
    int row[4][2], col[4][2], diag1[2], diag2[2];
    for (int j = 0; j < 4; j++)
      for (int k = 0; k < 2; k++)
        row[j][k] = col[j][k] = 0;
    diag1[0] = diag1[1] = diag2[0] = diag2[1] = 0;
    bool full = true;
    for (int j = 0; j < 4; j++)
      for (int k = 0; k < 4; k++)
      {
        char c;
        cin >> c;
        if (c == '.')
        {
          full = false;
        }
        if (c == 'X' || c == 'T')
        {
          row[j][0]++;
          col[k][0]++;
          if (j == k) diag1[0]++;
          if (j + k == 3) diag2[0]++;
        }
        if (c == 'O' || c == 'T')
        {
          row[j][1]++;
          col[k][1]++;
          if (j == k) diag1[1]++;
          if (j + k == 3) diag2[1]++;
        }
      }
    int who = -1;
    for (int j = 0; j < 4; j++)
      if (row[j][0] == 4 || col[j][0] == 4)
      {
        who = 0;
        break;
      }
      else if (row[j][1] == 4 || col[j][1] == 4)
      {
        who = 1;
        break;
      }
    if (diag1[0] == 4 || diag2[0] == 4) who = 0;
    if (diag1[1] == 4 || diag2[1] == 4) who = 1;
    cout << "Case #" << i << ": ";
    if (who == 0)
      cout << "X won" << endl;
    else if (who == 1)
      cout << "O won" << endl;
    else
    {
      if (full)
        cout << "Draw" << endl;
      else
        cout << "Game has not completed" << endl;
    }
  }
  return 0;
}

