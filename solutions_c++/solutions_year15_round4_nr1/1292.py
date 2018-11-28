#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cassert>

using namespace std;

#define ri(X) scanf("%d", &(X))
#define pi(X) printf("%d", (X))
#define mp(X,Y) make_pair(X,Y)
#define pb(X) push_back(X)
#define lint long long
#define pii pair<int,int>
#define inf 1e9
#define linf 1e18
#define X first
#define Y second
#define all(X) (X).begin(),(X).end()
#define uni(X) X.erase(unique(X.begin(), X.end()), X.end());

int T , n, m;
const int mn = 109;
const int mm = 10009;
string s[mn];


string w = "^>v<";
map<char,int> ma;

int dx[] = {-1,0,1,0};
int dy[] = {0,1,0,-1};



pii suc[mn][mn];
pii h(int x, int y, int d){
  if(0 <= x && x < n && 0 <= y && y < m){
    if(s[x][y] != '.') return mp(x,y);
    else return h(x+dx[d], y+dy[d], d);
  }else{
    return mp(-1,-1);
  }
}

bool check(int x, int y){
  
  for(int k = 0; k < 4; k++){
    if(h(x+dx[k], y+dy[k], k).X != -1) return 1;
  }
  return 0;
}

int solve(){
  for(int i = 0; i < n; i++){
    for(int j = 0; j < m; j++){
      if(s[i][j] == '.') continue;
      if(!check(i,j)) return -1;
    }
  }
  
  int res = 0;
  int d;
  for(int i = 0; i < n; i++){
    for(int j = 0; j < m; j++){
      if(s[i][j] == '.') continue;
      d = ma[s[i][j]];
      pii v = h(i+dx[d], j+ dy[d],d);
      suc[i][j] = v;
      if(v.X == -1) res++;
    }
  }
  return res;
  
  return 0;
  
}



int main(){
  for(int k = 0; k < 4; k++){
    ma[w[k]] = k;
  }
  ri(T);
  for(int t = 0; t < T; t++){
    ri(n); ri(m);
    for(int i = 0; i < n; i++){
      cin >> s[i];
    }
    int res = solve();
    if(res == -1){
      printf("Case #%d: IMPOSSIBLE\n", t+1);
    }else{
      printf("Case #%d: %d\n", t+1, res);
    }
  }
  return 0;
}

