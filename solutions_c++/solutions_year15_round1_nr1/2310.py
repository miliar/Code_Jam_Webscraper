#include<stdio.h>
#include<stdlib.h>

using namespace std;

const int MAX = 20000;

int min(int a, int b){
  if(a < b){
    return a;
  }
  else{
    return b;
  }
}

int loadSize(){
  static int size = 0;
  scanf("%d", &size);
  return size;
}

int* loadData(int size){
  static int data[MAX];
  for(int i=0; i<size; ++i){
    scanf("%d", &data[i]);
  }
  return data;
}

int findFirst(int size, int* data){
  int result = 0;
  for(int i=0; i<size-1; ++i){
    if(data[i+1] < data[i]){
      result += data[i]-data[i+1];
    }
  }
  return result;
}

int findMaxDifference(int size, int* data){
  int result = 0;
  for(int i=0; i<size-1; ++i){
    if(result < data[i]-data[i+1]){
      result = data[i]-data[i+1];
    }
  }
  return result;
}

int findSecond(int size, int* data){
  int max = findMaxDifference(size, data);
  int result = 0;
  for(int i=0; i<size-1; ++i){
    result += min(data[i], max);
  }
  return result;
}

void showResults(int first, int second){
  printf("%d %d", first, second);
}

void run(){
  int size = loadSize();
  int* data = loadData(size); 
  int first = findFirst(size, data);
  int second = findSecond(size, data);
  showResults(first, second);
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
