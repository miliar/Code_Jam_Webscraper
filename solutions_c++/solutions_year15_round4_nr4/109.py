#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <cmath>
#include <set>
#include <map>
#include <unordered_set>
#include <future>
#include <cstdint>
using namespace std;

int h, w;

inline int get(vector<vector<int>> &bd, int x, int y)
{
  if (y >= 0 && y < h)
    return bd[y][(x+w)%w];
  return -2;
}

inline bool check(vector<vector<int>> &bd, int x, int y)
{
  // cout << "check: " << x << ", " << y << endl;
  int cc = get(bd, x, y);
  if (cc < 0) return true;

  int amb = 0;
  int same = 0;

  {
    int c=get(bd, x, y+1);
    if (c==-1) amb++;
    if (c==cc) same++;
  }
  {
    int c=get(bd, x, y-1);
    if (c==-1) amb++;
    if (c==cc) same++;
  }
  {
    int c=get(bd, x+1, y);
    if (c==-1) amb++;
    if (c==cc) same++;
  }
  {
    int c=get(bd, x-1, y);
    if (c==-1) amb++;
    if (c==cc) same++;
  }

  return (same<=cc&&cc<=same+amb);
}

set<vector<vector<int>>> tbl;

int reg(const vector<vector<int>> &bd)
{
  if (tbl.count(bd)) return 0;

  for (int i=0;i<w;i++){
    vector<vector<int>> cbd(bd);
    for (int y=0;y<h;y++)
      for (int x=0;x<w;x++)
        cbd[y][x]=bd[y][(x+i)%w];
    tbl.insert(cbd);
  }
  return 1;
}

int64_t rec(int x, int y, vector<vector<int>> &bd)
{
  // cout << x << ", " << y << endl;
  if (y == h) {
    if (reg(bd)){
      /*
      cout << w << ", " << h << endl;
      for (int y=0;y<h;y++) {
        for (int x=0;x<w;x++)
          cout << bd[y][x];
        cout << endl;
      }
      // cout << endl;
      */
      return 1;
    }
    else
      return 0;
  }
  if (x == w) return rec(0, y+1, bd);

  int64_t ret = 0;
  for (int c = 1; c <= 4; c++) {
    bd[y][x] = c;
    if (check(bd, x, y) &&
        check(bd, x-1, y) &&
        check(bd, x+1, y) &&
        check(bd, x, y+1) &&
        check(bd, x, y-1))
      ret += rec(x+1, y, bd);
    bd[y][x] = -1;
  }
  return ret;
}

void solve()
{
  cin>>h>>w;
  vector<vector<int>> bd(h, vector<int>(w, -1));
  cout << rec(0, 0, bd) << endl;
}

int main()
{
  int cases; cin>>cases;
  vector<future<string>> fs;
  for (int cn=1;cn<=cases;cn++){
    cout << "Case #" << cn << ": ";
    solve();
    cout << flush;
  }
  return 0;
}
