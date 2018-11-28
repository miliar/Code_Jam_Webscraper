#include <cstdio>

int R, C;
bool p[20][20]; // false : /, true : \ //
int mp[40][40];
int dir[4][2] = {-1, 0, 0, -1, 0, 1, 1, 0};

int initdir[100], initx[100], inity[100];
int dir_false[4] = {2, 3, 0, 1};
int dir_true[4] = {1, 0, 3, 2};

int ans[100];
int go[100];

void sim(){
  for(int n = 1; n <= 2 * (R + C); n++){
    int x = initx[n], y = inity[n];
    int d = initdir[n];

    x += dir[d][0]; y += dir[d][1];

    int res = -1;

    for(;;){
      if(x == 0 || x == 2 * R || y == 0 || y == 2 * C){
        res = mp[x][y];
        break;
      }
      if(x % 2 == 1 && y % 2 == 1){ // mirror
        if(p[x / 2][y / 2]) d = dir_true[d];
        else d = dir_false[d];
      }

      x += dir[d][0]; y += dir[d][1];
    }

    go[n] = res;
  }
}

int main(){
  int T; scanf("%d", &T);
  for(int tt = 1; tt <= T; tt++){
    scanf("%d%d", &R, &C);

    for(int i = 0; i < 40; i++) for(int j = 0; j < 40; j++) mp[i][j] = 0;

    for(int i = 0; i < C; i++){
      int v = i + 1;
      mp[0][i * 2 + 1] = v;
      initdir[v] = 3;
      initx[v] = 0;
      inity[v] = i * 2 + 1;
    }
    for(int i = 0; i < R; i++){
      int v = i + C + 1;
      mp[i * 2 + 1][2 * C] = v;
      initdir[v] = 1;
      initx[v] = i * 2 + 1;
      inity[v] = 2 * C;
    }
    for(int i = 0; i < C; i++){
      int v = i + C + R + 1;
      mp[2 * R][2 * C - 2 * i - 1] = v;
      initdir[v] = 0;
      initx[v] = 2 * R;
      inity[v] = 2 * C - 2 * i - 1;
    }
    for(int i = 0; i < R; i++){
      int v = i + C + R + C + 1;
      mp[2 * R - 2 * i - 1][0] = v;
      initdir[v] = 2;
      initx[v] = 2 * R - 2 * i - 1;
      inity[v] = 0;
    }

    for(int n = 0; n < R + C; n++){
      int x, y; scanf("%d%d", &x, &y);
      ans[x] = y; ans[y] = x;
    }

    int N = R * C;
    bool found = false;

    for(int n = 0; n < (1 << N); n++){
      int n_ = n;
      for(int i = 0; i < R; i++){
        for(int j = 0; j < C; j++){
          p[i][j] = n_ % 2;
          n_ /= 2;
        }
      }

      sim();

      bool mat = true;
      for(int i = 1; i <= 2 * (R + C); i++){
        if(ans[i] != go[i]) mat = false;
      }

      if(mat){ found = true; break; }
    }

    printf("Case #%d:\n", tt);

    if(found){
      for(int i = 0; i < R; i++){
        for(int j = 0; j < C; j++) printf("%c", p[i][j] ? '\\' : '/');
        printf("\n");
      }
    }
    else puts("IMPOSSIBLE");
  }
  return 0;
}
