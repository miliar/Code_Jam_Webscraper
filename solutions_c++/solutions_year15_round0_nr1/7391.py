#include <iostream>
#include <fstream>
#include <string>

using namespace std;


int parseLine(int maxShyness, string line){
  int totalOvation = 0;
  int guests = 0;
  bool allClapping = false;
    for(int shynessLevel = 0; shynessLevel <= maxShyness; shynessLevel++){
      if(totalOvation >= shynessLevel) {
	totalOvation += line[shynessLevel] - '0';
      }
      else {
	++guests;
	++totalOvation;
	--shynessLevel;
      }
    }
    return guests;
}

int main(int argc, char** argv) {
  ifstream input;
  int numCases = 0;
  int maxShyness;
  string line;
  input.open(argv[1]);
  input >> numCases;
  for(int lineNum = 0; lineNum < numCases; lineNum++) {
    input >> maxShyness;
    input >> line;
    cout  << "case #" << lineNum + 1 << ": " << parseLine(maxShyness, line) << endl;
  }
  
  return 0;
}
