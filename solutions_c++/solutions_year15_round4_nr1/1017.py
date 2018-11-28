#include <cstdio>
#include <cmath>
#include <cstring>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#include <sstream>
#include <typeinfo>
#include <fstream>

using namespace std;

#define dbg(x) cout << #x << " = " << x << endl; 

int r, c;
string a[110];
char dir[] = {'>', '<', 'v', '^'};


void get_direction(char c, int &dx, int &dy) {
  if (c == '>') {
    dx = 0;
    dy = 1;
  } else if (c == '<') {
    dx = 0;
    dy = -1;
  } else if (c == 'v') {
    dx = 1;
    dy = 0;
  } else if (c == '^') {
    dx = -1;
    dy = 0;
  }
}


bool is_in_board(int x, int y) {
  return x > -1 && y > -1 && x < r && y < c;
}


bool is_direction_good(int i, int j, char c) {
  int dx, dy;
  get_direction(c, dx, dy);
  int x = i, y = j;
  x += dx; y += dy;
  while (is_in_board(x, y) && a[x][y] == '.') {
    x += dx; y += dy;
  }
  return (is_in_board(x, y));
}


int main()
{
    freopen("in", "r", stdin);
    //freopen("out", "w", stdout);
    int t;
    cin >> t;
    for (int tc = 1; tc <= t; tc++) {
        cout << "Case #" << tc << ": ";

        cin >> r >> c;
        for (int i = 0; i < r; i++) {
          cin >> a[i];
        }

        bool impossible = false;
        int ans = 0;

        for (int i = 0; i < r; i++) {
          for (int j = 0; j < c; j++) {
            if (a[i][j] != '.') {
              if (!is_direction_good(i, j, a[i][j])) {
                bool ok = false;
                for (int e = 0; e < 4; e++) {
                  if (is_direction_good(i, j, dir[e])) {
                    ok = true;
                    a[i][j] = dir[e];
                    break;
                  }
                }
                if (!ok) {
                  impossible = true;
                  break;
                }
                ans++;
              }
            }
          }
          if (impossible) break;
        }
        if (impossible) {
          cout << "IMPOSSIBLE";
        } else {
          cout << ans;
        }

        cout << endl;
    }
    return 0;
}
