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
int N;
int dist[1000010];
int get_r(int num){
  int r=0;
  while(num){
    int d = num%10;
    r*=10;
    r+=d;
    num/=10;
  }
  return r;
}
int main(){
  int tt;
  cin>>tt;
  f(CASO,1,tt+1){
    cin>>N;  
    f(i,0,N+1)dist[i] = -1;
    queue<int> q;
    q.push(1);
    int res = 1;
    dist[1] = 1;
    while(!q.empty()){
      int cur = q.front();
      q.pop();
      if(cur == N){
        res = dist[cur];
        break;
      }
      int nx = cur + 1;
      if(dist[nx]==-1){
        q.push(nx);
        dist[nx] = dist[cur] + 1;
      }
      int re = get_r(cur);
      if(re  > cur){
        if(dist[re] == -1){
          q.push(re);
          dist[re] = dist[cur] + 1;
        } 
      }
    }
    cout<<"Case #"<<CASO<<": "<<dist[N]<<endl;
  }
  return 0;
}
