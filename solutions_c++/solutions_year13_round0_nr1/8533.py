#include <cstdio>

bool Check (char c, char T[4][6])
{
  int  i, j;
  bool found;

  for (i = 0; i < 4; ++i) {
    for (j = 0, found = true; j < 4; ++j)
      if (T[i][j] != c && T[i][j] != 'T') {
        found = false;
        break;
      }
    if (found == true)
      return true;
  }
  if (found == true)
      return true;
  for (i = 0; i < 4; ++i) {
    for (j = 0, found = true; j < 4; ++j)
      if (T[j][i] != c && T[j][i] != 'T') {
        found = false;
        break;
      }
    if (found == true)
      return true;
  }
  for (i = 0, found = true; i < 4; ++i)
    if (T[i][i] != c && T[i][i] != 'T') {
      found = false;
      break;
    }
  if (found == true)
      return true;
  for (i = 0, found = true; i < 4; ++i)
    if (T[i][3 - i] != c && T[i][3 - i] != 'T') {
      found = false;
      break;
    }
  if (found == true)
      return true;
  
  return false;
}

int main()
{
  int  i, j, k, z;
  char T[4][6], result;
  bool full;

  scanf ("%d", &z);
  for (k = 1; k <= z; ++k)
  {
    for (i = 0; i < 4; ++i)
      scanf ("%s", T[i]);
    full = true;
    for (i = 0; i < 4 && full == true; ++i)
      for (j = 0; j < 4; ++j)
        if (T[i][j] == '.') {
          full = false;
          break;
        }
    if (Check ('X', T) == true)
      printf ("Case #%d: X won\n", k);
    else if (Check ('O', T) == true)
      printf ("Case #%d: O won\n", k);
    else if (full == true)
      printf ("Case #%d: Draw\n", k);
    else
      printf ("Case #%d: Game has not completed\n", k);
  }

  return 0;
}
