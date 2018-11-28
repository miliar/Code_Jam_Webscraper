//Program: a
//Author: gary
//Date: 04/05/2013
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <limits>
#include <string>
#include <iostream>
#include <sstream>
#include <functional>
#include <algorithm>
#include <bitset>
#include <deque>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <vector>
using namespace std;

#define ALL(c) (c).begin(), (c).end()
#define CNT(c,x) ((c).find(x) != (c).end())
#define FOR(i, a, n) for(int i=(a);i<=(n);i++)
#define REP(i, n) for(int i=0;i<(n);i++)
#define REP1(i, n) for(int i=0;i<=(n);i++)
#define DBG(VAR) cerr<<#VAR<<" = "<<(VAR)<<endl;
#define CLR(x, v) memset(x, v, sizeof(x))
#define SZ(x) ( (int) (x).size() )
#define MP(x, y) make_pair( (x), (y) )
#define MP3(x, y, z) MP( (x), MP( (y), (z) ) )
#define MP4(x1, y1, x2, y2) MP( MP(x1, y1), MP(x2, y2) )
#define foreach(it, C) for(typeof((C).begin())it=(C).begin();it!=(C).end();++it)
#define pb push_back
typedef long long LL;
typedef pair<int, int> PII;
template<class T> bool checkMin(T& a, T b) { if(a > b){ a = b;return 1;}return 0;}
template<class T> bool checkMax(T& a, T b) { if(a < b){ a = b;return 1;}return 0;}
//int dx[]={-1,0,1,0},  dy[]={0,1,0,-1};
//int dx[]={-1,-1,0,1,1,1,0,-1},dy[]={0,1,1,1,0,-1,-1,-1};
const int INF = 1e9;
const int MN = 1e6;

int dp[2][MN+2], T, A, n;
int sz[MN+2];
vector<int> states;

void mmin(int& a, int b){
  if(a == -1 || (b != -1 && a > b))
    a = b;
}

#define mm(x) ( min((x), MN+1))
pair<int, int> calc(int a, int b){
  int m = 0;
  while(a <= b){
    a += a - 1;
    m++;
  }
  return make_pair(a, m);
}

bool instates[MN+1];
int solve(){
  scanf("%d %d", &A, &n);
  REP(i, n)
    scanf("%d", sz+i);


  sort(sz, sz+n);
  CLR(instates, 0);
  states.clear();
  states.pb(A);
  instates[A] = 1;

  memset(dp, -1, sizeof dp);
  dp[1][A] = 0;
  vector<int> toadd;
  REP(i, n){
    //    printf("sz[%d] = %d\n", i, sz[i]);
    CLR(instates, 0);
    int p = i & 1;
    CLR(dp[p], -1);
    REP(j, SZ(states)){
      int u = states[j], v = -1;
      if(u > sz[i]){
	v = mm(u + sz[i]);
	mmin(dp[p][v], dp[!p][u]);
	toadd.pb(v);
      }else{
	// remove element i
	mmin(dp[p][u], dp[!p][u] + 1);
	toadd.pb(u);
	// find the x that 
	// u + x * (u - 1) > sz[i]
	// x > (sz[i] - u) / (u - 1)
	if(u != 1){
	  PII f = calc(u, sz[i]);
	  v = mm(f.first + sz[i]);
	  mmin(dp[p][v], dp[!p][u] + f.second);
	  toadd.pb(v);
	}
      }
    }
    states = toadd;
    toadd.clear();
  }
  int ans = -1;
  REP1(i, MN)
    mmin(ans, dp[!(n&1)][i]);
  return ans;
}
int main(){
  scanf("%d", &T);
  for(int caseNo = 1; caseNo <= T; caseNo++)
    printf("Case #%d: %d\n", caseNo, solve());
}
