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
#include <cstring>
#include <cstdlib>
#include <ctime>

using namespace std;
typedef long long lglg;

int main()
{
  int T;
  scanf("%d", &T);

  char rows[100][102];

  for(int t = 0; t < T; ++t) {
    printf("Case #%d: ", t+1);
    int R, C;

    scanf("%d%d", &R, &C);
    for(int i = 0; i < R; ++i) {
      scanf("%s", rows[i]);
    }

    int di, dj;
    int fix = 0;
    bool imp = false;

    for(int i = 0; i < R; ++i) {
      for(int j = 0; j < C; ++j) {
        if(rows[i][j] == '.' || imp) {
          continue;
        }

        if(rows[i][j] == '^') {
          di = -1;
          dj = 0;
        } else if(rows[i][j] == '>') {
          di = 0;
          dj = 1;
        } else if(rows[i][j] == '<') {
          di = 0;
          dj = -1;
        } else if(rows[i][j] == 'v') {
          di = 1;
          dj = 0;
        }

        bool good = false;
        int x = i + di, y = j + dj;
        while(x >= 0 && x < R && y >= 0 && y < C) {
          if(rows[x][y] != '.') {
            good = true;
            break;
          }
          x += di;
          y += dj;
        }
        if(!good) {
          ++fix;

          for(int i2 = 0; i2 < R; ++i2) {
            if(i2 != i && rows[i2][j] != '.') {
              good = true;
            }
          }
          for(int j2 = 0; j2 < C; ++j2) {
            if(j2 != j && rows[i][j2] != '.') {
              good = true;
            }
          }
          if(!good) {
            imp = true;
          }
        }
      }
    }

    if(imp) {
      printf("IMPOSSIBLE\n");
    } else {
      printf("%d\n", fix);
    }


  }

  return 0;
}
