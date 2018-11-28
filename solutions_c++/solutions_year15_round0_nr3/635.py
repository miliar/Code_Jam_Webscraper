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
#define db if(1)printf
template<typename C> void maxi(C& a,C b){if(a<b)a=b;}
template<typename C> void mini(C& a,C b){if(a>b)a=b;}
#define MAX 101000
char z[MAX];
int t[4][4] = {
  {1,2,3,4},
  {2,-1,4,-3},
  {3,-4,-1,2},
  {4,3,-2,-1}
};
int mn(int a,int b){
  int zn = 1;
  if(a < 0){
    zn*=-1;
    a = -a;
  }
  if(b < 0){
    zn*=-1;
    b = -b;
  }
  return zn * t[a-1][b-1];
}
int n;
LL m;
bool test(){
  static int cas = 0;cas++;
  printf("Case #%d: ",cas);
  make(n);
  scanf("%lld",&m);
  scanf("%s",z);
  R(i,n)z[i] = z[i] - 'i' + 2;
  int ak = 1;
  R(i,n)ak = mn(ak,z[i]);
  if(ak == 1 || (ak == -1 && m%2==0) || (abs(ak)>=2 && m%4!=2))return 0;
  ak = 1;
  LL po = 1e15;
  R(i,n*9){
    ak = mn(ak,z[i%n]);
    if(ak == 2){
      po = i+1;
      break;
    }
  }
  ak = 1;
  LL ko = 1e15;
  R(i,n*9){
    ak = mn(z[n-i%n-1],ak);
    if(ak == 4){
      ko = i+1;
      break;
    }
  }
  return po+ko < n*1ll*m;
}
main(){
  int _;make(_);while(_--)puts(test()?"YES":"NO");
}