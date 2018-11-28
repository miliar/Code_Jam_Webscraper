#include<bits/stdc++.h>
using namespace std;
typedef long long LL;
typedef pair<LL,LL> PI;
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
int p;
vector<PI> t;
vector<LL> war;
void licz(vector<PI> v){
  //printf("%d\n",SZ(v));
  if(SZ(v)==1)return;
  vector<PI> v2;
  LL pom = v[1].FI - v[0].FI;
  war.PB(pom);
  map<LL,LL> m;
  R(i,SZ(v)){
  //  printf("(%lld %lld)",v[i].FI,v[i].SE);
    LL il = v[i].SE - m[v[i].FI];
    if(il){
      v2.PB({v[i].FI,il});
      m[v[i].FI + pom] += il;
    }
  }
  //puts("");
  licz(v2);
}
void test(){
  static int cas = 0;cas++;
  printf("Case #%d:",cas);
  make(p);
  t.resize(p);
  war.clear();
  LL all = 0;
  R(i,p)scanf("%lld",&t[i].FI);
  R(i,p)scanf("%lld",&t[i].SE);
  int zer = __builtin_ctz(t[0].SE);
  //printf("zer: %d\n",zer);
  R(i,p)t[i].SE >>= zer;
  licz(t);
  R(i,zer)printf(" 0");
  R(i,war.size())printf(" %lld",war[i]);
  puts("");
}
main(){
  int _;make(_);while(_--)test();
}
