#include<iostream>
#include<math.h>

using namespace std;

void printCase(int cases, int fair){
  cout << "Case #" << cases << ": ";
  cout << fair;
  cout << endl;
}

int getDig(int i){
  int count = 0;
  while(i >= 10){
    i = i / 10;
    count++;
  }
  count++;
  return count;
}



int checkSym(int i, int length){
  if(length == 2){
    if(i/10 != i%10){
      return 0;
    }
  }
  if(length == 3){
    if(i == 676){
      return 0;
    }
    if(i/100 != i%10){
      return 0;
    }
  }
  return 1;  
}

int getFair(int min, int max){
  int count = 0;
  for(int i = min; i <= max; ++i){
    int j = pow(i, 0.5);
    int length = getDig(i);
    if((pow(j,2)==i) && checkSym(i, length)){
      count++;
    }
  }
  return count;
}

int main(){
  int i = 0;
  int fair = 0;
  int cases = 0, count = 0;
  cin >> cases;
  count = cases;
  while(count > 0){
    int min = 0, max = 0;
    cin >> min >> max;
    fair = getFair(min, max);
    printCase(cases-count+1, fair);
    count--;
  }
  return 0;
}
