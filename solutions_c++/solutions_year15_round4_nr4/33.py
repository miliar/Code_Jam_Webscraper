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
#define MAX 1000
LL dp[MAX];
LL P = 1e9 + 7;
int r,c;
int a[] = {3,4,6};
int b[] = {4,5,4};
LL licz(int el){
  dp[0] = 1;
  F(i,1,r+1){
    dp[i] = 0;
    if(i >= 3)
      dp[i] += dp[i-3];
    R(k,3){
      if(c % a[k] == 0 && el % a[k] == 0){
        if(i >= b[k])
          dp[i] += a[k] * dp[i-b[k]];
      }
    }
    dp[i] %= P;
  }
  return (dp[r] + dp[r-2]*2 + dp[r-4]) %P;
}
void test(){
  static int cas = 0;cas++;
  printf("Case #%d: ",cas);
  make2(r,c);r += 2;
  LL wyn = 0;
  P *= c;
  R(i,c)wyn += licz(i);
  wyn%=P;
  P /= c;
  assert(wyn % c == 0);
  printf("%lld\n",wyn/c);
}
main(){
  int _;make(_);while(_--)test();
}
