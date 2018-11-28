#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
using namespace std;
string generate_string(long long a){
  string str= "";
  int tmp, k = 1;
  while(a){
    tmp = a & 1;
    a = a >> 1;
    str += (tmp + '0');
  }
  for(int i = 0; i < str.length()/2; i++){
    swap(str[i], str[str.length()-i-1]);
  }
  return str;
}
long long fast_pow(int a, int p){
  long long out = 1;
  while(p){
    if(p&1)
      out *= a;
    a *= a;
    p /= 2;
  }
  return out;
}
long long convert_base(int b, string str){
  long long out = 0;
  int digit = 0;
  for(int i = 0;i < str.length(); i++){
    out += (str[str.length()-1-i]-'0')*fast_pow(b, i);
  }
  return out;
}
long long is_prime(long long a){
  if(a <= 2)  return 0;
  for(int i = 2; i <= sqrt(a); i++){
    if(a%i == 0){
      return i;
    }
  }
  return 0;
}
int main(){
  int t, n, J, k, count = 0, temp;
  long long tmp, store[9], divisor;
  string str;
  scanf("%d%d%d",&t,&n,&J);
  printf("Case #1:\n");
  for(int i = fast_pow(2,n-1)+1; i < fast_pow(2,n); i+=2){
    if(count == J)  break;
    str = generate_string(i);
    memset(store, 0, sizeof(0));
    k = 0;
    for(int j = 2; j <= 10; j++){
      tmp = convert_base(j, str);
      divisor = is_prime(tmp);
      if(divisor == 0){
        break;
      }
      else{
          store[k++] = divisor;
      }
      if(j == 10){
        count++;
        printf("%s ", str.c_str());
        for(int m = 0; m < 9; m++){
          printf("%lld ", store[m]);
        }
        printf("\n");
      }
    }
  }
}
