#include<cstdio>
#include<algorithm>
#include<vector>
#include<cassert>
#include<utility>
#include<numeric>
using namespace std;
int T,n,t[1010][1010];
double x[1010],y[1010];
int calc(){
  int ans=0,x_from=0,x_to=n-1,y_from=0,y_to=n-1;
  while(x_from<=x_to){
    if(x[x_from]>y[y_from]){
      ++ans;
      ++x_from;
      ++y_from;
    }else{
      ++x_from;
      --y_to;
    }
  }
  return ans;
}
int calc2(){
  int ans=0,y_from=0,y_to=n-1;
  for(int i=n-1;i>=0;i--){
    if(x[i]>y[y_to]){
      ++ans;
      ++y_from;
    }else{
      --y_to;
    }
  }
  return ans;
}
main(){
  scanf("%d",&T);
  for(int t=1;t<=T;t++){
    scanf("%d",&n);
    for(int i=0;i<n;i++)scanf("%lf",&x[i]);
    for(int i=0;i<n;i++)scanf("%lf",&y[i]);
    sort(x,x+n);
    sort(y,y+n);
//for(int i=0;i<n;i++)printf("%.3lf ",x[i]);puts("");
//for(int i=0;i<n;i++)printf("%.3lf ",y[i]);puts("");
    int ans=calc(),ans2=calc2();
    printf("Case #%d: %d %d\n",t,ans,ans2);
  }
}
