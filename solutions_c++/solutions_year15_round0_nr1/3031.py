#include <cstdio>
#include <cstring>
using namespace std;

char g[1005];
int main(){
  freopen("A-large.in","r",stdin);
  freopen("1.out","w",stdout);
  int tt;
  scanf("%d",&tt);
  for(int cal=1; cal<=tt; ++cal){
    int s, cur=0,tot=0;
    scanf("%d",&s);
    scanf("%s", g);
    for(int i=0; i<=s; ++i){
      int num = g[i]-'0';
      if(num && cur<i){
        tot+=i-cur;
        cur=i;
      }
      cur+=num; 
    }
    printf("Case #%d: %d\n", cal, tot);
  }
  return 0;
}
