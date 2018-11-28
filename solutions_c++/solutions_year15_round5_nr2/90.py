#define DEB

#include<bits/stdc++.h>
#include<unistd.h>
#define REP(i,m) for(int i=0;i<(m);++i)
#define REPN(i,m,in) for(int i=(in);i<(m);++i)
#define ALL(t) (t).begin(),(t).end()
#define CLR(a) memset((a),0,sizeof(a))
#define pb push_back
#define mp make_pair
#define fr first
#define sc second

using namespace std;


#ifdef DEB
#define dump(x)  cerr << #x << " = " << (x) << endl
#define prl cerr<<"called:"<< __LINE__<<endl
template<class T> void debug(T a,T b){ for(;a!=b;++a) cerr<<*a<<' ';cerr<<endl;}
#else
#define dump(x) ;
#define prl ;
template<class T> void debug(T a,T b){ ;}
#endif

template<class T> void chmin(T& a,const T& b) { if(a>b) a=b; }
template<class T> void chmax(T& a,const T& b) { if(a<b) a=b; }

typedef long long int lint;
typedef pair<int,int> pi;

namespace std{
  template<class S,class T>
  ostream &operator <<(ostream& out,const pair<S,T>& a){
    out<<'('<<a.fr<<','<<a.sc<<')';
    return out;
  }
}

const int INF=5e8;


int n,k;
int s[1005];

int ar[1005];

pi range[105];

bool check(int lb,int ub){
  int U=0,D=0;
  int restU=0,restD=0;
  REP(i,k){
    int b=range[i].fr,t=range[i].sc;
    if(t-b>ub-lb) return false;
    if(t>ub){
      D+=t-ub;
      restD+=b-lb-(t-ub);
    }else if(b<lb){
      U+=lb-b;
      restU+=ub-t-(lb-b);
    }else{
      restU+=ub-t;
      restD+=b-lb;
    }
  }
  int tmp=min(U,D);
  U-=tmp;
  D-=tmp;
  if(U>restD || D>restU) return false;
  return true;
}
int main(){
  int T;cin>>T;
  REP(setn,T){
    dump(setn);
    printf("Case #%d: ",setn+1);
    cin>>n>>k;

    REP(i,n-k+1) cin>>s[i];


    CLR(ar);

    ar[k-1]=s[0];
    for(int i=k;i<n;++i){
      ar[i]=ar[i-k]+s[i-k+1]-s[i-k];
    }
  
    int maxi=-INF,mini=INF;
    REP(i,k){
      int mn=INF,mx=-INF;
      for(int j=i;j<n;j+=k){
        chmin(mn,ar[j]);
        chmax(mx,ar[j]);
      }
      range[i]=mp(mn,mx);

      chmax(maxi,mx);
      chmin(mini,mn);
    }

    sort(range,range+k);


    int res=INF;
    for(int i=mini;i<=maxi;++i){
      int lb=i-1,ub=maxi;
      if(check(i,ub)==false) continue;
      while(ub-lb>1){
        int md=(lb+ub)>>1;
        if(check(i,md)){
          ub=md;
        }else{
          lb=md;
        }
      }
      chmin(res,ub-i);
    }
    printf("%d\n",res);
  }

  return 0;

}



