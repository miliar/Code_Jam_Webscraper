#include <iostream>
#include <string>
#include <vector>
using namespace std;

int X, Y;
vector<string> g;

int dx[4] = {0, -1, 0, 1};
int dy[4] = {1, 0, -1, 0};
struct Courtier {
  int i, x, y, d, match;
  Courtier(int i, int x, int y, int d)
    : i(i), x(x), y(y), d(d), match(0) {}
};
vector<Courtier> c;

int main() {
  int i, T, prob=1;
  for (cin >> T; T--;) {
    cin >> Y >> X;
    cout << "Case #" << prob++ << ":" << endl;

    g = vector<string>(Y, string(X, '.'));
    c = vector<Courtier>();
    i = 1;
    for (int x = 0; x < X; x++) c.push_back(Courtier(i++, x, -1, 0));
    for (int y = 0; y < Y; y++) c.push_back(Courtier(i++, X, y, 1));
    for (int x = X-1; x >= 0; x--) c.push_back(Courtier(i++, x, Y, 2));
    for (int y = Y-1; y >= 0; y--) c.push_back(Courtier(i++, -1, y, 3));
    for (i = 0; i < X+Y; i++) {
      int a, b;
      cin >> a >> b;
      c[a-1].match = b;
      c[b-1].match = a;
    }

    while (c.size()) {
      for (i = 0; i < c.size(); i++) {
        Courtier& c1 = c[i];
        Courtier& c2 = c[(i+1)%c.size()];
        if (c1.match == c2.i) {
//cout << c1.i << ' ' << c1.x << ' ' << c1.y << ' ' << c1.d << endl;
          for (;;) {
            c1.x += dx[c1.d];
            c1.y += dy[c1.d];
//cout << c1.i << ' ' << c1.x << ' ' << c1.y << ' ' << c1.d << endl;
            if (c1.x == c2.x && c1.y == c2.y) break;
            if (c1.x < 0 || c1.x >= X || c1.y < 0 || c1.y >= Y) goto fail;
            if (g[c1.y][c1.x] == '.') {
              g[c1.y][c1.x] = (c1.d&1) ? '/' : '\\';
            }
            if (g[c1.y][c1.x] == '/') {
              c1.d ^= 1;
            } else if (g[c1.y][c1.x] == '\\') {
              c1.d ^= 3;
            }
          }
          int i1 = c1.i, i2 = c2.i;
          for (int j = 0; j < c.size(); j++)
            if (c[j].i == i1 || c[j].i == i2) {
              c.erase(c.begin()+j--);
            }
          i = -1;
          break;
        }
      }
      if (i == c.size()) goto fail;
    }

fail:;
    if (c.size()) {
      cout << "IMPOSSIBLE" << endl;
    } else {
      for (int y = 0; y < Y; y++)
      for (int x = 0; x < X; x++)
        if (g[y][x] == '.') g[y][x] = '/';
      for (int y = 0; y < Y; y++) cout << g[y] << endl;
    }
  }
}
