#include <vector>
#include <iostream>

// X is 1, O is 10, T is 100, 0 is empty.
typedef std::vector<std::vector<int> > Table;

Table ReadTable()
{
  Table ret(4);
  for ( int i = 0; i < 4; ++i )
  {
    std::string s;
    std::cin >> s;
    std::vector<int> v(4);
    for ( int j = 0; j < 4; ++j )
    {
      if ( s[j] == 'X' )
        v[j] = 1;
      else if ( s[j] == '.' )
        v[j] = 0;
      else if ( s[j] == 'O' )
        v[j] = 10;
      else if ( s[j] == 'T' )
        v[j] = 100;
    }
    ret[i] = v;
  }
  return ret;
}

int CheckLine(int i0, int i1, int i2, int i3)
{
  int sum = i0 + i1 + i2 + i3;
  if ( sum == 4 || sum == 103 )
    return 1;
  else if ( sum == 40 || sum == 130 )
    return 10;

  if ( !i0 || !i1 || !i2 || !i3 )
    return 0;
  else
    return -1;
}

bool Output(int res, int c)
{
  if ( res == 1 )
  {
    std::cout << "Case #" << c << ": X won" << std::endl;
    return true;
  }
  else if ( res == 10 )
  {
    std::cout << "Case #" << c << ": O won" << std::endl;
    return true;
  }
  return false;
}

void Process(const Table& ta, int c)
{
  bool emptyCases = false;
  for ( int i = 0; i < 4; ++i )
  {
    // Check row.
    int res = CheckLine(ta[i][0], ta[i][1], ta[i][2], ta[i][3]);
    if ( res == 0 )
      emptyCases = true;
    if ( Output(res, c) )
      return;

    // Check column.
    res = CheckLine(ta[0][i], ta[1][i], ta[2][i], ta[3][i]);
    if ( res == 0 )
      emptyCases = true;
    if ( Output(res, c) )
      return;
  }
  // Diagonal.
  int res = CheckLine(ta[0][0], ta[1][1], ta[2][2], ta[3][3]);
  if ( res == 0 )
    emptyCases = true;
  if ( Output(res, c) )
    return;

  // Reverse Diagonal.
  res = CheckLine(ta[3][0], ta[2][1], ta[1][2], ta[0][3]);
  if ( res == 0 )
    emptyCases = true;
  if ( Output(res, c) )
    return;

  if ( emptyCases )
    std::cout << "Case #" << c << ": Game has not completed" << std::endl;
  else
    std::cout << "Case #" << c << ": Draw" << std::endl;
}

int main()
{
  int t;
  std::cin >> t;
  for ( int i = 0; i < t; ++i )
  {
    Table table = ReadTable();
    std::string empty;
    std::getline(std::cin, empty);
    Process(table, i + 1);
  }
}

