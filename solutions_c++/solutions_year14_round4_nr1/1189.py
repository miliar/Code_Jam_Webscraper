#include<cstdio>
#include<algorithm>
#include<cstring>
#include<cassert>
using namespace std;

int n,c;
int tam[1123];
int foi[1123];

int main (){
  int tt;
  scanf("%d",&tt);
  for(int pp=1;pp<=tt;pp++){
    int ret=0;
    memset(foi,0,sizeof(foi));
    memset(tam,0,sizeof(tam));
    tam[0]=999999;
    
    scanf("%d %d",&n,&c);
    for(int i=0;i<n;i++){
      int a;
      scanf("%d",&a);
      tam[a]++;
    }
    for(int a=1100;a>=1;a--){
      if(tam[a]==0)continue;
      for(int b=c-a;b>=0;b--){
	if(a!=b){
	  int x = min(tam[a],tam[b]);
	  ret += x;
	  tam[b]-=x;
	  tam[a]-=x;
	}
	else {
	  ret += tam[a]/2;
	  tam[a] = tam[a]- 2*(tam[a]/2);
	}
	if(tam[a]<=0)break;
      }
      assert(tam[a]==0);
      
    }
    printf("Case #%d: %d\n",pp,ret);
      
  }
  return 0;
}
