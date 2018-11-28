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

const int MAX=1100000;
int N,p,q,r,s,t[MAX];
int64 _sum[MAX];
int64 sum(int from,int to){
  int64 ans=0;
  if(from>to)return 0;
  return _sum[from]-_sum[to+1];
}
int main(){
  int c;
  scanf("%d",&c);
  for(int cc=1;cc<=c;cc++){
    scanf("%d %d %d %d %d",&N,&p,&q,&r,&s);
    FOR(i,N)t[i]=((int64)i*p+q)%r+s;
    _sum[N]=0;
    for(int i=N-1;i>=0;i--)_sum[i]=_sum[i+1]+t[i];
    int64 ans=0;
    int i=0;
    FOR(j,N){
      while(i+1<=j&&max(sum(0,i-1),sum(i,j))>=max(sum(0,i),sum(i+1,j)))++i;
      int64 cur=sum(0,N-1)-max(sum(0,i-1),max(sum(i,j),sum(j+1,N-1)));
      ans=max(ans,cur);
    }
    printf("Case #%d: %0.9lf\n",cc,(double)ans/sum(0,N-1));
  }
}
