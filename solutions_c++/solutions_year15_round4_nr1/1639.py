#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <iterator>
#define FOR(i,a,n) for(int i = (a); i < (int)(n); ++i)
#define foreach(itr,c) for(decltype((c).begin()) itr=(c).begin(); itr != (c).end(); itr++)
#define mp(a,b) make_pair(a,b)

using namespace std;

//typedef __int64 ll;
//typedef unsigned __int64 ull;
typedef long long ll;
typedef unsigned long long ull;


template<typename T>
inline T ABS(T a) { return a > 0 ? a : -a; }
template<typename T>
inline T MIN(T a, T b) { return a < b ? a : b; }
template<typename T>
inline T MAX(T a, T b) { return a > b ? a : b; }
template<typename T>
inline T CHKMIN(T &a, T b) { if(a > b) a = b; return a; }
template<typename T>
inline T CHKMAX(T &a, T b) { if(a < b) a = b; return a; }
template<typename T>
inline void SWAP(T &a, T &b) { static T c; c = a; a = b; b = c; }

template<typename T, typename... T0>
T MAX(T a, T b, T0... c) { return a > b ? MAX(a, c...) : MAX(b, c...); }
template<typename T, typename... T0>
T MIN(T a, T b, T0... c) { return a < b ? MIN(a, c...) : MIN(b, c...); }

template<typename T, int n>
void myin(T a[]) { FOR(i, 0, n) cin >> a[i]; }
template<typename T>
void myin(T &a) { cin >> a; }

template<typename T>
void print(T a) { cout << a << ' '; }
template<typename T, typename... T0>
void print(T a, T0... b) { print(a); print(b...); }
template<typename T>
void println(T a) {cout << a << endl;}
template<typename T, typename... T0>
void println(T a, T0... b) { print(a); println(b...); }

char in[110][110];
int r, c;
int mark[110][110], num[10010], rn[110], cn[110], now;
int points[10010][2], top;

int dir[4][2] = {-1, 0, 0, -1, 1, 0, 0, 1};

int c2d(char x) {
  switch(x) {
  case '^': return 0; 
  case '<': return 1;
  case 'v': return 2;
  case '>': return 3;
  }
}

void push(int x, int y) {
  points[top][0] = x;
  points[top][1] = y;
  top++;
}

void pop() {
  top--;
}

void mkall(int m) {
  FOR(i, 0, top) {
    int x = points[i][0];
    int y = points[i][1];
    mark[x][y] = m;
  }
}

void dfs(int x, int y) {
  top = 0;
  push(x, y);
  mark[x][y] = now;
  
  int d = c2d(in[x][y]);
  int dx = dir[d][0], dy = dir[d][1];
  int nx = x + dx, ny = y + dy;
  
  while(1) {
    while(0 <= nx && nx < r && 0 <= ny && ny < c && in[nx][ny] == '.') {
      nx = nx + dx, ny = ny + dy;
    }
    //println("xy", x, y, nx, ny);

    if(!(0 <= nx && nx < r && 0 <= ny && ny < c)) break;
    
    if(mark[nx][ny] != 0) {
      //println("mkall", mark[nx][ny]);
      if(mark[nx][ny] != now) mkall(mark[nx][ny]);
      else mkall(-1);
      return;
    }
    
    x = nx, y = ny;
    push(x, y);
    mark[x][y] = now;
    d = c2d(in[x][y]);
    dx = dir[d][0], dy = dir[d][1];
    nx = x + dx, ny = y + dy;
  }
  now++;
  return;
}

#define FILEIO 
#define FILENAME "A-large"

int main() {

#ifdef FILEIO
  freopen( FILENAME ".in", "r", stdin);
  freopen( FILENAME ".out", "w", stdout);
#endif

  int tt;
  cin >> tt;
  FOR(t, 1, tt + 1) {
    cin >> r >> c;
    FOR(i, 0, r) {
      cin >> in[i];
    }
    memset(mark, 0, sizeof(mark));
    now = 1;
    
    FOR(i, 0, r) FOR(j, 0, c) {
      if(in[i][j] == '.') continue;
      if(mark[i][j] != 0) continue;
      dfs(i, j);
    }
    /*
    FOR(i, 0, r) {
      FOR(j, 0, c) printf("%d ", mark[i][j]); puts("");
    }
    */
    memset(num, 0, sizeof(num));
    FOR(i, 0, r) rn[i] = 0;
    FOR(i, 0, c) cn[i] = 0;
    FOR(i, 0, r) FOR(j, 0, c) {
      if(in[i][j] == '.') continue;
      rn[i]++;
      cn[j]++;
      if(mark[i][j] > 0) {
        int k = mark[i][j];
        points[k][0] = i;
        points[k][1] = j;
        num[k]++;
      }
    }
    //FOR(i, 1, now) printf("%d ", num[i]); puts("");
    int ans = now;
    FOR(k, 1, now) {
      if(num[k] > 1) continue;
      int x = points[k][0], y = points[k][1];
      if(rn[x] == 1 && cn[y] == 1) {
        ans = -1;
        break;
      }
    }
    printf("Case #%d: ", t);
   if(ans == -1) puts("IMPOSSIBLE");
   else printf("%d\n", now - 1);
  }
  return 0;
}
/*
99
4 4
.>>>
>...
>...
.>>>
*/
