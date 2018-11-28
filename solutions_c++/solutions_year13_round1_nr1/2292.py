#include <iostream>

#include <fstream>

#include <string>

#include <Math.h>

using namespace std;

int lawn [100][100];

int main(int argc, char *argv[])
{
  ifstream inputFile;
  inputFile.open(argv[1]);

  //string numOfInputStr;
  //getline(inputFile, numOfInputStr);
  //int numOfInput = atoi(numOfInputStr.c_str());
  int numOfInput;

  inputFile >> numOfInput;

  //cout << argv[1] << endl;
  //cout << numOfInput << endl;

  for(int inputIndex=0; inputIndex<numOfInput; inputIndex++) {

    unsigned long long int firstRadius;
    inputFile >> firstRadius;

    unsigned long long int startedPaint;
    inputFile >> startedPaint;

    if(firstRadius<=100000&&startedPaint<=100000000) {
      unsigned long long int firstBlackArea = 2*(firstRadius+1)-1;
      unsigned long long int b = (firstBlackArea-2);
      unsigned long long int answer = floor((sqrt(b*b + 8*startedPaint) - b) / 4);
      cout << "Case #" << inputIndex+1 << ": " << answer << endl;
    } else {
      unsigned long long int remainingPaint = startedPaint;
      unsigned long long int currentRadius = firstRadius;

      bool isWhite = true;

      unsigned long long int blackCount = 0;

      while(remainingPaint>0) {
        if(isWhite) {
          currentRadius++;
          isWhite = false;
        } else {
          unsigned long long int neededPaint = 2*currentRadius -1;
          if(remainingPaint>=neededPaint) {
            remainingPaint-=neededPaint;
            blackCount++;
            currentRadius++;
            isWhite = true;
          } else {
            break;
          }
        }
      }

      cout << "Case #" << inputIndex+1 << ": " << blackCount << endl;
    }

  }

  return 0;
} 
