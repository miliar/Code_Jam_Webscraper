//#include <stdlib.h>
#include <stdio.h>
#include <vector>
//#include 

void readInput(std::vector<int> & aud) {
  int maxAud = 0;
  char audInput[1024] = {0};
  scanf("%d %s", &maxAud, audInput);
  //  aud.resize(maxAud + 1);
  //printf("maxAud: %d\n", maxAud);
  for (int i = 0; i < maxAud + 1; ++i) {
    int size = audInput[i] - '0';
    aud.push_back(size);
    // printf("next val: %d\n", size);
  }
}

int calcAnswer(std::vector<int> & aud) {
  int numStanding = 0;
  int friends = 0;
  for (int i = 0; i < aud.size(); ++i) {
    // printf("i = %d, numstand = %d, friends = %d\n", i, numStanding, friends);
    if (i > numStanding) {
      int diff = i - numStanding;
      friends += diff;
      numStanding += diff;
    }
    numStanding += aud[i];
  }
  return friends;
}

void printAnswer(int testNum, int answer) {
  printf("Case #%d: %d\n", testNum + 1, answer);
}

int main()
{
  int numCases = 0;
  scanf("%d", &numCases);
  for (int i = 0; i < numCases; ++i) {
    //printf("test case %d\n", i);
    std::vector<int> aud;
    readInput(aud);
    int answer = calcAnswer(aud);
    printAnswer(i, answer);
  }
}
