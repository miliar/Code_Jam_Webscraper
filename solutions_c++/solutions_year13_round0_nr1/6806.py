//Program: a
//Author: gary
//Date: 13/04/2013
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
#define st(x) string(1, x)
typedef long long LL;
typedef pair<int, int> PII;
template<class T> bool checkMin(T& a, T b) { if(a > b){ a = b;return 1;}return 0;}
template<class T> bool checkMax(T& a, T b) { if(a < b){ a = b;return 1;}return 0;}
//int dx[]={-1,0,1,0},  dy[]={0,1,0,-1};
//int dx[]={-1,-1,0,1,1,1,0,-1},dy[]={0,1,1,1,0,-1,-1,-1};
const int INF = 1e9;
const int MN = -1;

int T;
char g[5][5];
char winner(string s){
  int X = count(ALL(s),'X'), O = count(ALL(s), 'O'), T = count(ALL(s), 'T');
  if(X == 4 || X + T == 4) return 'X';
  if(O == 4 || O + T == 4) return 'O';
  return 'T';
}
char determineWinner(){
  char c;
  REP(i, 4)
    if( ( c = winner(g[i])) != 'T')
      return c;
  REP(i, 4){
    string s ="";REP(j,4)s+=g[j][i];
    if( ( c = winner(s)) != 'T')
      return c;
  }
  string s="";
  REP(i, 4)
    s += g[i][i];
  if( ( c = winner(s)) != 'T')
    return c;
  s = "";
  REP(i, 4)
    s += g[i][3-i];
  if( ( c = winner(s) ) != 'T')
    return c;
  REP(i, 4)
    if( count(g[i], g[i]+4, '.'))
      return 'N';
  return 'D';
}
int main(){
  scanf("%d\n", &T);
  FOR(t, 1, T){
    REP(i, 4)     scanf("%s\n", g[i]);
    //REP(i, 4) puts(g[i]);
    printf("Case #%d: ", t);
    switch(determineWinner()){
    case 'N': puts("Game has not completed"); break;
    case 'D': puts("Draw"); break;
    case 'X': puts("X won");break;
    case 'O': puts("O won");break;
    }
    
  }
}
