#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;


int s[1005];
int main(){
  freopen("B.in","r",stdin);
  freopen("B.out","w",stdout);
  int tt, n, i, x, j;
  scanf("%d",&tt);
  for(int cal=1;cal<=tt;++cal){
    scanf("%d",&n);
    memset(s,0,sizeof(s));
    for(i=1;i<=n;++i){
      scanf("%d",&x);
      s[x]++;
    }
    

    int tot, ans=1e9;
    for(i=1;i<=1000;++i){
      tot=0;
      for(j=i+1;j<=1000;++j){
        tot+=s[j]*((j-1)/i);
      }
      ans=min(ans,tot+i);
    }
    printf("Case #%d: %d\n", cal, ans);
  }  
    
  return 0;
}
