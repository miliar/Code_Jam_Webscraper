#include <bits/stdc++.h>
#include <string> 
using namespace std;


int digits[10];

int isAllDigist(){

  bool isAllDigist = true;

  for(int i = 0; i < 10 ; ++i){
    if(digits[i] == -1 ){
      isAllDigist = false;
      break;
    } 
  }

  return isAllDigist;
}

unsigned long escapeInsomnia(unsigned long n, unsigned long count) {

  string str = to_string(n * count);
  for(int i=0; i < str.length(); ++i){
    int k = (int)str[i] - 48;
    digits[k] = 1;
  }
  if(isAllDigist())
    return (n * count);
  else{
    count++;
    return escapeInsomnia(n, count);
  }
}

int main () {

  int countOfTestCase;
  int chosenNumber;

  cin >> countOfTestCase;
  int origin = countOfTestCase;

  while (countOfTestCase--) {

    memset(digits, -1, sizeof(digits));

    cin >> chosenNumber;

    if(chosenNumber == 0){
       cout << "Case #" << (origin - countOfTestCase) << ": INSOMNIA" << endl;
    } else {
      cout << "Case #" << (origin - countOfTestCase) << ": " << escapeInsomnia(chosenNumber, 1) << endl;
    }
  }
  return 0;
}
