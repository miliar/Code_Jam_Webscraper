#pragma warning (disable: 4530) 
#include<map>
#include<set>
#include<list>
#include<cmath>
#include<queue>
#include<stack>
#include<cstdio>
#include<string>
#include<vector>
#include<complex>
#include<cstdlib>
#include<cstring>
#include<numeric>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<functional>
#include<climits>


#define mp       make_pair
#define pb       push_back
#define all(x)   (x).begin(),(x).end()
#define rep(i,n) for(int i=0;i<(n);i++)
 
using namespace std;
 
typedef    long long          ll;
typedef    unsigned long long ull;
typedef    vector<bool>       vb;
typedef    vector<int>        vi;

typedef    vector<vb>         vvb;
typedef    vector<vi>         vvi;
typedef    pair<int,int>      pii;
 
const int INF=1<<29;
const double EPS=1e-9;
 
const int dx[]={1,0,-1,0,1,1,-1,-1},dy[]={0,-1,0,1,1,-1,-1,1};//right down left up
int test;
int law[200][200];
int y_max[200],x_max[200];
int W,H;
bool OK(){
  rep(y,H) rep(x,W) if(law[y][x] != x_max[y] && law[y][x] != y_max[x]) return false;
  return true;
}
int main(){
  scanf("%d",&test);
  rep(t,test){
    memset(law,0,sizeof(law));
    memset(y_max,0,sizeof(y_max));
    memset(x_max,0,sizeof(x_max));
    
    cin>>H>>W;
    rep(y,H) rep(x,W) cin>>law[y][x];
    rep(y,H) rep(x,W) x_max[y] = max(x_max[y],law[y][x]);
    rep(x,W) rep(y,H) y_max[x] = max(y_max[x],law[y][x]);
    printf("Case #%d: %s\n",t + 1,(OK() ? "YES" : "NO"));
  }
}
