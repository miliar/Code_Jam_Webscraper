#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <iterator>
#include <ctime>
#include <iomanip>

typedef unsigned int uint32;
typedef signed long long int64;
typedef unsigned long long uint64;

using namespace std;

#define ALL(a) a.begin(), a.end()
#define FOR(a) for (int i = 0; i < (a); ++i)
#define D(a) #a << ": " << a << "\n"

vector<string> arr;
vector<string> seen;
int res, r, c;

map<char, vector<int>> off;

char next_(char c)
{
  switch (c)
  {
    case 'v': return '<';
    case '<': return '^';
    case '^': return '>';
    case '>': return 'v';
  }
}

char rot(pair<int, int> a)
{
  arr[a.first][a.second] = next_(arr[a.first][a.second]);
  return arr[a.first][a.second];
}

int go(int i, int j, pair<int, int> last, char dir)
{
  if (i < 0 || i >= r || j < 0 || j >= c)
    return 0;

  if (seen[i][j])
    return 1;

  seen[i][j] = 1;

  int a = 0;
  if (arr[i][j] != '.')
  {
    last ={ i, j };
    dir = arr[i][j];

    for (; a < 4; ++a)
    {
      int ii = i + off[dir][0];
      int jj = j + off[dir][1];
      if (go(ii, jj, last, dir))
        break;

      dir = rot(last);
    }

    seen[i][j] = 0;

    if (a == 4)
      return 0;

    if (a != 0)
      ++res;

    return 1;
  }
  
  return go(i + off[dir][0], j + off[dir][1], last, dir);
}

int main()
{
  off.insert({ 'v', { 1,  0 } });
  off.insert({ '^', { -1, 0 } });
  off.insert({ '<', { 0, -1 } });
  off.insert({ '>', { 0,  1 } });

  int CASES;
  cin >> CASES;
  for (int CASE = 1; CASE <= CASES; ++CASE)
  {
    cin >> r >> c;
    arr.clear();
    arr.resize(r);
    seen.clear();
    string tmp;
    FOR(c) tmp += '\0';
    FOR(r) cin >> arr[i];

    int ok = 1;
    res = 0;
    for (int i = 0; i < r && ok; ++i)
    {
      for (int j = 0; j < c && ok; ++j)
      {
        if (arr[i][j] != '.')
        {
          seen.clear();
          seen.resize(r, tmp);
          ok = go(i, j, { i, j }, arr[i][j]);
        }
      }
    }

    if (ok)
      printf("Case #%d: %d\n", CASE, res);
    else
      printf("Case #%d: IMPOSSIBLE\n", CASE);
  }

  return 0;
}
