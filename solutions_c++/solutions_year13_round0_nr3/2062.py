#include<stdio.h>
#include<stdlib.h>

const int MAX = 10000001;
long long array[MAX];
long long table[100];
long long begin, end;
long long number;
long long test_case;
long long result;

bool palindrom(long long n){
  int index=0;
  bool ok = true;
  while(n>0){
    table[index] = n%10;
    n = n/10;
    ++index;
  }
  int k = index-1;
  for(int i=0; i<index; ++i){
    if(table[i] != table[k]){
      ok = false;
      break;
    }
    k--;
  }
  return ok;
}

int main(){
  int j = 0;
  for(long long i=1; i<10000001; ++i){
    if(palindrom(i) && palindrom(i*i)){
      array[j] = i*i;
      j++;
    }
  }
  scanf("%lld", &number);
  for(int i=0; i<number; ++i){
    test_case = i+1;
    result = 0;
    scanf("%lld", &begin);
    scanf("%lld", &end);
    for(int i=0; i<j; ++i){
      if(begin <= array[i] && array[i] <= end){
	result+=1;
      }
    }
    printf("Case #%lld: ", test_case);
    printf("%lld\n", result);
  }
}
