#include <cstdio>
#include <cstring>
using namespace std;

int C=1;
int T,n,res,dif,up;
char s[1024];

int main(){

  scanf("%d",&T);
  while(T--){
    scanf("%d %s",&n,s);
    res = 0;
    up = s[0]-'0';
    for(int i=1;i<=n;i++){
      if(i>up){
        dif = i-up;
        res += dif;
        up += dif;
      }
      up = up + s[i]-'0';
    }
    printf("Case #%d: %d\n",C++,res);
  }

}
