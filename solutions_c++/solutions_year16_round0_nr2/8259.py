#include <bits/stdc++.h>
#include <string> 
using namespace std;


string pancakes;

char flipPancake(bool checkFace){
  if(checkFace)
    return '-';
  else
    return '+';
}

int flipCount() {

  bool checkFacePositive = false;
  if(pancakes[0] == '-')
    checkFacePositive = true;

  int count = 0;
  char compareChar = flipPancake(checkFacePositive);

  for(int i = 1; i < pancakes.length(); i++){
    
    if(pancakes[i] != compareChar)
    {
      count++;
      checkFacePositive = !checkFacePositive;
      compareChar = flipPancake(checkFacePositive);
      
    }
  }
  if(checkFacePositive) count++;
  return count;
}

int main () {

  int countOfTestCase;
  char cake;
  cin >> countOfTestCase;
  int origin = countOfTestCase;
  string s;
  getline(cin, s);

  while (getline(cin, pancakes))
  {
    countOfTestCase--;
    cout << "Case #" << (origin - countOfTestCase) << ": " << flipCount() << endl;
  }

  
  return 0;
}
