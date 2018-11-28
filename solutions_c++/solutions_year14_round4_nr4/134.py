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

const int MOD=1000000000+7;
const int INF=1000000000;
int M,N;
string t[1010];
typedef pair<int,int> p2;
p2 s[5][1<<8];
int cost[1<<8];
int lcp(int i,int j){
  assert(i!=j);
  int pos=0;
  while(t[i][pos]==t[j][pos])++pos;
  return pos;
}
int main(){
  int c;
  scanf("%d",&c);
  for(int cc=1;cc<=c;cc++){
    scanf("%d %d",&M,&N);
    for(int i=0;i<M;i++){
      char buf[110];
      scanf(" %s",buf);
      t[i]=buf;
    }
    sort(t,t+M);
    FOR(i,1<<M){
      cost[i]=0;
      int prev=-1;
      FOR(j,M)if(i&1<<j){
        cost[i]+=t[j].length();
        if(prev>-1)cost[i]-=lcp(j,prev);else ++cost[i];
        prev=j;
      }
    }
    memset(s,0,sizeof(s));
    FOR(i,1<<M)s[1][i]=p2(cost[i],1);
    for(int cnt=2;cnt<=N;cnt++)FOR(i,1<<M){
      s[cnt][i]=s[cnt-1][i];
      for(int j=i;j;j=j-1&i){
        p2 tmp=s[cnt-1][i^j];
        tmp.first+=cost[j];
        if(tmp.first>s[cnt][i].first)s[cnt][i]=tmp;else if(tmp.first==s[cnt][i].first){
          s[cnt][i].second+=tmp.second;
          if(s[cnt][i].second>=MOD)s[cnt][i].second-=MOD;
        }
      }
    }
    printf("Case #%d: %d %d\n",cc,s[N][(1<<M)-1].first,s[N][(1<<M)-1].second);
  }
}
