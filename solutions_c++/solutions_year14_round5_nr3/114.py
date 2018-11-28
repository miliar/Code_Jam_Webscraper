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

int N,nr[1010];
char type[1010];
int main(){
  int c;
  scanf("%d",&c);
  for(int cc=1;cc<=c;cc++){
    scanf("%d",&N);
    FOR(i,N)scanf(" %c %d",&type[i],&nr[i]);
    /*if(cc==30){
      cout<<N<<endl;
      FOR(i,N)cout<<type[i]<<" "<<nr[i]<<endl;
    }*/
    vi s;
    FOR(i,N)if(nr[i])s.push_back(nr[i]);
    int cnt=0;
    FOR(i,N)cnt+=!nr[i];
    FOR(i,cnt)s.push_back(2010+i);
    sort(s.begin(),s.end());
    s.erase(unique(s.begin(),s.end()),s.end());
    int m=s.size();
    FOR(i,N)if(nr[i])nr[i]=lower_bound(s.begin(),s.end(),nr[i])-s.begin();else nr[i]=-1;
    bool ok[1<<15],ok2[1<<15];
    assert(m<=15);
    memset(ok,1,sizeof(ok));
    FOR(i,N){
      memset(ok2,0,sizeof(ok2));
      //cout<<m<<" "<<type[i]<<" "<<nr[i]<<endl;
      FOR(j,1<<m)if(ok[j]){
        if(type[i]=='E'){
          if(nr[i]==-1){
            FOR(k,m)if(!(j&1<<k))ok2[j|1<<k]=true;
          }else if(!(j&1<<nr[i])){
            ok2[j|1<<nr[i]]=true;
          }
        }else if(type[i]=='L'){
          if(nr[i]==-1){
            FOR(k,m)if((j&1<<k))ok2[j-(1<<k)]=true;
          }else if(j&1<<nr[i]){
            ok2[j-(1<<nr[i])]=true;
          }
        }
      }
      memcpy(ok,ok2,sizeof(ok2));
    }
    int ans=1010;
    FOR(i,1<<m)if(ok[i])ans=min(ans,__builtin_popcount(i));
    printf("Case #%d: ",cc);
    if(ans<1010)printf("%d\n",ans);else printf("CRIME TIME\n");
  }
}
