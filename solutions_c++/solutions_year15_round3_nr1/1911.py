#include<stdio.h>
#include<stdlib.h>

using namespace std;

const int MAX = 0;

int loadNumber(){
  static int number = 0;
  scanf("%d", &number);
  return number;
}

int count(int rows, int columns, int ship){
  return ship-1+(((columns-1)/ship)+1)*rows;
}

void showResult(int result){
  printf("%d", result);
}

void run(){  
  int rows = loadNumber();
  int columns = loadNumber();
  int ship = loadNumber();
  showResult(count(rows, columns, ship));
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
