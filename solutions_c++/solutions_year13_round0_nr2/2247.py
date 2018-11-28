#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cfloat>
#include <climits>
#include <cctype>
#include <cmath>
#include <cassert>
#include <ctime>

#include <iostream>
#include <iomanip>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <bitset>
#include <complex>
#include <limits>
#include <functional>
#include <numeric>

#define rep(x,n) for(int x = 0; x < n; ++x)
#define print(x) cout << x << endl
#define dbg(x) cerr << #x << " == " << x << endl
#define _ << " , " <<
#define mp make_pair
#define x first
#define y second

using namespace std;

template<class T> void pv(T a, T b) { for (T i = a; i != b; ++i) cout << *i << " "; cout << endl; }

typedef long long ll;
typedef pair<int,int> pii;

int board[111][111];
int n,m;

int main() {
  int T; cin>>T;
  for(int testcase=1;testcase<=T;testcase++) {
    cin>>n>>m;
    rep(i,n) rep(j,m) cin>>board[i][j];
    int ok=1;
    if(n>1&&m>1) for(int k=100;k>=1;k--) {
      int _board[111][111]={0};
      rep(i,n) rep(j,m) if(board[i][j]<=k) _board[i][j]=1;
      rep(i,n) {
        int line=1;
        rep(j,m) if(_board[i][j]==0) line=0;
        if(line) rep(j,m) _board[i][j]=-1;
      }
      rep(j,m) {
        int column=1;
        rep(i,n) if(_board[i][j]==0) column=0;
        if(column) rep(i,n) _board[i][j]=-1;
      }
      rep(i,n) rep(j,m) if(_board[i][j]>0) ok=0;
    }
    printf("Case #%d: %s\n",testcase, ok?"YES":"NO");
  }
  return 0;
}
