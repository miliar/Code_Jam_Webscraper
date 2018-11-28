#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
double c,f,x,p,s,ans;
int t,tt;

int main(){
  freopen("1.txt","r",stdin);
  freopen("2.txt","w",stdout);
  scanf("%d",&t);
  for (tt=1;tt<=t;++tt){
    scanf("%lf%lf%lf",&c,&f,&x);
    p=2;
    ans=x/p;
    s=c/p;
    p+=f;
    while (s+x/p<ans){
      ans=s+x/p;
      s+=c/p;
      p+=f;
    }
    printf("Case #%d: %.7f\n",tt,ans);
  }
  return 0;
}