#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;
double C,F,X,ans,s,spe;

void dfs(){
  //if (ans-s<1e-6) return;
  while (ans>s+X/spe){
    ans=s+X/spe;
    s+=C/spe; spe+=F;
  }
}

int main(){
  //freopen("a.in","r",stdin);
  //freopen("a.out","w",stdout);
  int T;
  scanf("%d",&T);
  for (int I=1;I<=T;I++){
  	scanf("%lf%lf%lf",&C,&F,&X);
  	ans=1e9; s=0; spe=2;
  	ans=ans*ans;
  	dfs();
  	printf("Case #%d: %.7lf\n",I,ans);
  }
  return 0;
}
