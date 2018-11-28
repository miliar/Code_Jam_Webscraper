#include <bits/stdc++.h>
using namespace std;
#define TR(i,v)       for(__typeof((v).begin())i=(v).begin();i!=(v).end();++i)
#define DEBUG(x)      cout<<#x<<" = "<<x<<endl
#define SIZE(p)       (int)(p).size()
#define MP(a,b)       make_pair((a),(b))
#define ALL(p)        (p).begin(),(p).end()
#define rep(i,n)      for(int i=0;i<(int)(n);++i)
#define REP(i,a,n)    for(int i=(a);i<(int)(n); ++i)
#define FOR(i,a,b)    for(int i=(int)(a);i<=(int)(b);++i)
#define FORD(i,b,a)   for(int i=(int)(b);i>=(int)(a);--i)
#define CLR(x,y)      memset((x),(y),sizeof((x)))
typedef long long LL;
typedef pair<int,int> pii;
const double eps=1e-8;
double V,X;
double C[105],R[105];
int n;
bool eq(double a,double b){
  return fabs(a-b)<eps;
}
int dcmp(double a,double b){
  return eq(a,b)?0:a<b?-1:1;
}
void gao1(){
  if(!eq(C[0],X)){
    puts("IMPOSSIBLE");
  }else{
    printf("%.12f\n",V/R[0]);
  }
}
int main(){
  int T;scanf("%d",&T);
  FOR(cs,1,T){
    printf("Case #%d: ",cs);
    scanf("%d",&n);
    scanf("%lf%lf",&V,&X);
    rep(i,n)scanf("%lf%lf",R+i,C+i);
    // if(cs==82){
    //   printf("%.12f %.12f\n",V,X);
    //   rep(i,n)printf("%.12f %.12f\n",R[i],C[i]);
    //   return 0;
    // }
    if(n==1){
      gao1();
      continue;
    }
    if(eq(C[0],C[1])){
      if(eq(C[0],X)){
        printf("%.12f\n",V/(R[0]+R[1]));
      }else{
        puts("IMPOSSIBLE");
        continue;
      }
    }else{
      double a=C[0]/V,b=C[1]/V;
      double v1=(X-b*V)/(a-b);
      double v2=V-v1;
      if(dcmp(v1,0)<0 || dcmp(v2,0)<0){
        puts("IMPOSSIBLE");
        continue;
      }
      double rr=max(v1/R[0],v2/R[1]);
      if(eq(C[0],X))
        rr=min(rr,V/R[0]);
      if(eq(C[1],X))
        rr=min(rr,V/R[1]);
      printf("%.12f\n",rr);
    }
  }
  return 0;
}
