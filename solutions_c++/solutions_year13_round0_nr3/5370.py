#include <iostream>

#include <fstream>

#include <string>

#include <vector>

#include <sstream>

using namespace std;

string convertInt(unsigned long long int number)
{
   stringstream ss;//create a stringstream
   ss << number;//add number to the stream
   return ss.str();//return a string with the contents of the stream
}

bool isPalindrome(unsigned long long int numNum) {
  string numStr = convertInt(numNum); 
  bool isMirror = true;

  int firstDigitIndex=0;
  int lastDigitIndex=numStr.length()-1;
  for(; firstDigitIndex<lastDigitIndex; firstDigitIndex++, lastDigitIndex--) {
    if(numStr[firstDigitIndex]!=numStr[lastDigitIndex]) {
      isMirror = false;
    }
  }

  return isMirror;
}



int main(int argc, char *argv[])
{
  ifstream inputFile;
  inputFile.open(argv[1]);

  string numOfInputStr;
  getline(inputFile, numOfInputStr);
  int numOfInput = atoi(numOfInputStr.c_str());

  //cout << argv[1] << endl;
  //cout << numOfInput << endl;

  for(int inputIndex=0; inputIndex<numOfInput; inputIndex++) {

    //cout << "Time: " << inputIndex << endl;

    std::vector<unsigned long long int> palindromes;
    std::vector<unsigned long long int> fairAndSquares;
    std::vector<unsigned long long int>::iterator it;

    unsigned long long int lower;
    unsigned long long int upper;

    inputFile >> lower;
    inputFile >> upper;

    for(unsigned long long int theNumber=0; theNumber<=upper; theNumber++) {
      if(isPalindrome(theNumber)) {
        palindromes.push_back(theNumber);
        //cout << "Palindrome: " << theNumber << endl;
      }
    }

    for(unsigned long long int theNumber=lower; theNumber<=upper; theNumber++) {
      if(isPalindrome(theNumber)) {
        for(it = palindromes.begin();it<palindromes.end(); it++) {
          if((*it)*(*it)==theNumber) {
            fairAndSquares.push_back(theNumber);
            //cout << "Fair and Square: " << theNumber << endl;
          }
        }
      }
    }

    cout << "Case #" << inputIndex+1 << ": " << fairAndSquares.size() << endl;

  }

  return 0;
} 
