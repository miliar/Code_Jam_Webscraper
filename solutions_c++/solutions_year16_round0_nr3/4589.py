#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

long long unsigned int len, t, n;
char str[33];

long long unsigned int lst[9];

long long unsigned int isPrime(long long unsigned int a){
  long long unsigned int to = (long long unsigned int)sqrt(a);
  for(long long unsigned int i=2;i<=to;i++){
    if(a%i==0) return i;
  }
  return 0;
}

long long unsigned int str2num(int base){
  long long unsigned int temp=1, s=0;
  for(long long int i=len-1;i>=0;i--){
    if(str[i]=='1') s+=temp;
    temp*=base;
  }
  return s;
}

bool isJamCoin(){
  // check lead and end char
  if(str[0]=='0' || str[len-1]=='0') return false;
  for(long long unsigned int i=2;i<=10;i++){
    long long unsigned int temp = str2num(i);
    long long unsigned int fac=isPrime(temp);
    if(fac==0) return false;
    else lst[i-2]=fac;
  }
  return true;
}

void init(){
  for(long long unsigned int i=0;i<len;i++) str[i]='0';
  str[0]=str[len-1]='1';
}

bool next(){
  long long unsigned int i=len-2;
  while(i>0){
    if(str[i]=='0'){
      str[i]='1';
      return true;
    }else{
      str[i]='0';
      i--;
    }
  }
  return false;
}

int main(int argc, char const *argv[]) {
  scanf("%llu\n", &t);
  scanf("%llu %llu\n", &len, &n);
  printf("Case #1:\n");
  init();
  while(n){
    if(isJamCoin()){
      printf("%s", str);
      for(long long unsigned int i=0;i<9;i++) printf(" %llu", lst[i]);
      printf("\n");
      n--;
    }
    next();
  }
  return 0;
}
