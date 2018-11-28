#include<cassert>
#include<cstdio>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
using namespace std;

#define ALL(t) t.begin(),t.end()
#define FOR(i,n) for (int i=0;i<(int)(n);i++)
#define FOREACH(i,t) for (typeof(t.begin())i=t.begin();i!=t.end();i++)
typedef vector<int> vi;
typedef long long int64;

const int64 INF=1LL<<60;
int64 d[1234][1234],r[1234];
bool seen[1234];
int64 calc(int min_x,int max_x,int min_y,int max_y){
  //cout<<min_x<<" "<<max_x<<" "<<min_y<<" "<<max_y<<endl;
  if(max_x<0)return calc(-max_x,-min_x,min_y,max_y);
  if(max_y<0)return calc(min_x,max_x,-max_y,-min_y);
  if(min_x<0)return min(calc(0,-min_x,min_y,max_y),calc(0,max_x,min_y,max_y));
  if(min_y<0)return min(calc(min_x,max_x,0,-min_y),calc(min_x,max_x,0,max_y));
  return max(min_x,min_y);
}
int main(){
  int c;
  scanf("%d",&c);
  for(int cc=1;cc<=c;cc++){
    int W,H,B;
    scanf("%d %d %d",&W,&H,&B);
    int x0[1234],y0[1234],x1[1234],y1[1234];
    FOR(i,B){
      scanf("%d %d %d %d",&x0[i],&y0[i],&x1[i],&y1[i]);
    }
    int N=B+2,source=B,sink=B+1;
    FOR(i,B)d[source][i]=d[i][source]=x0[i];
    FOR(i,B)d[sink][i]=d[i][sink]=W-1-x1[i];
    d[source][sink]=d[sink][source]=W;
    FOR(i,B)FOR(j,B){
      int min_x=x0[i]-(x1[j])-1;
      int max_x=x1[i]-(x0[j])+1;
      int min_y=y0[i]-(y1[j])-1;
      int max_y=y1[i]-(y0[j])+1;
      d[i][j]=calc(min_x,max_x,min_y,max_y);
    }
    FOR(i,N)r[i]=INF;
    FOR(i,N)seen[i]=false;
    r[source]=0;
    while(1){
      int best=-1;
      FOR(i,N)if(!seen[i]&&(best==-1||r[i]<r[best]))best=i;
      if(best==-1)break;
      seen[best]=true;
      FOR(i,N)r[i]=min(r[i],r[best]+d[best][i]);
    }
    printf("Case #%d: %lld\n",cc,r[sink]);
  }
}
