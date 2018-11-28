
#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

bool allDigits(bool digits[10], int kevin);

int main(){
  ofstream outputStream ("CodeJam1Output.txt");
  ifstream inputStream ("A-large.in");
  //outputStream << "kevin" << endl;
  int startNum;
  int k;
  int result;
  bool done;
  int cases;
  inputStream >> cases;
  cases += 1;
  bool dig[10];
  for (int j = 1; j < cases; j++){
    for (int lemon = 0; lemon < 10; lemon++){
      dig[lemon] = false;
    }

    inputStream >> startNum;
    if (startNum == 0) {outputStream << "Case #" << j << ": INSOMNIA" << endl; continue;}
    k = 0;
    done = false;
    while(!done){
      k += 1;
      done = allDigits(dig, startNum * k);
    }
    result = startNum * k;
    outputStream << "Case #" << j << ": " << result << endl;
  }
  outputStream.close();
  inputStream.close();
}


bool allDigits(bool digits[10], int kevin){
  int digit;
  int numDigits;
  numDigits = ceil(log10(kevin));
  if ((kevin % 10) == 0){numDigits += 1;}
  if (numDigits == 0) {numDigits += 1;}


  for (int i = 0; i < numDigits; i++){
    digit = kevin % 10;
    digits[digit] = true;
    kevin /= 10;
  }
  for (int i = 0; i != 10; i++){
    if (digits[i] == false){
    return false;
    }
  }
  return true;

}
