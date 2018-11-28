#include <bits/stdc++.h>
using namespace std;

#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define REP(i,n) for(int i=0;i<n;i++)
#define foreach(v,c) for(typeof(c.begin()) v=c.begin();v!=c.end();++v)
#define printA(a,l,r) for(int zzz49=l; zzz49!=r; zzz49++) cout << a[zzz49] << ((zzz49==r-1)?"\n":" ")

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef pair<int,int> pi;

#define maxn 120

int T,zz;

int dx[4] = {0,-1,0,1};
int dy[4] = {1,0,-1,0};
char dirs[5] = {'>','^','<','v','.'};
char grid[maxn][maxn];
int qgrid[maxn][maxn];
int R,C;

bool inb(const int &x, const int &y) {
  //cout << x << "," << y << endl;
  return x>=0 && y>=0 && x<R && y<C;
}

int go() {
  int cnt = 0;
  REP(i,R) REP(j,C) {
    int dir = qgrid[i][j];
    if (dir==4) continue;
    //cout << "testing " << i << "," << j << endl;
    int x=i,y=j;
    while (inb(x+=dx[dir],y+=dy[dir]) && qgrid[x][y]==4);
    if (inb(x,y)) continue;

    cnt++;
    bool good = false;
    REP(dir,4) {
      int x=i,y=j;
      while (inb(x+=dx[dir],y+=dy[dir]) && qgrid[x][y]==4);
      if (inb(x,y)) good = true;
    }
    if (!good) return -1;
  }
  return cnt;
}

int main() {
  cin >> T;
  for (int zz=1;zz<=T;zz++) {
    cin >> R >> C;
    REP(i,R) REP(j,C) cin >> grid[i][j];
    REP(dir, 5) REP(i,R) REP(j,C) if (grid[i][j] == dirs[dir]) qgrid[i][j]=dir;
    //    REP(i,R) printA(qgrid[i],0,C);
    int res = go();
    if (res==-1)
      cout << "Case #" << zz << ": " << "IMPOSSIBLE"<< endl;
    else
      cout << "Case #" << zz << ": " << res << endl;
  }
  return 0;
}
