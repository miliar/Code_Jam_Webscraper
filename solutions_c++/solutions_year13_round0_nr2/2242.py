#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

typedef vector<int> vi;
typedef long long ll;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<vi> vvi;
typedef vector<vii> vvii;

#define INF 100000000

int main()
{
  int T; cin >> T;
  for(int t = 1; t <= T; ++t)
  {
    int N, M; cin >> N >> M;
    vvi grid(N, vi(M));
    for(int i = 0; i < N; ++i)
    {
      for(int j = 0; j < M; ++j)
      {
        cin >> grid[i][j];
      }
    }
    bool possible = true;
    for(int i = 0; i < N; ++i)
    {
      for(int j = 0; j < M; ++j)
      {
        //test horizontal
        bool possible_horizontal = true;
        for(int k = 0; k < M; ++k)
        {
          if (grid[i][j] < grid[i][k]) possible_horizontal = false;
        }
        //test vertical
        bool possible_vertical = true;
        for(int k = 0; k < N; ++k)
        {
          if (grid[i][j] < grid[k][j]) possible_vertical = false;
        }
        //cout << i << " " << j << " - " << possible_horizontal << " " << possible_vertical << endl;
        if (!possible_horizontal && !possible_vertical) possible = false;
      }
    }
    printf("Case #%d: ", t);
    if (possible)
    {
      printf("YES");
    }
    else
    {
      printf("NO");
    }
    printf("\n");
  }
}

