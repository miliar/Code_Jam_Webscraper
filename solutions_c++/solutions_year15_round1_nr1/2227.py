#include <iostream>
#include <fstream>

using namespace std;

int main() {

  ifstream fileToReadFrom;
  fileToReadFrom.open("/home/daeyeon/workspace/cpp/round1a/A-large(1).in");

  ofstream fileToWriteTo;
  fileToWriteTo.open("/home/daeyeon/workspace/cpp/round1a/A-large.out");

  int numCase;
  int numSnapshots,currentNum;
  int lastNum;
  int allValues[10000];
  int maxInterval;
  
  fileToReadFrom >> numCase;

  for (int i=0; i<numCase; i++) {
    fileToReadFrom >> numSnapshots;
    int sumTotal = 0;
    int regularTotal = 0;

    fileToReadFrom >>  lastNum;
    allValues[0] = lastNum;
    maxInterval = 0;

    for (int j=1; j<numSnapshots; j++) {
      fileToReadFrom >> currentNum;
      allValues[j] = currentNum;
      if(lastNum > currentNum) {
	int currentInterval = lastNum-currentNum;
	sumTotal += currentInterval;
	if (currentInterval > maxInterval) maxInterval = currentInterval;  
      }

      lastNum = currentNum;
    }

    for (int k=1; k<numSnapshots; k++) {
      if (allValues[k-1]<maxInterval) 
	regularTotal += allValues[k-1];
      else 
	regularTotal += maxInterval;
    }

    fileToWriteTo << "Case #" << i+1 << ": " << sumTotal << " " << regularTotal << endl;
  }

  fileToReadFrom.close();
  fileToWriteTo.close();
  return 0;
}
