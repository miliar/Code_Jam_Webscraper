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
int n;
void test(){
  static int cas = 0;cas++;
  printf("Case #%d: ",cas);
  make(n);n++;
  scanf(" ");
  vector<int> all;
  R(i,n){
    char z = getchar();
    z-='0';
    R(_,z)all.PB(i);
  }
  sort(ALL(all));
  int wyn = 0;
  R(i,all.size()){
    maxi(wyn,all[i] - i);
  }
  printf("%d\n",wyn);
}
main(){
  int _;make(_);while(_--)test();
}