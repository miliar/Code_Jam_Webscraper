#define FILE_IO

#include<iostream>
#include<algorithm>
#include<set>
#include<map>
#include<vector>
#include<queue>
#include<cstdio>
#include<cstring>

using namespace std;

typedef long long ll;
#ifdef unix
#define LLD "%lld"
#else
#define LLD "%I64d"
#endif

typedef double lf; 

typedef pair<int,int> pii;
typedef pair<lf,lf> pff;
#define mp make_pair
#define X first
#define Y second  

#define pb push_back
#define forI_(i,V,_) for(typeof(V.end())i=_;i!=V.end();++i)
#define forI(i,V) forI_(i,V,V.begin())

int best(int x,int n){
  if(x!=n-1)
    return n/2+best(n/2-(n-x-2)/2-1,n/2);
  else
    return 0;
}

int worst(int x,int n){
  if(!x)
    return n-1;
  else
    return worst((x-1)/2,n/2);
}

int main(){
#ifdef FILE_IO
  freopen("t.in","r",stdin);
  freopen("t.out","w",stdout);
#endif
  int T,Test=0;
  int n,L,m,i;
  for(scanf("%d",&T);T--;){
    printf("Case #%d: ",++Test);
    scanf("%d%d",&n,&L);
    m=1<<n,L=m-L;
    for(i=0;i<m;++i)
      if(worst(i,m)<L)
        break;
    printf("%d ",i-1);
    for(i=0;i<m;++i)
      if(best(i,m)<L)
        break;
    printf("%d\n",i-1);
  }
  return 0;
}
