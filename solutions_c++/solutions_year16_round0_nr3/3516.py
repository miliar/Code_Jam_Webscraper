#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <vector>
int a[11]={0,0,3,2,5,2,7,2,3,2,11};
using namespace std;
int main(){
  freopen("b.txt","w",stdout);
  int T=50;
  int f=(1<<15)+1;
  puts("Case #1:");
  while(T){
    while(1){
      int cnt=0;
      long long p=0,q;
      for (int i=10;i>1;i--){
        p=0;
        long long ff=f,bas=1;
        while(ff){
          p=p+bas*(ff&1);
          ff/=2;
          bas*=i;
        }
        if (i==10) {q=p;}
        if (!(p%a[i])) cnt++;
      }
      f+=6;
      if (cnt==9){
        printf("%lld ", q);
        for (int i=2;i<=10;i++){
           if (i-2) printf(" ");
           printf("%d", a[i]);
         }
        puts("");
        break;
      }
    }
    T--;
  }

  return 0;
}