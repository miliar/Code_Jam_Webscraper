#include<iostream>
#include<fstream>
#include<string>
#include<cstring>
using namespace std;

const int maxc = 100;
const int maxr = 100;

int main()
{
  ifstream cin("p1.in");
  ofstream cout("p1.out");
  int t, T;
  int dx[] = {0, 0, 1, -1};
  int dy[] = {1, -1, 0, 0};
  string map[maxr];
  cin >> T;
  for (t = 1; t <= T; t ++)
  {
    cout << "Case #" << t << ": ";
    int ans = 0;
    bool ip = false;
    int r, c;
    cin >> r >> c;
    for (int i = 0; i < r; i ++)
      cin >> map[i];
    for (int i = 0; i < r && !ip; i ++)
      for (int j = 0; j < c && !ip; j ++)
        if (map[i][j] != '.')
        {
          bool flag = true;
          int dir;
          if (map[i][j] == '^') dir = 3;
          if (map[i][j] == '<') dir = 1;
          if (map[i][j] == '>') dir = 0;
          if (map[i][j] == 'v') dir = 2;
          int pi = i, pj = j;
          pi += dx[dir]; pj += dy[dir];
          while (flag &&
              pi >= 0 && pj >= 0 && pi < r && pj < c)
          {
            if (map[pi][pj] != '.') flag = false;
            pi += dx[dir]; pj += dy[dir];
          }
          if (flag)
          {
            ans ++;
            bool mark = true;
            for (int ad = 1; ad < 4 && mark; ad ++)
            {
              int dd = (dir + ad) % 4;
              pi = i; pj = j;
              pi += dx[dd]; pj += dy[dd];
              while (mark &&
                  pi >= 0 && pj >= 0 && pi < r && pj < c)
              {
                if (map[pi][pj] != '.') mark = false;
                pi += dx[dd]; pj += dy[dd];
              }
            }
            if (mark) ip = true;
          }
        }
    if (ip) cout << "IMPOSSIBLE" << endl;
    else  cout << ans << endl;
  }
  return 0;
}

          
