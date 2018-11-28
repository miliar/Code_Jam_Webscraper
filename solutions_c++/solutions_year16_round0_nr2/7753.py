#include <iostream>
#include <string>

using namespace std;

void copyStack(string str, char* stack){
  for (int i = 0; i < str.length(); i++){
    stack[i] = str[i];
  }
  stack[str.length()] = 0;
}

char flipCake(char cake){
  if (cake == '+') return '-';
  return '+';
}

void doFlip(char* stack, int lastIndex){
  int swapLow = 0;
  int swapHigh = lastIndex;
  char temp;
  while (swapHigh > swapLow){
    temp = flipCake(stack[swapHigh]);
    stack[swapHigh] = flipCake(stack[swapLow]);
    stack[swapLow] = temp;
    swapHigh--;
    swapLow++;
  }
  if (swapHigh == swapLow){
    stack[swapHigh] = flipCake(stack[swapHigh]);
  }
}

int getEndOfNextRun(char* stack){
  for (int i = 0; i <= 100; i++){
      if (i == 99 || stack[i] != stack[i+1]){
        return i;
    }
  }
  return -1;
}

bool isAllUp(char* stack){
  for (int i = 0; i < 100; i++){
    if (stack[i] == '-'){
      return false;
    }
    if (stack[i] == 0){
      return true;
    }
  }
  return true;
}

int main(int argc, char** argv){

  int numTestCases;
  cin >> numTestCases;

  char stack[100];

  for (int t = 1; t <= numTestCases; t++){
    string stackString;
    int numFlips = 0;

    cin >> stackString;

    copyStack(stackString, stack);
    //cout << "Stack: " << stackString << endl;

    while (!isAllUp(stack)){

      int index = getEndOfNextRun(stack);
      //cout << "Stack Before: " << stack << " ~ " << index << endl;
      doFlip(stack, index);
      numFlips++;
      if (isAllUp(stack)){
        index = -1;
      }
      //cout << "Stack After:  " << stack << endl;
    }

    cout << "Case #" << t << ": " << numFlips << endl;
  }

  return 0;
}
