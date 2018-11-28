#include <iostream>

using namespace std;

struct Click
{
  int i, j;
};

struct B
{
  int W, H;
  bool mine[50][50];

  bool ism(int i, int j) const
  {
    return 0 <= i && i < H && 0 <= j && j < W && mine[i][j];
  }

  void recur(bool (&x)[50][50], int (&c)[50][50], int i, int j) const
  {
    if (0 <= i && i < H && 0 <= j && j < W) {
      if (x[i][j]) return;
      x[i][j] = true;
      if (c[i][j] == 0) {
        recur(x, c, i-1, j-1);
        recur(x, c, i-1, j);
        recur(x, c, i-1, j+1);
        recur(x, c, i,   j-1);
        recur(x, c, i,   j+1);
        recur(x, c, i+1, j-1);
        recur(x, c, i+1, j);
        recur(x, c, i+1, j+1);
      }
    }
  }

  bool check(Click& ret) const
  {
    int c[50][50];
    ret.i = -1;
    ret.j = -1;
    int minn = 10;

    for (int i = 0; i < H; i++) {
      for (int j = 0; j < W; j++) {
        if (ism(i, j)) {
          c[i][j] = 10;
        } else {
          c[i][j] = 0;
          if (ism(i-1, j-1)) c[i][j]++;
          if (ism(i-1, j))   c[i][j]++;
          if (ism(i-1, j+1)) c[i][j]++;
          if (ism(i,   j-1)) c[i][j]++;
          if (ism(i,   j+1)) c[i][j]++;
          if (ism(i+1, j-1)) c[i][j]++;
          if (ism(i+1, j))   c[i][j]++;
          if (ism(i+1, j+1)) c[i][j]++;
          if (c[i][j] < minn) {
            minn = c[i][j];
            ret.i = i;
            ret.j = j;
          }
        }
      }
    }
    if (minn == 10) return false;
    bool x[50][50];
    for (int i = 0; i < H; i++) {
      for (int j = 0; j < W; j++) {
        x[i][j] = false;
      }
    }
    recur(x, c, ret.i, ret.j);
    for (int i = 0; i < H; i++) {
      for (int j = 0; j < W; j++) {
        if (!mine[i][j] && !x[i][j]) return false;
      }
    }
    return true;
  }
};

struct Anser
{
  bool found;
  Click c;
  B b;
};

Anser answer[6][6][25];

void solve(int H, int W)
{
  int n = H * W;

  for (int idx = 0; idx < (1 << n); idx++) {
    B b;
    b.H = H;
    b.W = W;

    int k = idx;
    int N = 0;
    for (int i = 0; i < H; i++) {
      for (int j = 0; j < W; j++) {
        b.mine[i][j] = k & 1;
        if (k & 1) N++;
        k >>= 1;
      }
    }
    if (answer[H][W][N].found) continue;

    Click ck;
    if (b.check(ck)) {
      answer[H][W][N].found = true;
      answer[H][W][N].b = b;
      answer[H][W][N].c = ck;
    }
  }
}

void solve_all()
{
  for (int H = 1; H <= 5; H++) {
    for (int W = 1; W <= 5; W++) {
      solve(H, W);
    }
  }
}

int main()
{
  solve_all();

#if 1
  int T;
  cin >> T;
  
  for (int cas = 1; cas <= T; cas++) {
    int H, W, N;
    cin >> H >> W >> N;

    cout << "Case #" << cas << ":" << endl;
    if (answer[H][W][N].found) {
      Anser& a = answer[H][W][N];
      for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
          if (a.b.mine[i][j]) {
            cout << "*";
          } else if (a.c.i == i && a.c.j == j) {
            cout << "C";
          } else {
            cout << ".";
          }
        }
        cout << endl;
      }
    } else {
      cout << "Impossible" << endl;
    }
  }
#else

  int T = 0;
  for (int W = 1; W <= 5; W++) {
    for (int H = 1; H <= 5; H++) {
      T += W * H;
    }
  }
  cout << T << endl;

  int cas = 1;
  for (int W = 1; W <= 5; W++) {
    for (int H = 1; H <= 5; H++) {
      for (int N = 1; N < W * H; N++) {
#if 1
        cout << "Case #" << cas << ":" << endl;
        cas++;
        if (answer[H][W][N].found) {
          Anser& a = answer[H][W][N];
          for (int i = 0; i < H; i++) {
            for (int j = 0; j < W; j++) {
              if (a.b.mine[i][j]) {
                cout << "*";
              } else if (a.c.i == i && a.c.j == j) {
                cout << "C";
              } else {
                cout << ".";
              }
            }
            cout << endl;
          }
        } else {
          cout << "Impossible" << endl;
        }
#else
        cout << W << " " << H << " " << N << endl;
#endif
      }
    }
  }
#endif

  return 0;
}
