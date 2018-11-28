#include <cstring>
#define REP(i,n) for(int i=0; i<(int)(n); i++)

#include <cstdio>
inline int getInt(){ int s; scanf("%d", &s); return s; }

#include <set>

using namespace std;

int w, h;
char g[128][128];
int f[128][128];
int in[128][128];

const int _dx[] = {0,1,0,-1};
const int _dy[] = {-1,0,1,0};
#define IN(x,s,g) ((x) >= (s) && (x) < (g))
#define ISIN(x,y,w,h) (IN((x),0,(w)) && IN((y),0,(h)))
int m[256];
const int inf = 100000000;

int dfs(int y, int x, int d, int cnt = 0){
  if(!ISIN(x, y, w, h)) return cnt < 2 ? inf : 1;
  // printf("%d %d %d %d (%c)\n", y, x, d, cnt, g[y][x]);
  if(f[y][x]) return 0;
  if(g[y][x] != '.'){
    f[y][x] = 1;
    d = m[(int)g[y][x]];
    cnt += 1;
    int ret = dfs(y + _dy[d], x + _dx[d], d, cnt);
    if(ret == inf){
      REP(i,4){
	ret = 1 + dfs(y + _dy[i], x + _dx[i], i, cnt);
	if(ret < inf) break;
      }
    }
    return ret;
  }else{
    return dfs(y + _dy[d], x + _dx[d], d, cnt);
  }
}

int main(){
  const int T = getInt();

  m['^'] = 0;
  m['>'] = 1;
  m['v'] = 2;
  m['<'] = 3;

  REP(t,T){
    h = getInt();
    w = getInt();

    REP(i,h) scanf("%s", g[i]);
    memset(in, 0, sizeof(in));
    memset(f, 0, sizeof(f));

    REP(i,h) REP(j,w){
      if(g[i][j] == '.') continue;
      const int d = m[(int)g[i][j]];

      int x = j + _dx[d];
      int y = i + _dy[d];

      while(ISIN(x, y, w, h)){
	if(g[y][x] != '.'){
	  in[y][x]++;
	  break;
	}

	x += _dx[d];
	y += _dy[d];
      }
    }

    // REP(i,h){ REP(j,w) printf("%d", in[i][j]); puts(""); }

    int ans = 0;
    REP(i,h) REP(j,w) if(g[i][j] != '.' && in[i][j] == 0){
      if(f[i][j]) continue;
      ans = min(inf, ans + dfs(i, j, m[(int)g[i][j]]));
    }

    // REP(i,h) puts(g[i]);

    printf("Case #%d: ", t + 1);
    if(ans >= inf) puts("IMPOSSIBLE");
    else printf("%d\n", ans);
  }

  return 0;
}










