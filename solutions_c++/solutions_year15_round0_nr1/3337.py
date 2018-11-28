#include<stdio.h>
#include<stdlib.h>
#include<string.h>

using namespace std;

const int MAX = 2000;

int convert(char digit){
  static char offset = '0';
  return digit - offset;
}

int loadMax(){
  static int result = 0;
  scanf("%d", &result);
  return result;
}

int* parseData(char* data, int max){
  static int parsed[MAX];
  for(int i=0; i<=max; ++i){
    parsed[i] = convert(data[i]);
  }
  return parsed;
}

int* loadData(int max){
  static char data[MAX];
  scanf("%s\n", data);
  return parseData(data, max);
}

int getFirst(int* data){
  return data[0];
}

int check(int acc, int index){
  if(acc < index){
    return index-acc;
  }
  else{
    return 0;
  }
}

int execute(int max, int* data){
  int result = 0;
  int acc = getFirst(data);
  for(int i=1; i<=max; ++i){
    int additionals = check(acc, i);
    acc += data[i]+additionals;
    result += additionals;
  }
  return result;
}

void showResult(int result){
  printf("%d", result);
}

void run(){
  int max = loadMax();  
  int* data = loadData(max);  
  showResult(execute(max,data));
}

int main(){
  int number;
  scanf("%d", &number);
  for(int i=1; i<=number; ++i){
    printf("Case #%d: ", i);
    run();
    printf("\n");
  }
  return 0;
}
