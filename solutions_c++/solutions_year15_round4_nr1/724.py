#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int,int> P;
const ll INF = 5000000000;
#define PB push_back
#define sz(a) (a).size()
#define reps(i,n,m) for(int (i)=(n);(i)<(m);++(i))
#define rep(i,n) reps(i,0,n)
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};
ll T;
string mp[110];
int r, c;
bool valid(int x,int y){
  return 0<= x && x < r && 0 <= y && y < c;
}

bool exist(int x, int y, int d) {
  int nx=x+dx[d], ny=y+dy[d];

  while(valid(nx, ny)){
    if(mp[nx][ny] != '.')
      return true;
    nx += dx[d];
    ny += dy[d];
  }
  return false;

}
int main(){
  cin >> T;
  reps(times, 1, T+1) {
    cin >> r >> c;
    rep(i, r){
      cin >> mp[i];
    }
    int ans = 0;
    int flg = 1;
    rep(i, r){
      rep(j, c) {
        if (mp[i][j] == '.') {
          continue;
        }
        int dir = 0;
        switch(mp[i][j]) {
        case '^':
          dir = 0;
          break;
        case '>':
          dir = 1;
          break;
        case 'v':
          dir = 2;
          break;
        case '<':
          dir = 3;
          break;
        }
        if (exist(i, j, dir)) {
          continue;
        }
        flg = 0;
        rep(k, 4){
          if(exist(i,j, k)) {
            flg = 1;
            ans ++;
            break;
          }
        }
        if(flg==0)goto END;
      }
    }
  END:
    if (flg == 0) {
      printf("Case #%d: IMPOSSIBLE\n", times);
    } else {
      printf("Case #%d: %d\n", times, ans);
    }
  }

}
