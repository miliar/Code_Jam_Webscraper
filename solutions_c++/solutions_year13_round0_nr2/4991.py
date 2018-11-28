#include <cstdio>
#include <cstring>
#include <algorithm>
#define MAX_N 100
#define MAX_M 100
using namespace std;
int T;
int M,N;
int Table[MAX_N+1][MAX_M+1];
int MHeight[MAX_M];
int NHeight[MAX_N];
int main(){
  scanf("%d",&T);
  for(int i=0;i<T;++i){
    memset(Table,0,sizeof(Table));
    memset(MHeight,0,sizeof(MHeight));
    memset(NHeight,0,sizeof(NHeight));
    scanf("%d%d",&M,&N);

    for(int j=0;j<M;++j)
      for(int k=0;k<N;++k)
	scanf("%d",&Table[j][k]);

    for(int j=0;j<M;++j){
      int mm=0;
      for(int k=0;k<N;++k){
	mm=max(mm,Table[j][k]);
      }
      MHeight[j]=mm;
    }

    for(int j=0;j<N;++j){
      int mm=0;
      for(int k=0;k<M;++k){
	mm=max(mm,Table[k][j]);
      }
      NHeight[j]=mm;
    }
    bool res=true;
    for(int j=0;j<M;++j)
      for(int k=0;k<N;++k)
	if(Table[j][k] < MHeight[j] && Table[j][k] < NHeight[k] )res=false;

    printf("Case #%d: ",i+1);


    if(res)printf("YES");
    else printf("NO");

    printf("\n");
  }

  return 0;
}
