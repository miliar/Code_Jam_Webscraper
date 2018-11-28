#include<bits/stdc++.h>

#define REP(i,s,n) for(int i=s;i<n;i++)
#define rep(i,n) REP(i,0,n)
#define MAX 60
#define IINF (INT_MAX)

using namespace std;

int R,C,M;
bool used[MAX][MAX];
char G[MAX][MAX];
int cell[MAX][MAX];
const string N = "Impossible";
int dx[] = {+0,+1,+1,+1,+0,-1,-1,-1};
int dy[] = {-1,-1,+0,+1,+1,+1,+0,-1};
int dx4[] = {1,0,-1,0};
int dy4[] = {0,1,0,-1};
int bc[1<<26];

inline bool isValid(int x,int y){
  return ( 0 <= x && x < C && 0 <= y && y < R );
}

inline bool check(int sx,int sy){
  rep(i,R)rep(j,C)used[i][j]=false;
  used[sy][sx] = true;
  deque<int> deq;
  deq.push_back(sx+sy*C);
  while(!deq.empty()){
    int cur = deq.front(); deq.pop_front();
    int x = cur % C, y = cur / C;
    if( cell[y][x] != 0 ) continue;
    rep(i,8){
      int nx = x + dx[i], ny = y + dy[i];
      if( !isValid(nx,ny) ) continue;
      if( used[ny][nx] ) continue;
      used[ny][nx] = true;
      deq.push_back(nx+ny*C);
    }
  }
  rep(i,R)rep(j,C)if( G[i][j] != '*' && !used[i][j] ) return false;
  return true;
}

int main(){
  int T,CNT = 1;
  rep(state,(1<<25))bc[state] = __builtin_popcount(state);
  cin >> T;
  while(T--){
    cin >> R >> C >> M;
    cout << "Case #" << CNT++ << ":" << endl;


    int remain1 = M;
    int remain2 = R * C - M;
    char c1 = '*';
    char c2 = '.';

    if( remain1 > remain2 ){
      swap(remain1,remain2);
      swap(c1,c2);
    }

    bool found = false;
    rep(state,(1<<(R*C))){
      if( bc[state] != remain1 ) continue;
      rep(i,R)rep(j,C){
	if( (state>>(j+i*C)) & 1 ) G[i][j] = c1;
	else                       G[i][j] = c2;
      }

      rep(i,R)rep(j,C)if(G[i][j]=='.'){
	int cost = 0;
	rep(k,8){
	  int x = j + dx[k], y = i + dy[k];
	  if( !isValid(x,y) ) continue;
	  if( G[y][x] == '*' ) cost++;
	}
	cell[i][j] = cost;
      }

      rep(i,R)rep(j,C)if(G[i][j]=='.')if(check(j,i)){
	  found = true;
	  G[i][j] = 'c';
	  goto Fin;
	}
    }

  Fin:;
    if( !found ) cout << N << endl;
    else{
      rep(i,R){
	rep(j,C)cout << G[i][j];
	cout << endl;
      }
    }

  }
  return 0;
}
