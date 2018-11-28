#include<stdio.h>
#include<stdlib.h>
#include<string.h>

using namespace std;

const int MAX = 1000001;

int min(int lhs, int rhs){
  int result = 0;
  if(lhs < rhs){
    result = lhs;
  }
  else{
    result = rhs;
  }
  return result;
}

int getDecimalLog(int decimal){
  int result = 0;
  while(decimal > 9){
    result++;
    decimal = decimal/10;
  }
  return result;
}

int getDecimalPower(int decimalLog){
  int result = 1;
  for(int i=0; i<decimalLog; ++i){
    result *= 10;
  }
  return result;
}

int reverseDecimal(int decimal){
  int result = 0;
  int log = getDecimalLog(decimal);
  int decimalPower = getDecimalPower(log);
  for(int i=0; i<=log; ++i){
    result += (decimal%10)*decimalPower;    
    decimal = decimal/10;    
    decimalPower = decimalPower/10;    
  }
  return result;
}

int* preprocess(){
  static int data[MAX];
  data[0] = 0;
  for(int i=1; i<MAX; ++i){
    int reversed = reverseDecimal(i);
    if(reversed < i && i%10 != 0){
      data[i] = 1+min(data[i-1], data[reversed]);
    }
    else{
      data[i] = 1+data[i-1];
    }
  }
  return data;
}

long long loadValue(){
  static long long result = 0;
  scanf("%lld", &result);
  return result;
}

void showResult(long long result){
  printf("%lld", result);
}

long long calculate(int* processed, int value){
  return 0;
}

void run(int* processed){
  long long value = loadValue();
  long long result = 0;
  if(value < (long long)MAX){
    result = (long long) processed[(int) value];
  }
  else{
    result = calculate(processed, value);
  }
  showResult(result);
}

int main(){
  int* data = preprocess();
  int number;
  scanf("%d", &number);
  for(int i=1; i<=number; ++i){
    printf("Case #%d: ", i);
    run(data);
    printf("\n");
  }
  return 0;
}
