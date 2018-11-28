#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;
bool ok[10];
bool check(long long s){
  int ct = 0;
  while(s){
    ok[s%10] = true;
    s/=10;
  }
  for(int i=0;i<10;i++){
    if(ok[i]){
      ct++;
    }
  }
  return ct==10;
}
int main(){
  int T;
  scanf("%d",&T);
  for(int cas=1;cas<=T;cas++){
    memset(ok,false,10);
    long long n;
    scanf("%lld",&n);
    long long res = 0;
    for(long long i=1;i<=100000;i++){
      if(check(n*i)){
        res = n*i;
        break;
      }
    }
    printf("Case #%d: ", cas);
    if(res == 0){
      printf("INSOMNIA\n");
    } else {
      printf("%lld\n",res);
    }
  }
  return 0;
}