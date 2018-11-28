#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cctype>
#include <algorithm>
#include <string>
#include <vector>
#include <deque>
#include <stack>
#include <queue>
#include <list>
#include <map>
#include <set>

using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;
typedef vector<string> vs;
typedef vector<long long> vll;
#define sz(a)  int((a).size())
#define pb  push_back
#define all(c)  (c).begin(),(c).end()
#define mset(arr,val)  memset(arr,val,sizeof(arr))
#define tr(c,i)  for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)
#define rep(var,n)  for(int var=0;var<(n);var++)
#define repN(var,n)  for(int var=1;var<=(n);var++)
#define forr(var,from,to) for(int var=(from);var<=(to);var++) 
#define found(s,e)  ((s).find(e)!=(s).end())
#define remove_(c,val) (c).erase(remove((c).begin(),(c).end(),(val)),(c).end())
#define lastc(str) (*((str).end()-1))

// #include "cout.h"

// ENWS
int dx[4] = { 1, 0, -1, 0 }, dy[4] = { 0, 1, 0, -1 };

#define U 1000
#define M 2048
int dp[U*2+1][U*2+1];

string solve(int X, int Y) {
  // printf("solve(%d,%d)...\n", X, Y); 
  if (dp[U+X][U+Y] == -1) return "?";

  vector<char> v;
  while (X != 0 || Y != 0) {
    int mi = dp[U+X][U+Y];
    int x = (mi / M)-U, y = (mi % M)-U;
    int dx = X - x, dy = Y - y;
    // printf("@ (%d,%d), d=(%d,%d)\n", X,Y, dx,dy);
    if (dx > 0) {
      v.pb('E');
    } else if (dx < 0) {
      v.pb('W');
    } else if (dy > 0) {
      v.pb('N');
    } else if (dy < 0) {
      v.pb('S');
    }
    X = x; Y = y;
  }
  reverse(all(v));

  return string(all(v));
}

void sub(){

  queue<vector<int> > q;

  vector<int> v0(4, 0);
  q.push(v0);

  while (!q.empty()) {
    vector<int> v = q.front(); q.pop();

    int x = v[0], y = v[1], st = v[2] + 1, last_m = v[3];
    // printf("%d (%d, %d), (%d %d)\n", st, x,y, (last_m/M)-U, (last_m%M)-U);

    if (abs(x) > U || abs(y) > U) continue;
    if (dp[U+x][U+y] >= 0) continue;

    dp[U+x][U+y] = last_m;

    v[2] = st;
    v[3] = (U+x)*M + (U+y);

    v[0] = x+st; v[1] = y; q.push(v);
    v[0] = x-st; v[1] = y; q.push(v);
    v[0] = x; v[1] = y+st; q.push(v);
    v[0] = x; v[1] = y-st; q.push(v);
  }
}

main(){
  int _T; cin>>_T;

  rep(i,U*2+1) rep(j,U*2+1) dp[i][j] = -1;
  sub();

  repN(_t,_T) {
    int X,Y; cin>>X>>Y;
    printf("Case #%d: %s\n", _t, solve(X,Y).c_str());
  }
}
