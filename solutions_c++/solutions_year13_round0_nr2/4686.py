#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include<cassert>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include<bitset>

#define REP(i,b,n) for(int i=b;i<(int)n;i++)
#define rep(i,n)   REP(i,0,n)
#define ALL(C)     (C).begin(),(C).end()
#define FOR(it,o)  for(__typeof((o).begin()) it=(o).begin(); it!=(o).end(); ++it)
#define dbg(x) cout << __LINE__ << ' ' << #x << " = " << (x) << endl


typedef long long ll;

using namespace std;

const int N = 100;

int goal[N][N];

int R, C;

int getR(int r){
  int ret = 0;
  rep(i, C){
    ret = max(ret, goal[r][i]);
  }
  return ret;
}

int getC(int c){
  int ret = 0;
  rep(i, R){
    ret = max(ret, goal[i][c]);
  }
  return ret;
}

class State{
public:
  int t[N][N];
  State(){
    rep(i, N)rep(j, N)t[i][j] = 100;
  }
  bool solve(){
    rep(i, R){
      int tmp = getR(i);
      rep(j, C){
	t[i][j] = min(t[i][j], tmp);
      }
    }
    rep(j, C){
      int tmp = getC(j);
      rep(i, R){
	t[i][j] = min(t[i][j], tmp);
      }
    }
    rep(i, R){
      rep(j, C){
	if(t[i][j] != goal[i][j])return false;
      }
    }
    return true;
  }
};

int main(){
  int T;
  cin >> T;
  rep(tc, T){
    cout << "Case #" << tc+1<<": " << flush;
    cin >> R >> C;
    rep(i, R){
      rep(j, C){
	cin >> goal[i][j];
      }
    }
    State s;
    if(s.solve())cout << "YES" << endl;
    else cout << "NO" << endl;
  }
  return 0;
}
