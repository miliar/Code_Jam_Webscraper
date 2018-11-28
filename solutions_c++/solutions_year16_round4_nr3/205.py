#define NDEBUG
#include <cassert>
#include <cstring>
#include <iostream>
#include <map>
using namespace std;

#define repeat(n) for (int repc = (n); repc > 0; --repc)
template <typename T> inline int get_bit(const T &x, int index) {
  return int((x >> index) & 1);
}
#define ZERO(v) memset((v), 0, sizeof (v))

const int MAXN = 35;

struct Point {
  int y, x;
};
enum Direction { DR, DL, UL, UR };
Point next(Point p, Direction d) {
  int dy = d == DR || d == DL ? 1 : -1;
  int dx = d == DL || d == UL ? -1 : 0;
  return Point{p.y + dy, p.x + dx + (p.y%2==0)};
}

int R, C;
int num[MAXN][MAXN];
bool graf[MAXN][MAXN][4];

void assign_nums() {
  ZERO(num);
  int next = 1;
  for (int x=0; x<C; ++x) num[0][x] = next++;
  for (int y=0; y<R; ++y) num[1+2*y][C] = next++;
  for (int x=C-1; x>=0; --x) num[2*R][x] = next++;
  for (int y=R-1; y>=0; --y) num[1+2*y][0] = next++;
  // for (int y=0; y<=2*R; ++y) {
  //   for (int x=0; x<C+y%2; ++x) {
  //     fprintf(stderr, "%c", num[y][x] != 0 ? '0'+num[y][x] : ' ');
  //   }
  //   fprintf(stderr, "\n");
  // }
}

void solve() {
  cin >> R >> C;
  map<int, int> lovers;
  repeat (R+C) {
    int a, b;
    cin >> a >> b;
    lovers[a] = b;
    lovers[b] = a;
  }
  assign_nums();
  for (int mask=0; mask<(1<<R*C); ++mask) {
    ZERO(graf);
    for (int y=0; y<R; ++y) {
      for (int x=0; x<C; ++x) {
        const Point s1{2*y, x};
        if (!get_bit(mask, y*C+x)) {
          Point s2 = next(s1, DR);
          graf[s1.y][s1.x][DR] = 1;
          graf[s2.y][s2.x][UL] = 1;
          Point s3 = next(s1, DL), s4 = next(s3, DR);
          graf[s3.y][s3.x][DR] = 1;
          graf[s4.y][s4.x][UL] = 1;
        } else {
          Point s2 = next(s1, DL);
          graf[s1.y][s1.x][DL] = 1;
          graf[s2.y][s2.x][UR] = 1;
          Point s3 = next(s1, DR), s4 = next(s3, DL);
          graf[s3.y][s3.x][DL] = 1;
          graf[s4.y][s4.x][UR] = 1;
        }
      }
    }

    map<int, int> dest;
    for (int y=0; y<=2*R; ++y) {
      for (int x=0; x<C+y%2; ++x) {
        if (num[y][x] > 0) {
          Point p{y, x}, last{-5, -5};
          while (1) {
            int dir;
            for (dir=0; dir<4; ++dir) {
              Point n = next(p, (Direction)dir);
              if (graf[p.y][p.x][dir] && !(n.y == last.y && n.x == last.x)) {
                last = p;
                p = n;
                break;
              }
            }
            assert(dir < 4);
            if (num[p.y][p.x] > 0) {
              dest[num[y][x]] = num[p.y][p.x];
              break;
            }
          }
        }
      }
    }
    if (dest == lovers) {
      for (int y=0; y<R; ++y) {
        for (int x=0; x<C; ++x) {
          cout << "\\/"[get_bit(mask, y*C+x)];
        }
        cout << '\n';
      }
      return;
    }
  }
  cout << "IMPOSSIBLE" << endl;
}

int main() {
  ios_base::sync_with_stdio(false);

  int T;
  cin >> T;
  for (int tt=1; tt<=T; ++tt) { // caret here
    cout << "Case #" << tt << ":\n";
    solve();
    cout << flush;
  }
}
