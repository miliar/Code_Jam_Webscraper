#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {

  string line;
  ifstream fileToReadFrom;
  fileToReadFrom.open("/home/daeyeon/workspace/cpp/A-large.in");

  ofstream fileToWriteTo;
  fileToWriteTo.open("/home/daeyeon/workspace/cpp/question1-Large.out");
  
  int numCase;
  int numShyness;
  char shyness;

    fileToReadFrom >> numCase;

    for (int i=0; i<numCase; i++) {
     
      int numPeopleNeeded = 0;
      int numPeopleSofar = 0;
      fileToReadFrom >> numShyness;
     
      for (int j=0;j<=numShyness;j++) {
	fileToReadFrom >> shyness;
	int temp = int(shyness-'0');
	
	if(j>numPeopleSofar) {
	  int currentlyNeeded = j-numPeopleSofar;
	  numPeopleNeeded += currentlyNeeded;
	  numPeopleSofar += currentlyNeeded;
	
	}	
	numPeopleSofar += temp;
      }
      fileToWriteTo << "Case #" << i+1 << ": "<< numPeopleNeeded<<endl;
    }


    fileToReadFrom.close();

  fileToWriteTo.close();

  return 0;
}



