//Program: a
//Author: gary
//Date: 30/05/2015
#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <algorithm>
using namespace std;
#define SZ(x) ( (int) (x).size() )
#define dbg(x) cerr << #x << " = " << x << endl;
#define mp make_pair
#define pb push_back
#define fi first
#define se second
typedef long long ll;
typedef pair<int, int> pii;
// const int INF = 1e9;
const int MAX_N = 101;
const int dx[] = {-1, 0, 1, 0};
const int dy[] = { 0, 1, 0, -1}; 
const string DIRECTION = "^>v<";

int N, M;
char S[MAX_N][MAX_N];

bool inside(int i, int j){
  return 0 <= i && i < N && 0 <= j && j < M;
}

bool inside(pii p){
  return inside(p.fi, p.se);
}

pii get_next(int i, int j, int d){
  int nx = i + dx[d];
  int ny = j + dy[d];
  while(inside(nx, ny) && S[nx][ny] == '.'){
    nx += dx[d];
    ny += dy[d];
  }
  return make_pair(nx, ny);
}

int main(){
  int T;
  scanf("%d", &T);
  for(int tc = 1; tc <= T; tc++){
    scanf("%d%d", &N, &M);
    for(int i = 0; i < N; i++)
      scanf("%s", S[i]);
    printf("Case #%d: ", tc);
    int res = 0;
    for(int i = 0; i < N && res != -1; i++){
      for(int j = 0; j < M && res != -1; j++){
        int d = DIRECTION.find(S[i][j]);
        if(d == -1)
          continue;
        if(inside(get_next(i, j, d)))
          continue;
        int ok = 0;
        for(int nd = 0; nd < 4; nd++){
          if(inside(get_next(i, j, nd))){
            ok = 1;
            break;
          }
        }
        if(!ok){
          res = -1;
        } else {
          res += 1;
        }
      }
    }
    if(res == -1) 
      printf("IMPOSSIBLE\n");
    else
      printf("%d\n", res);
  }
  return 0;
}
