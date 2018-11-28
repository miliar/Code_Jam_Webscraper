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
int r,c,n;
int grande;

map<int,int> memo[20][20][20];
inline void apaga(int &mask,int i){
    mask&=(~(1<<i));
}
inline void prende(int &mask,int i){
  mask|=(1<<i);
  }

void imprime(int mask,int tam)
{
for(int i=0;i<tam;i++)
{
if(mask&(1<<i))
cout<<1;
else
      cout<<0;
}
cout<<endl;
}
int go(int x, int y, int mask, int tengo){
  if(x>=r) {
      if(tengo == n) return 0;
      else return grande; 
    }
    if(y>=c) return go(x+1,0,mask,tengo);
    if(memo[x][y][tengo].count(mask)) return memo[x][y][tengo][mask];
    int res = grande;
    //pongo
    {
      int ant = y-1;
      int choca = 0;
      //izq
      if(ant>=0 && (mask&(1<<ant))){
        choca += 1;
      }
      //arriba
      if((mask&(1<<y))){
        choca += 1;
      }
      if(tengo + 1 <= n){
        int mask2 = mask;
        prende(mask2,y);
        res = min(res, choca + go(x, y+1, mask2, tengo +1));
      }
    }

    //no pong 
    int mask2 = mask;
    apaga(mask2,y);
    res = min(res,go(x, y+1, mask2, tengo));
    return memo[x][y][tengo][mask] = res;
}

int main(){
  int tt;
  cin>>tt;
  f(CASO,1,tt+1){
    cin>>r>>c>>n;
    grande = 1000000;
    f(i,0,20)f(j,0,20)f(k,0,20)memo[i][j][k].clear();
    int res = go(0,0,0,0);
    cout<<"Case #"<<CASO<<": "<<res<<endl;
  }
  return 0;
}
