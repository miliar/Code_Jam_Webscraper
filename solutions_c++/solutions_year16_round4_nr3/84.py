#define REP(i,n) for(int i=0; i<(int)(n); i++)

#include <cstdio>
inline int getInt(){ int s; scanf("%d", &s); return s; }

#include <set>

using namespace std;


const int Up = 0;
const int Right = 1;
const int Down = 2;
const int Left = 3;

const int dx[4] = { 0, 1, 0, -1 };
const int dy[4] = { -1, 0, 1, 0 };

int nextDir(int dir, char wall) {
  if(dir == Up) {
    if(wall == '/') return Right;
    else if(wall == '\\') return Left;
  } else if(dir == Right) {
    if(wall == '/') return Up;
    else if(wall == '\\') return Down;
  } else if(dir == Down) {
    if(wall == '/') return Left;
    else if(wall == '\\') return Right;
  } else if(dir == Left) {
    if(wall == '/') return Down;
    else if(wall == '\\') return Up;
  }
  throw 0;
}

char g[32][32];
int h, w;
int a[32];
int b[32];

int dfs(int x, int y, int dir) {
  const int next = nextDir(dir, g[y][x]);

  const int xx = x + dx[next];
  const int yy = y + dy[next];

  if(xx == -1) {
    return w + h + w + (h - 1 - yy);
  } else if(xx == w) {
    return w + yy;
  } else if(yy == -1) {
    return xx;
  } else if(yy == h) {
    return w + h + (w - 1 - xx);
  }

  return dfs(xx, yy, next);
}

int check(int pos) {
  // printf("%d(%d %d): ", pos, w, h);
  if(pos < w) {
    // printf("%d %d %d !1\n", pos, 0, Down);
    return dfs(pos, 0, Down);
  } else if(pos < w + h) {
    const int p = pos - w;
    // printf("%d %d %d !2\n", w - 1, p, Left);
    return dfs(w - 1, p, Left);
  } else if(pos < w + h + w) {
    const int p = pos - (w + h);
    // printf("%d %d %d !3\n", w - 1 - p, h - 1, Up);
    return dfs(w - 1 - p, h - 1, Up);
  } else {
    const int p = pos - (w + h + w);
    // printf("%d %d %d !4\n", 0, h - 1 - p, Right);
    return dfs(0, h - 1 - p, Right);
  }
}

bool ok() {
  REP(i,h+w) {
    const int bb = check(a[i]);
    const int aa = check(b[i]);
    // printf("%d => %d : %d => %d\n", a[i] + 1, bb + 1, b[i] + 1, aa + 1);
    if(!(aa == a[i] && bb == b[i])) return false;
  }
  return true;
}

int main(){
  const int T = getInt();
  REP(t, T) {
    h = getInt();
    w = getInt();
    const int n = h * w;

    REP(i,h+w) {
      a[i] = getInt() - 1;
      b[i] = getInt() - 1;
    }

    bool ans = false;
    REP(i,1<<n) {
      REP(y,h) {
	REP(x,w) {
	  const int p = y * w + x;
	  if((i & (1 << p)) == 0) {
	    g[y][x] = '/';
	  } else {
	    g[y][x] = '\\';
	  }
	}
	g[y][w] = '\0';
      }

      // REP(i,h) puts(g[i]);
      if(ok()) {
	ans = true;
	break;
      }
    }

    printf("Case #%d:\n", t + 1);
    if(ans) {
      REP(i,h) puts(g[i]);
    } else {
      puts("IMPOSSIBLE");
    }
  }


}










