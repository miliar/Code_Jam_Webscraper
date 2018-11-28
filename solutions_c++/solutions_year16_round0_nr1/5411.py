#include <cstdio>
#include <cstring>
int digits[10];
bool check(){
  for(int i = 0; i < 10; i++){
    if(digits[i] == 0){
      return false;
    }
  }
  return true;
}
void count_digit(long long a){
  int tmp;
  while(a){
    tmp = a % 10;
    a /= 10;
    digits[tmp] = 1;
  }
}
int main(){
  int t, k;
  long long n,store;
  scanf("%d",&t);
  for(int i = 0; i < t; i++){
    k = 2;
    scanf("%lld",&n);
    store = n;
    if(n == 0){
      printf("Case #%d: INSOMNIA\n", i+1);
      continue;
    }
    memset(digits, 0, sizeof(digits));
    while(1){
      count_digit(n);
      if(check()){
        printf("Case #%d: %lld\n",i+1, n);
        break;
      }
      else{
        n = store*k++;
      }
    }
  }
}
