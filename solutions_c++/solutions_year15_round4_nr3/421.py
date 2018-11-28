#include <bits/stdc++.h>
using namespace std;
#define TR(i,v)      for(__typeof((v).begin())i=(v).begin();i!=(v).end();++i)
#define DEBUG(x)     cout<<#x<<"="<<x<<endl
#define SIZE(p)      (int)(p).size()
#define MP(a,b)      make_pair((a),(b))
#define ALL(p)       (p).begin(),(p).end()
#define rep(i,n)     for(int i=0;i<(int)(n);++i)
#define REP(i,a,n)   for(int i=(a);i<(int)(n);++i)
#define FOR(i,a,b)   for(int i=(int)(a);i<=(int)(b);++i)
#define FORD(i,b,a)  for(int i=(int)(b);i>=(int)(a);--i)
#define CLR(x,y)     memset((x),(y),sizeof((x)))
typedef unsigned long long LL;
typedef pair<int,int> PII;
typedef vector<int> VI;
const int MAXN=200+10,seed=1e9+7;
VI s[MAXN];
map<LL,int> HBT;
int gid(LL x){
  if (HBT.count(x))return HBT[x];
  int sz=HBT.size();
  HBT[x]=sz; return sz;
}
LL ghash(string s){
  LL r=0;
  for(size_t i=0; i<s.size();++i){
    r=r*seed+s[i];
  }
  return r;
}
int main(){
  int T;scanf("%d",&T);
  FOR(cs,1,T){
    printf("Case #%d: ",cs);
    int n;cin>>n;HBT.clear();
    string lns;getline(cin,lns);
    rep(i,n){
      getline(cin,lns);s[i].clear();
      stringstream sin(lns);
      while(sin>>lns)
        s[i].push_back(gid(ghash(lns)));      
    }
    int ret=~0U>>1,m=SIZE(HBT);    
    static int mp[100000];
    rep(msk,1<<(n-2)){
      rep(i,m)mp[i]=0;
        for(auto &x:s[0])mp[x]|=1;
          for(auto &x:s[1])mp[x]|=2;
            rep(i,n-2){
              if(msk>>i&1){
                for(auto &x:s[i+2])mp[x]|=1;
              }
            else{
              for(auto &x:s[i+2])mp[x]|=2;
            }
        }
        int tmp=0;
        rep(i,m)tmp+=mp[i] == 3;
          ret=min(ret,tmp);
      }
      printf("%d\n",ret);
    }
    return 0;
  }
