#include<iostream>
#include<queue>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<string>
#include<cstring>
#include<map>
#include<numeric>
#include<sstream>
#include<cmath>
#include<ctime>
using namespace std;
#define all(v) (v).begin(),(v).end()
#define rall(v) (v).end,(v).begin
#define pb push_back
#define f(i,x,y) for(int i=x;i<y;i++)
#define FOR(it,A) for(typeof A.begin() it = A.begin();it!=A.end();it++)
#define sqr(x) (x)*(x)
#define mp make_pair
#define clr(x,y) memset(x,y,sizeof x)
typedef pair<int,int> pii;
typedef long long ll;
typedef long double ld;
int memo[1003][1003];
int todos[1003];
int D;
int go(int x,int y){
  if(x>=y || y == 1) return 0;
  if (memo[x][y]!=-1) return memo[x][y];
  int res = 0;
  int yy = y/2;
  res = 1 + go(x ,yy) + go(x, y - yy); 
  return memo[x][y] = res;
}
int dame(int X){
  int r = 0;
  f(i,0,D){
    //r += go(X,todos[i]);
     if( todos[i] > X ){
       int cant =  todos[i] / X;
       if(todos[i] % X) cant++;
       cant-- ;
       r += cant;
     }
  } 
  return r;
}

int main(){
  int casos;
  scanf("%d", &casos);
  //clr(memo,-1);
  f(t,1,casos+1){ 
    scanf("%d", &D);
    int maxi = 0;
    f(i,0,D) { scanf("%d", &todos[i]) ; maxi = max(maxi, todos[i]);}
    int res = maxi;
    int limit = min(1001, maxi + 1);
    f(X,1,limit){
      //cout<<dame(X) << " " << X <<endl; 
      res = min(res, dame(X) + X);
    }
    printf("Case #%d: %d\n", t, res);
  }
  return 0;
}
