// AUTHOR: Ray Powers
// DATE: April 12, 2013
// PLATFORM: C++98

// Description: The purpose of this program is to determine the correct sequence of treasure chests to open.


#include<iostream>
#include<fstream>
#include<string>
#include<sstream>
#include<queue>
#include<algorithm>

using namespace std;

// Data Structure
struct testCase {
  int n;
  int m;
  int grass[10][10];
};


string processTestCase(testCase treasureHunt);
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
      srcFile >> tmpCase.n;
      srcFile >> tmpCase.m;
      for (int j = 0; j < tmpCase.n; j++) {
	for (int k = 0; k < tmpCase.m; k++) {
	  srcFile >> tmpCase.grass[j][k];
	  //cout << tmpCase.grass[j][k] << " ";
	}
	//cout << endl;
      }

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


string processTestCase(testCase game) {
  
  // Locals
  const string NO = "NO";
  const string YES = "YES";
  string answer = "YES";

  // Process Game
  for (int i = 0; i < game.n; i++) {
    for (int j = 0; j < game.m; j++) {
      if (answer != NO) {
	if (game.grass[i][j] == 1) {
	  // Check to see if this swath was possible.
	  // Check vertical
	  bool vertCheck = true;
	  for (int k = 0; k < game.n; k++) {
	    if (game.grass[k][j] == 2) {
	      vertCheck = false;
	    }
	  }

	  // Check Horizontal
	  bool horizCheck = true;
	  for (int k = 0; k < game.m; k++) {
	    if (game.grass[i][k] == 2) {
	      horizCheck = false;
	    }
	  }

	  // Check
	  if (horizCheck || vertCheck) {
	    // Path is ok.
	    answer = YES;
	  
	  } else {
	    // Not possible
	    answer = NO;
	  }
	}
      }
    }
  }


  return answer;
}
