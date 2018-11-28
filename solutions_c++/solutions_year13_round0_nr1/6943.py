#include <iostream>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

int print_res (int id, string str)
{
  printf ("Case #%d: %s\n", id + 1, str.c_str ());
  return 0;
}

int solve (int id)
{
  string str;
  char field[4][4];
  int dot_found = 0;
  for (int i = 0; i < 4; ++i)
  {
    getline (cin, str);
    for (int j = 0; j < 4; ++j)
    {
      field[i][j] = str[j];
      if (field[i][j] == '.')
        dot_found = 1;
    }
  }
  getline (cin, str);
  int x, o, t;
  /// Diagonals
  x = o = t = 0;
  for (int i = 0; i < 4; ++i)
    switch (field[i][i])
  {
    case 'X': x++; break;
    case 'O': o++; break;
    case 'T': t++; break;
    default: break;
  }
  if (x + t == 4)
    return print_res (id, "X won");
  if (o + t == 4)
    return print_res (id, "O won");
  x = o = t = 0;
  for (int i = 0; i < 4; ++i)
    switch (field[i][3 - i])
  {
    case 'X': x++; break;
    case 'O': o++; break;
    case 'T': t++; break;
    default: break;
  }
  if (x + t == 4)
    return print_res (id, "X won");
  if (o + t == 4)
    return print_res (id, "O won");
  /// ROW
  for (int j = 0; j < 4; ++j)
  {
    x = o = t = 0;
    for (int i = 0; i < 4; ++i)
      switch (field[i][j])
    {
      case 'X': x++; break;
      case 'O': o++; break;
      case 'T': t++; break;
      default: break;
    }
    if (x + t == 4)
      return print_res (id, "X won");
    if (o + t == 4)
      return print_res (id, "O won");
  }
  /// COL
  for (int j = 0; j < 4; ++j)
  {
    x = o = t = 0;
    for (int i = 0; i < 4; ++i)
      switch (field[j][i])
    {
      case 'X': x++; break;
      case 'O': o++; break;
      case 'T': t++; break;
      default: break;
    }
    if (x + t == 4)
      return print_res (id, "X won");
    if (o + t == 4)
      return print_res (id, "O won");
  }

  if (dot_found)
    return print_res (id, "Game has not completed");
  else
    return print_res (id, "Draw");

  return -1;
}

int main ()
{
  freopen ("input.txt", "r", stdin);
  freopen ("output.txt", "w", stdout);
  
  string case_str;
  getline (cin, case_str);
  size_t cases = atoi (case_str.c_str ());
  
  for (size_t id = 0; id < cases; ++id)
    if (solve (id) < 0)
      std::cerr << "BAD CASE: " << id + 1 << endl;

  return 0;
}