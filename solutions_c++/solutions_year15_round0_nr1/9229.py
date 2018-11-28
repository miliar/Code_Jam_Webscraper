#include <iostream>
#include <algorithm>
//#include <limits.h>
#include <vector>

using namespace std;

int toInt(char c) {
  return int(c) - int('0');
}

int main() {
  int t;
  cin>>t;

  for (int i = 0; i < t; i++) {

    vector<int> spectators;

    int smax = 0;
    cin>>smax;

    string levels;
    cin>>levels;

    for (int j = 0; j < levels.size(); j++) {
      spectators.push_back(toInt(levels[j]));
    }

    // Solving stuff
    int sol = 0;
    int availablePeople = 0;

    int currentPeople = 0;

    for (int j = 0; j < spectators.size(); j++) {
      if (spectators[j] == 0) continue;
      if (currentPeople < j) {
        sol += (j - currentPeople);
      }
      availablePeople += spectators[j];
      currentPeople = availablePeople + sol;
    }

    cout<<"Case #"<<(i+1)<<": "<<sol<<endl;
  }

  return 0;
}
