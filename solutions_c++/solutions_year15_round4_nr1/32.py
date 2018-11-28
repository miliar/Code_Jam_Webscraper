#include<bits/stdc++.h>
using namespace std;
typedef pair<int,int> PI;
typedef long long LL;
typedef double D;
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
#define MAX 101
int r,c;
char z[MAX][MAX];
int il[MAX][MAX];
void clr(){
  R(i,r)R(j,c){
    il[i][j] = 0;
  }
}
void test(){
  static int cas = 0;cas++;
  printf("Case #%d: ",cas);
  make2(r,c);
  clr();
  R(i,r)scanf("%s",z[i]);
  int wyn = 0;
  R(i,r){
    R(j,c){
      if(z[i][j] != '.'){
        if(z[i][j] == '<')
          wyn++;
        il[i][j]++;
        break;
      }
    }
    FD(j,c){
      if(z[i][j] != '.'){
        if(z[i][j] == '>')
          wyn++;
        il[i][j]++;
        break;
      }
    }
  }
  R(j,c){
    R(i,r){
      if(z[i][j] != '.'){
        if(z[i][j] == '^')
          wyn++;
        il[i][j]++;
        break;
      }
    }
    FD(i,r){
      if(z[i][j] != '.'){
        if(z[i][j] == 'v')
          wyn++;
        il[i][j]++;
        break;
      }
    }
  }
  R(i,r)R(j,c)if(il[i][j] == 4){
    puts("IMPOSSIBLE");
    return;
  }
  printf("%d\n",wyn);
}
main(){
  int _;make(_);while(_--)test();
}
