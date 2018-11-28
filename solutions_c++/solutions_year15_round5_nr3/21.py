#include<bits/stdc++.h>
using namespace std;
typedef long double D;
typedef pair<D,int> PI;
typedef long long LL;
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
template<typename C> void MA(C& a,C b){if(a<b)a=b;}
template<typename C> void MI(C& a,C b){if(a>b)a=b;}
#define MAX 511
D wyn[MAX][MAX][3];
//D gg[MAX][MAX][2];
D y;
int st[MAX];
int n;
vector<PI> m,w;
D gd(PI x,D t){
  //printf("gd %Lf %Lf\n",x.SE + t * x.FI,t);
  return x.SE + t * x.FI;
}
void test(){
  m.clear();
  w.clear();
  static int cas = 0;cas++;
  printf("Case #%d: ",cas);
  cerr << cas << endl;
  scanf("%Lf",&y);
  make(n);
  R(i,n)
    make(st[i]);
  R(i,n){
    D pom;
    scanf("%Lf",&pom);
    if(st[i] < 0){
      m.PB({pom,-st[i]});
    }else
      w.PB({pom,st[i]});
  }
  sort(ALL(m),greater<PI>());
  sort(ALL(w),greater<PI>());
  R(i,SZ(m)+1)R(j,SZ(w)+1)R(k,3){
    wyn[i][j][k] = 1e18;
  }
  //wyn[0][0][0] = 0;
  //wyn[0][0][1] = 0;
  wyn[0][0][2] = 0;
  //gg[0][0][0] = 0;
  //gg[0][0][1] = 0;
  D res = 1e18;
  R(i,SZ(m)+1)R(j,SZ(w)+1){
    if(i == SZ(m) && j == SZ(w)){
      MI(res,wyn[i][j][0]);
      MI(res,wyn[i][j][1]);
    }
    D t = wyn[i][j][0];
    D g = i == 0 ? 0 : gd(m[i-1], t);
    //if(i!=SZ(m))
    {
      int ak = i-1;
      D nast;
      do{
        ak++;
        if(ak == SZ(m))break;
        nast = gd(m[ak],t);
      }while(ak < SZ(m) && nast - g < 0);
      if(ak != SZ(m)){
        D dz = (nast - g) / (y - m[ak].FI);
        MI(wyn[ak+1][j][0], t+dz);
      }else{
        if(j == SZ(w)){
          MI(res,t);
        }
      }
      MI(wyn[ak][j][2], t + g/y);
    }
    
    
    t = wyn[i][j][1];
    g = j == 0 ? 0 : gd(w[j-1], t);
    //if(j!=SZ(w))
    {
      int ak = j-1;
      D nast;
      do{
        ak++;
        if(ak == SZ(w))break;
        nast = gd(w[ak],t);
      }while(ak < SZ(w) && nast - g < 0);
      if(ak != SZ(w)){
        D dz = (nast - g) / (y - w[ak].FI);
        if(dz < 0){
          printf("%Lf\n",dz);
          exit(0);
        }
        MI(wyn[i][ak+1][1], t+dz);
      }else{
        if(i == SZ(m)){
          MI(res,t);
        }
      }
      MI(wyn[i][ak][2], t + g/y);
    }
    
    t = wyn[i][j][2];
    if(i!=SZ(m)){
      D nast = gd(m[i],t);
      D dz = nast / (y - m[i].FI);
      
      MI(wyn[i+1][j][0],t+dz);
    }
    if(j!=SZ(w)){
      D nast = gd(w[j],t);
      D dz = nast / (y - w[j].FI);
      
      MI(wyn[i][j+1][1],t+dz);
    }
  }
  printf("%.7Lf\n",res);
//  printf("%.7f\n",min(wyn[SZ(m)][SZ(w)][0],wyn[SZ(m)][SZ(w)][1]));
}
main(){
  int _;make(_);while(_--)test();
}
