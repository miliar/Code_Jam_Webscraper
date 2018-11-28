#include <iostream>
#include <list>
#include <vector>
#include <algorithm>

using namespace std;

char n[4][4];
char winner = 'M';

bool m(char a, char b)
{
  if (a != '.' && b != '.' && (a == b || a == 'T' || b == 'T'))
  {
    winner = (a == 'T' ? b : a);
    return true;
  }
  else
    return false;
}

void solve_case(int id)
{
  for (int i = 0; i < 4; i++)
  {
    for (int j = 0; j < 4; j++)
    {
      cin >> n[i][j];
    }
    cin.get(); // get rid of the newline
  }
  cin.get(); // get rid of the newline

  for (int i = 0; i < 4; i++)
  {
    if (m(n[i][0], n[i][1]) && m(n[i][1], n[i][2]) && m(n[i][2], n[i][3]))
    {
      cout << "Case #" << id << ": " << winner << " won" << endl;
      return;
    }

    if (m(n[0][i], n[1][i]) && m(n[1][i], n[2][i]) && m(n[2][i], n[3][i]))
    {
      cout << "Case #" << id << ": " << winner << " won" << endl;
      return;
    }
  }
  if (m(n[0][0], n[1][1]) && m(n[1][1], n[2][2]) && m(n[2][2], n[3][3]))
  {
    cout << "Case #" << id << ": " << winner << " won" << endl;
    return;
  }
  if (m(n[3][0], n[2][1]) && m(n[2][1], n[1][2]) && m(n[1][2], n[0][3]))
  {
    cout << "Case #" << id << ": " << winner << " won" << endl;
    return;
  }

  for (int i = 0; i < 4; i++)
    for (int j = 0; j < 4; j++)
      if (n[i][j] == '.')
      {
        cout << "Case #" << id << ": Game has not completed" << endl;
        return;
      }

  cout << "Case #" << id << ": Draw" << endl;
}

int main(void)
{
  int nb_cases;
  cin >> nb_cases;
  cin.get(); // get rid of the newline

  for (int i = 1; i <= nb_cases; i++)
    solve_case(i);

  return 0;
}
