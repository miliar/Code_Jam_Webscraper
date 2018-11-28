#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#ifdef CXX0X
#include <unordered_map>
#endif
#include <set>
#include <algorithm>
#include <utility>
#include <cstring>
#include <cstdlib>
using namespace std;
#define SIZE 105
#define MOD_NUM 
#define MOD(n) (n%MOD_NUM)
typedef unsigned long long int ulli;
typedef long long int slli;
typedef pair<int,int> pr;

int c, n, m;
int mtx[SIZE][SIZE];

inline bool horizon_possible(int base, int x)
{
  for(int i=0; i<m; ++i)
    if(mtx[x][i] > base)
      return false;
  return true;
}
inline bool vertical_possible(int base, int y)
{
  for(int i=0; i<n; ++i)
    if(mtx[i][y] > base)
      return false;
  return true;
}

inline bool possible(int x, int y)
{
  return horizon_possible(mtx[x][y], x) || vertical_possible(mtx[x][y], y);
}

bool solve()
{
  for(int i=0; i<n; ++i)
    for(int j=0; j<m; ++j)
      if(!possible(i, j))
        return false;
  return true;
}

int main()
{
  ios::sync_with_stdio(false);
  cin >> c;
  for(int z=0; z<c; ++z)
  {
    cin >> n >> m;
    for(int i=0; i<n; ++i)
      for(int j=0; j<m; ++j)
        cin >> mtx[i][j];
    cout << "Case #" << z+1 << ": ";
    if(solve())
      cout << "YES" << endl;
    else
      cout << "NO" << endl;
  }
}
