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

struct grid {
  int d[4];
};

grid g1, g2;

void bad_magician()
{
  cout << "Bad magician!";
}

void volunteer_cheated()
{
  cout << "Volunteer cheated!";
}

void resolve()
{
  int both_row[17];
  for(int i=0; i < 17; ++i)
    both_row[i] = 0;
  for(int i=0; i < 4; ++i)
  {
    ++both_row[g1.d[i]];
  }
  for(int i=0; i < 4; ++i)
  {
    ++both_row[g2.d[i]];
  }
  int sol = -1;
  bool more_than_one = false;
  for(int i=1; i < 17 && !more_than_one; ++i)
  {
    if(both_row[i] >= 2)
    {
      if(sol == -1)
        sol = i;
      else
        more_than_one = true;
    }
  }
  if(more_than_one)
    bad_magician();
  else if(sol == -1)
    volunteer_cheated();
  else
    cout << sol;
}

void read_grid(grid& g)
{
  int ign;
  int row;
  cin >> row;
  --row;
  for(int i=0; i < 4; ++i)
    for(int j=0; j < 4; ++j)
      if(i == row)
        cin >> g.d[j];
      else
        cin >> ign;
}

int main()
{
  int test_cases;
  scanf("%d", &test_cases);
  for(int t=1; t <= test_cases; ++t)
  {
    read_grid(g1);
    read_grid(g2);
    cout << "Case #" << t << ": ";
    resolve();
    cout << "\n";
  }
}
