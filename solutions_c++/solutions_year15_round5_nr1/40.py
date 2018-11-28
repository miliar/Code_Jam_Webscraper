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
template<typename C> void MA(C& a,C b){if(a<b)a=b;}
template<typename C> void MI(C& a,C b){if(a>b)a=b;}
#define MAX 1001001
int n,d,s[MAX],m[MAX];
void maketab(int *t){
  int a,c,r;
  make2(t[0],a);
  make2(c,r);
  F(i,1,n)t[i] = (t[i-1] * 1ll * a + c) % r;
}
int a[MAX],b[MAX];
void test(){
  static int cas = 0;cas++;
  printf("Case #%d: ",cas);
  cerr << cas << endl;
  make2(n,d);
  maketab(s);
  maketab(m);
  F(i,1,n)
    m[i] %= i;
  multiset<PI> ss;
  R(i,n){
    a[i] = s[i] - d;
    b[i] = s[i];
    if(i){
      MA(a[i],a[m[i]]);
      MI(b[i],b[m[i]]);
    }
    if(a[i] <= b[i]){
      ss.insert({a[i],-1});
      ss.insert({b[i],1});
    }
  }
  int wyn = 1;
  int ak = 0;
  for(auto x:ss){
    ak -= x.SE;
    MA(wyn,ak);
  }
  printf("%d\n",wyn);
}
main(){
  int _;make(_);while(_--)test();
}
