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
int x,n,m;
bool test(){
  static int cas = 0;cas++;
  printf("Case #%d: ",cas);
  scanf("%d%d%d",&x,&n,&m);
  if(x==1)return 1;
  if(x==2)return n*m%2 == 0;
  if(x==3){
    int pom = n*m;
    if(pom < 6)return 0;
    if(pom%3)return 0;
    return 1;
  }
  if(x==4){
    int pom = n*m;
    return pom == 12 || pom == 16;
  }
}
main(){
  int _;make(_);while(_--)puts(test()?"GABRIEL":"RICHARD");
}