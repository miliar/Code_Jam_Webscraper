#include <iostream>
#include <iomanip>
#include <vector>
#include <stack>
#include <algorithm>

using namespace std;

struct St
{
  int river[100][500];
};

struct Solve
{
  int W, H, B;
  St S;

  Solve()
  {
    cin >> W >> H >> B;
    for (int x = 0; x < W; x++) {
      for (int y = 0; y < H; y++) {
        S.river[x][y] = 0;
      }
    }
    for (int b = 0; b < B; b++) {
      int x0, x1, y0, y1;
      cin >> x0 >> y0 >> x1 >> y1;
      for (int x = x0; x <= x1; x++) {
        for (int y = y0; y <= y1; y++) {
          S.river[x][y] = -1;
        }
      }
    }
    /*
    for (int x = 0; x < W; x++) {
      if (S.river[x][0] == 0) {
        S.river[x][0] = 2;
      }
    }
    */
  }

  int solve()
  {
    int count = 0;

    for (int x = 0; x < W; x++) {
      if (find_route(x, 0, 0, 1)) {
        count++;
      }
    }
    return count;
  }

  bool find_route(int x, int y, int dx, int dy)
  {
    if (x < 0 || x >= W || y < 0 || y >= H) return false;
    if (S.river[x][y] != 0) return false;

    S.river[x][y] = 1;

    //cout << x << ", " << y << endl;
    if (y == H - 1) return true;

    if (find_route(x - dy, y + dx, -dy, dx)) return true;
    if (find_route(x + dx, y + dy, dx, dy)) return true;
    if (find_route(x + dy, y - dx, dy, - dx)) return true;
    return false;
  }

};

int main()
{
  int T;

  cin >> T;

  for (int cas = 1; cas <= T; cas++) {
    Solve s;
    cout << "Case #" << cas << ": " << s.solve() << endl;
  }

  return 0;
}
