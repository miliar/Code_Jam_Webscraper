#include<bits/stdc++.h>
using namespace std;

#define CLR(a,x) memset(a,x,sizeof(a))
#define PB push_back
#define INF 1000000000
#define MOD 1000000007
#define MP make_pair
#define tr(container , it) for(typeof(container.begin()) it=container.begin() ; it!=container.end() ; it++)
#define FOR(i,a,b) for(i=a;i<b;i++)
#define REP(i,a) FOR(i,0,a)
#define LL long long
#define VI vector < int >
#define PII pair < int , int >
string board[128];
int n, m;
int dx[] = {1, 0, -1, 0};
int dy[] = {0, 1, 0, -1};
string arrows = "v>^<";

bool isin(int p, int q) {
  return p >= 0 && q >= 0 && p <= n+1 && q <= m+1;
}

int main() {
  int t;
  int kase = 1;
  scanf("%d",&t);
  while(t--) {
    scanf("%d%d",&n,&m);
    board[0] = board[n+1] = string(m+2, '*');
    for(int i=1;i<=n;i++) {
      cin>>board[i];
      board[i] = "*" + board[i] + "*";
    }
    bool flag = true;
    int ans = 0;
    for(int i=1;i<=n;i++) {
      for(int j=1;j<=m;j++) {
        if(board[i][j] == '.') {
          continue;
        }
        bool need = false;
        int total = 0;
        for(int dir=0;dir<4;dir++) {
          int curx = i + dx[dir];
          int cury = j + dy[dir];
          while(isin(curx, cury)) {
            if(board[curx][cury] == '*') {
              if(arrows[dir] == board[i][j]) {
                need = true;
              }
              total++;
              break;
            }
            if(board[curx][cury] != '.') {
              break;
            }
            curx += dx[dir];
            cury += dy[dir];
          }
        }
        if(total == 4) {
          flag = false;
          i = n+1;
          break;
        }
        if(need) {
          ans++;
        }
      }
    }
    if(flag) {
      cout<<"Case #"<<kase++<<": "<<ans<<endl;
    } else {
      cout<<"Case #"<<kase++<<": IMPOSSIBLE"<<endl;
    }
  }
  return 0;
}
