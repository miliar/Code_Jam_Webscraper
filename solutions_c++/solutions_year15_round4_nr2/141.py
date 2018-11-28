
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

int n;

int m1,m2;
int V,X;
pi flow1[105],flow2[105];//(volume,temp)
int readD(){
  double a;scanf("%lf",&a);
  a*=10000;
  a+=0.5;

  int res=a;
  return res;
}

double getheat(pi* a,int m){
  double res=0;
  REP(i,m) res+=a[i].fr*(lint)a[i].sc;
  return res;
}

double getvol(pi* a,int m){
  double res=0;
  REP(i,m) res+=a[i].fr;
  return res;
}

bool cmp(const pi& a,const pi& b){
  return a.sc<b.sc;
}

int main(){
  int t;cin>>t;


  REP(setn,t){
    printf("Case #%d: ",setn+1);

    cin>>n;
    V=readD();X=readD();

    m1=m2=0;
    bool iszero=false;
    REP(i,n){
      pi tmp;
      tmp.fr=readD();
      tmp.sc=readD()-X;
      if(tmp.sc<0) flow1[m1++]=mp(tmp.fr,-tmp.sc);
      else flow2[m2++]=tmp;

      if(tmp.sc==0) iszero=true;
    }

    debug(flow1,flow1+m1);
    debug(flow2,flow2+m2);

    sort(flow1,flow1+m1,cmp);
    sort(flow2,flow2+m2,cmp);

    if(!iszero && (m1==0 || m2==0)){
      puts("IMPOSSIBLE");
      continue;
    }

    double lb=0,ub=1e10;
    REP(hoge,200){
      double md=(lb+ub)/2;

      double hsum1=getheat(flow1,m1)*md,hsum2=getheat(flow2,m2)*md;

      pi* flow;

      dump(hsum1);dump(hsum2);
      int m;

      double dif=abs(hsum1-hsum2);
      if(hsum1>hsum2){
        flow=flow1;
        m=m1;
      }else{
        flow=flow2;
        m=m2;
      }

      double vol=(getvol(flow1,m1)+getvol(flow2,m2))*md;

      for(int i=m-1;i>=0;--i) if(flow[i].sc>0){
        double time=dif/flow[i].sc/flow[i].fr;
        chmin(time,md);
        dif-=time*flow[i].sc*flow[i].fr;
        vol-=time*flow[i].fr;

        if(dif<1e-100) break;
      }
      dump(vol);
      if(vol>V) ub=md;
      else lb=md;
    }
    printf("%.10f\n",lb);
  }

  return 0;

}



