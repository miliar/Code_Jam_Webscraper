#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
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
#include <string>
#include <cstring>
#include <climits>
#include <queue>
using namespace std;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef long long LL;
#define ALL(a)  (a).begin(),(a).end()
#define RALL(a) (a).rbegin(), (a).rend()
#define PB push_back
#define MP make_pair
#define SZ(a) int((a).size())
#define SORT(c) sort((c).begin(),(c).end())
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n)  FOR(i,0,n)
const double EPS = 1e-10;
const double PI  = acos(-1.0);
const int INF = 1000000;

int H, W;
char DIR[5] = "^>v<";
int dy[4] = {-1,0,1,0};
int dx[4] = {0,1,0,-1};

bool isin(int x, int y){
  return 0 <= x && x < W && 0 <= y && y < H;
}

int check(VS& vs, int x, int y){
  if(vs[y][x] == '.'){
	return 0;
  }
  int did, ppy = -1, ppx = -1, py = y, px = x;
  for(did=0;;++did) if(DIR[did] == vs[y][x]) break;

  vector<vector<bool>> vis(H, vector<bool>(W, false));
  while(!vis[y][x]){
	vis[y][x] = true;
	x += dx[did]; y += dy[did];
	if(!isin(x,y)) break;
	if(vs[y][x] != '.'){
	  for(did=0;;++did) if(DIR[did] == vs[y][x]) break;
	  ppy = py, ppx = px;
	  py = y, px = x;
	}
  }
  if(isin(x,y)) return true;
  if(ppy < 0) return INF;

  char c;
  if(ppx == px){
	if(ppy < py) c = 'v';
	else c = '^';
  }
  else{
	if(ppx < px) c = '<';
	else c = '>';
  }
  vs[py][px] = c;
  return 1;
}

/*
int dfs(VS& vs, int i, int j){
  if(i == H) return (check(vs)? 0: INF);
  if(j == W) return dfs(vs, i+1, 0);
  if(vs[i][j] == '.') return dfs(vs, i, j+1);
  char ch = vs[i][j];
  int res = INF;
  REP(d,4){
	vs[i][j] = DIR[d];
	res = min(res, dfs(vs, i, j+1) + (ch != DIR[d]));
  }
  vs[i][j] = ch;

  return res;
}
*/
int solve(VS& vs){
  int res = 0;
  REP(y,H) REP(x,W){
	if(vs[y][x] == '.') continue;
	res += check(vs,x,y);
	res = min(res, INF);
  }
  return res;
}

int id(int x, int y){
  return x + y*W;
}

int main(){
  cin.tie(0);
  ios_base::sync_with_stdio(false);

  int T; cin >> T;
  FOR(t,1,T+1){
	cin >> H >> W;
	VS vs(H); REP(i,H) cin >> vs[i];

	int SZ = 1;
	VVI G(H*W+1);
	VVI idx(H, VI(W, -1));
	VI in(H*W+1, 0);
	REP(y,H) REP(x,W){
	  if(vs[y][x] == '.') continue;
	  if(idx[y][x] < 0) idx[y][x] = SZ++;
	  int did;
	  for(did=0;;++did) if(DIR[did] == vs[y][x]) break;
	  int tx = x, ty = y;
	  while(true){
		tx += dx[did]; ty += dy[did];
		if(!isin(tx,ty)) break;
		if(vs[ty][tx] != '.'){
		  if(idx[ty][tx] < 0) idx[ty][tx] = SZ++;
		  break;
		}
	  }
	  if(!isin(tx,ty))
		G[idx[y][x]].PB(0);
	  else{
		G[idx[y][x]].PB(idx[ty][tx]);
	  }

	  REP(d,4){
		tx = x + dx[d], ty = y + dy[d];
		while(isin(tx,ty) && vs[ty][tx] == '.'){
		  tx += dx[d]; ty += dy[d];
		}
		if(isin(tx,ty)){
		  in[idx[y][x]]++;
		}
	  }
	}

	int ans = 0;
	FOR(i,1,SZ){
	  bool ng = false;
	  for(auto to: G[i]) if(to == 0){ ng = true; break;}
	  if(ng){
		if(in[i] == 0)
		  ans = INF;
		else
		  ans++;
	  }
	}
		
	if(ans < INF)
	  cout << "Case #" << t << ": " << ans << endl;
	else
	  cout << "Case #" << t << ": " << "IMPOSSIBLE" << endl;
  }
  
  return 0;
}
