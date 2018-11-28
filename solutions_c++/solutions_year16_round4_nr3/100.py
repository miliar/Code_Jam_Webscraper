#include <bits/stdc++.h>

#define FOR(i,a,b) for (int i = (int)(a); i < (int)(b); ++i)
#define REP(i,n) FOR(i,0,n)
#define pb push_back
#define x first
#define y second

#define TRACE(x) cerr << #x << " = " << x << endl
#define _ << " _ " <<

using namespace std;

typedef long long ll;
typedef pair < int, int > pii;

const int dx[] = {-1, 0, 1, 0};
const int dy[] = {0, 1, 0, -1};

int r, c;
int p[205];

int nxt[205];

char mat[205][205];

bool check(){

  //REP(i,r){REP(j,c) cout << mat[i][j]; cout << endl;}
  REP(i,2*r+2*c){
    int x, y, d;
    if (i < c) x = 0, y = i, d = 0;
    else if (i < c+r) x = i-c, y = c-1, d = 1;
    else if (i < 2*c+r) x = r-1, y = 2*c+r-i-1, d = 2;
    else x = 2*c+2*r-i-1, y = 0, d = 3;
    //TRACE(i _ x _ y _ d);
    while (x >= 0 && y >= 0 && x < r && y < c){
      //TRACE(x _ y _ d);
      if (mat[x][y] == '/'){d ^= 3;}
      else {d ^= 1;}
      //TRACE(x _ y _ d);
      x += dx[d], y += dy[d];
      d ^= 2;
      //TRACE(x _ y _ d);
    }
    int id = -1;
    if (x == -1) id = y;
    if (y == -1) id = 2*c+2*r-x-1;
    if (x == r) id = r+2*c-y-1;
    if (y == c) id = x+c; assert(id != -1);
    //TRACE(i _ 111 _ x _ y);
    if (nxt[i+1] != id+1) return false;
  } return true;
  
}

void solve(){

  cin >> r >> c;
  REP(i,2*r+2*c) cin >> p[i];
  REP(i,2*r+2*c) nxt[p[i]] = p[i^1];

  assert(r*c <= 16);
  REP(i,1<<(r*c)){
    REP(a,r) REP(b,c) if ((i>>(a*c+b))&1) mat[a][b] = '/'; else mat[a][b] = '\\';
    /*if (r == 1 && c == 3){
      mat[0][0] = mat[0][1] = '/';
      mat[0][2] = '\\';
      TRACE(check());
      exit(0);
      }*/
    if (check()){
      REP(a,r){REP(b,c) cout << mat[a][b]; cout << endl;}
      return;
    }
  } cout << "IMPOSSIBLE\n";
  
}

int main(){

  int t;
  cin >> t;
  REP(i,t) cout << "Case #" << i+1 << ": \n", solve();

  return 0;
}
