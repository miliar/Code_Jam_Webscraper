#include<stdio.h>
#include<stdlib.h>
#include<set>

using namespace std;

int const MAX = 4;
int number;
int first, second;
set<int> myset;
int result;

void insert(int element){
  unsigned int size = myset.size();
  myset.insert(element);
  if(size == myset.size()){
    result = element;
  }
}

void load(int num){
  int loaded;
  for(int i=1; i<=MAX; ++i){
    for(int j=1; j<=MAX; ++j){
      scanf("%d", &loaded);
      if(i==num){
	insert(loaded);
      }
    }
  }
}

void printResult(){
  if(myset.size() == 2*MAX){
    printf("Volunteer cheated!");
  }
  else{
    if(myset.size() == 2*MAX-1){
      printf("%d", result);
    }
    else{
      printf("Bad magician!");
    }
  }
}

void run(){
  scanf("%d", &first);
  load(first);
  scanf("%d", &second);
  load(second);
  printResult();
  myset.clear();
}

int main(){
  scanf("%d", &number);
  for(int i=1; i<=number; ++i){
    printf("Case #%d: ", i);
    run();
    printf("\n");
  }
  return 0;
}
