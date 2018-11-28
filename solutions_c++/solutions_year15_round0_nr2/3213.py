#include<stdio.h>
#include<stdlib.h>
#include<set>

using namespace std;

int min(int lhs, int rhs){
  if(lhs < rhs){
    return lhs;
  }
  else{
    return rhs;
  }
}

int loadSize(){
  static int result = 0;
  scanf("%d\n", &result);
  return result;
}

multiset<int>& loadData(){
  static multiset<int> container;  
  static int element = 0;
  int size = loadSize();
  container.clear();
  for(int i=0; i<size; ++i){
    scanf("%d", &element);
    container.insert(element);
  }
  scanf("\n");
  return container;
}

int findMax(const multiset<int>& container){
  return *(container.rbegin());  
}

int increase(int value, int index){
  return (value-1)/index;
}

int calculate(int index, multiset<int>& container){
  int acc = 0;
  multiset<int>::iterator iter;
  for(iter = container.begin(); iter != container.end();){
    int value = *iter;
    if(value <= index){
      container.erase(iter++);
    }
    else{
      acc += increase(value, index);
      ++iter;
    }
  }
  return index+acc;
}

int execute(multiset<int>& container){
  int max = findMax(container);
  int result = max;
  for(int i=1; i<=max; ++i){
    int value = calculate(i, container);
    result = min(result, value);
  }
  return result;
}

void showResult(int result){
  printf("%d", result);
}

void run(){
  multiset<int> data = loadData();      
  showResult(execute(data));
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
