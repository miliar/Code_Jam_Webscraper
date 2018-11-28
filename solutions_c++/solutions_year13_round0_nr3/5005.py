// AUTHOR: Ray Powers
// DATE: April 13, 2013
// PLATFORM: C++98

// Description: The purpose of this program is to find fair-n-square numbers between a set interval.


#include<iostream>
#include<fstream>
#include<string>
#include<sstream>
#include<queue>
#include<algorithm>
#include<cmath>

using namespace std;

// Data Structure
struct testCase {
  int a;
  int b;
};


int processTestCase(testCase game);
// Function processes a test case for a correct sequence of values.
// pre: none
// post: none


int main (int argNum, char * argValues[]) {

  // Locals
  testCase tmpCase;
  int numOfLines = 0;
  queue<testCase> testCases;

  // Need to obtain test data.
  // Read in File Contents
  string filename = argValues[1];
  ifstream srcFile;
  srcFile.open(filename.c_str());
  if (srcFile.fail()) {
    return -1;
  }  

  // File was opened. Proceed to read in contents.
  if (srcFile.is_open()) {
    srcFile >> numOfLines;
    numOfLines += 1;
    // Store the rest of the data.
    for (int i = 1; i < numOfLines; i++) {
      srcFile >> tmpCase.a;
      srcFile >> tmpCase.b;
      //cout << tmpCase.a << " and " << tmpCase.b << endl;
      testCases.push(tmpCase);
    }
    
  }
  srcFile.close();
  srcFile.clear();

  // Process 
  for (int i = 1; i < numOfLines; i++) {
    tmpCase = testCases.front();
    testCases.pop();
    cout << "Case #" << i << ": " << processTestCase(tmpCase) << endl;
  }

  return 0;
}


int processTestCase(testCase game) {
  
  // Locals
  int answer = 0;
  //cout << game.a << " with " << game.b << endl;

  // Process Game
  for (int i = game.a; i < (game.b + 1); i++) {
    stringstream ss;
    ss.clear();
    ss << i;
    string tmpStr = ss.str();
    //cout << tmpStr << endl;
    ss.flush();
    bool isPalindrome = true;
    for (int j = 0; j < (tmpStr.length() / 2); j++) {
      if (tmpStr[j] != tmpStr[tmpStr.length() - j -1]) {
	// Not a Palindrome. :(
	isPalindrome = false;
	break;
      }
    }

    if (isPalindrome) {
      // check square.
      double root = sqrt(i);
      stringstream tmpSS;
      string rootStr;
      tmpSS.flush();
      tmpSS << root;
      tmpSS >> rootStr;
      //cout << "Square is: " << rootStr << endl;
      tmpSS.flush();

      for (int j = 0; j < (rootStr.length() / 2); j++) {
	if (rootStr[j] != rootStr[rootStr.length() - j -1]) {
	  // Not a Palindrome. :(
	  isPalindrome = false;
	  break;
	}
      }
      
      if (isPalindrome) {
	answer++;
      }
    }
  }


  return answer;
}
