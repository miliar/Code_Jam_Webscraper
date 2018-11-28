#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int computeNumFriends(const vector<int>& levels) {
  if (levels.size() <= 1) {
    return 0;
  }
  int numFriends = 0;
  int currentStanding = levels[0];
  for (int i = 1; i < levels.size(); ++i) {
    if (currentStanding < i) {
      numFriends += i - currentStanding;
      currentStanding = i;
    }
    currentStanding += levels[i];
  }
  return numFriends;
}
 
int main(int argc, char** argv) {
  ifstream f("input");
  int numCases;
  f >> numCases;
  for (int i = 0; i < numCases; ++i) {
    int numLevels;
    string levelsStr;
    f >> numLevels >> levelsStr;
    ++numLevels;
    vector<int> levels;
    levels.reserve(numLevels);
    const char* cs = levelsStr.c_str();
    for (int j = 0; j <  numLevels; ++j) {
      levels.push_back(cs[j] - '0');
    }
    cout << "Case #" << i + 1 << ": " << computeNumFriends(levels) << endl;
  }
}
