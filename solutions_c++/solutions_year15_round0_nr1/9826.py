#include <string>
#include <iostream>
#include <sstream>
#include <stdio.h>
using namespace std;

int main (int argc, char const *argv[])
{
  string format = "Case #%d: %d\n";
  stringstream parse;
  string stringIn;
  int numCases;
  
  getline(cin, stringIn);
  numCases = atoi(stringIn.c_str());

  for(int i = 0; i < numCases; i++) {
    string audience_string;
    int audience[1000 + 1];
    int standing = 0;
    int missing = 0;
    int n;

    // parse the line into x, r and c
    getline(cin, stringIn);
    parse.clear();
    parse.str("");
    parse << stringIn;
    parse >> n;
    parse >> audience_string;

    //read in the audience count
    for(int j = 0; j < n+1; j++) {
      audience[j] = audience_string[j] - '0';
    }

    // check each audience shyness level in turn
    for(int j = 0; j < n+1; j++) {
      // add missing audience members if necessary
      if (standing < j && audience[j]) {
        missing += j - standing;
        standing += missing;
      }
      standing += audience[j];
    }

    printf(format.c_str(), i + 1, missing);
  }

  return 0;
}
