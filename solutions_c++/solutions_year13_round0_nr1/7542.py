#include <iostream>
#include <string>
#include <cstdio>
#include <cstring>
#include <vector>
#include <map>
#include <bitset>
#include <algorithm>
#include <utility>
#include <queue>
#include <iomanip>

using namespace std;
typedef long long ll;
typedef unsigned long long llu;
typedef vector<int> vi;
typedef vector<bool> vb;
typedef vector<ll> vl;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef map<int, int> mii;

#define DFS_WHITE -1
#define DFS_BLACK 1
#define INF 1000000000

#define REP(i, n) for(int i=0; i < n; ++i)
#define SET(x, i) (x |= (1 << (i)))
#define UNSET(x, i) (x &= ~(1 << (i)))
#define GET(x, i) ((x) & (1 << (i)))

#define N 100

char grid[4][4];
string s;

int check(char &last, char c1, int i)
{
  if(i == 3 && (last == c1 || last == 'T' || c1 == 'T'))
  {
    if(c1 == 'O' || last == 'O')
      return 1;
    if(c1 == 'X' || last == 'X')
      return 2;
  }
  else if(c1 != last && c1 != 'T' && last != 'T')
    return 3;
  
  if(c1 != 'T')
    last = c1;
  return -1;
}

int solve()
{
  int result = -1;
  // check vertically
  for(int j=0; j < 4 && result == -1; ++j)
  {
    char last = grid[0][j];
    for(int i=1; i < 4 && result == -1; ++i)
    {
      result = check(last, grid[i][j], i);
    }
    if(result == 3)
      result = -1;
  }
  if(result != -1)
    return result;

  // check horizontally.
  for(int i=0; i < 4 && result == -1; ++i)
  {
    char last = grid[i][0];
    for(int j=1; j < 4 && result == -1; ++j)
    {
      result = check(last, grid[i][j], j);
    }
    if(result == 3)
      result = -1;
  }
  if(result != -1)
    return result;
  // check diagonal 1
  char last = grid[0][0];
  for(int i=1; i < 4 && result == -1; ++i)
  {
    result = check(last, grid[i][i], i);
  }
  if(result == 3)
    result = -1;
  if(result != -1)
    return result;

  // check diagonal 2
  last = grid[0][3];
  for(int i=1, j=2; i < 4 && result == -1; ++i, --j)
  {
    result = check(last, grid[i][j], i);
  }
  if(result == 3)
    result = -1;
  return result;
}

int main()
{
  int test;
  scanf("%d\n", &test);
  for(int i=1; i <= test; ++i)
  {
    bool hasDot = false;
    for(int j=0; j < 4; ++j)
    {
      for(int k=0; k < 4; ++k)
      {
        scanf("%c", &grid[j][k]);
        if(grid[j][k] == '.')
          hasDot = true;
      }
      getline(std::cin, s);
    }
    getline(std::cin, s);
    int res = solve();
    if(res == -1)
    {
      if(hasDot)
        printf("Case #%d: Game has not completed\n", i);
      else
        printf("Case #%d: Draw\n", i);
    }
    else if(res == 1)
    {
      printf("Case #%d: O won\n", i);
    }
    else
      printf("Case #%d: X won\n", i);
  }
  return 0;
}
