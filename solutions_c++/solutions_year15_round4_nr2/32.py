#include<bits/stdc++.h>
using namespace std;
typedef pair<int,int> PI;
typedef long long LL;
typedef long double D;
#define FI first
#define SE second
#define MP make_pair
#define PB push_back
#define R(I,N) for(int I=0;I<N;I++)
#define F(I,A,B) for(int I=A;I<B;I++)
#define FD(I,N) for(int I=N-1;I>=0;I--)
#define make(A) scanf("%d",&A)
#define make2(A,B) scanf("%d%d",&A,&B)
#define ALL(x) (x).begin(), (x).end()
#define SZ(x) ((int)(x).size())
#define db if(1)printf
template<typename C> void maxi(C& a,C b){if(a<b)a=b;}
template<typename C> void mini(C& a,C b){if(a>b)a=b;}
#define MAX 1001
int n;
D v,x;
pair<D,D> kr[MAX];
D eps = 1e-14;
bool spr(D t){
  D ak = v;
  D wyn1 = 0;
  R(i,n){
    D pom = min(ak, kr[i].SE * t);
    ak -= pom;
    wyn1 += pom * kr[i].FI;
  }
  if(ak > eps)return 0;
  ak = v;
  D wyn2 = 0;
  FD(i,n){
    D pom = min(ak, kr[i].SE * t);
    ak -= pom;
    wyn2 += pom * kr[i].FI;
  }
  return wyn1 < v*x + eps && wyn2 > v*x - eps;
}
void test(){
  static int cas = 0;cas++;
  printf("Case #%d: ",cas);
  scanf("%d%Lf%Lf",&n,&v,&x);
  R(i,n){
    scanf("%Lf%Lf",&kr[i].SE,&kr[i].FI);
  }
  sort(kr,kr+n);
  if(kr[0].FI > x + eps || kr[n-1].FI < x - eps){
    puts("IMPOSSIBLE");
    return;
  }
  D po = 0 ,ko = 1e11;
  R(_,100){
    D m = (po + ko)/2;
    if(spr(m))
      ko = m;
    else
      po = m;
  }
  if(ko > 1e10){
    eps = 1e-13;
    po = 0;
    ko = 1e11;
    R(_,100){
      D m = (po + ko)/2;
      if(spr(m))
        ko = m;
      else
        po = m;
    }
    eps = 1e-14;
  }
  printf("%.8Lf\n",ko);
}
main(){
  int _;make(_);while(_--)test();
}
