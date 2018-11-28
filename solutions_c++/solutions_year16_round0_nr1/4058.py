#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <vector>
using namespace std;
int a=0;
int p=0,t;
int q[1000005];
int main(){
  for (int i=1;i<=1000000;i++){
    p=a=0;
    while(a-1023){
      p+=i;
      t=p;
      while(t){
        a|=1<<(t%10);
        t/=10;
      }
    }
    q[i]=p;
  }
  int T,n,ca=0;
  freopen("a.txt","r",stdin);
  freopen("b.txt","w",stdout);
  scanf("%d",&T);
  while(T--){
    scanf("%d",&n);
    printf("Case #%d: ",++ca );
    if (!n)
      puts("INSOMNIA");
      else printf("%d\n", q[n]);
  }
  return 0;
}