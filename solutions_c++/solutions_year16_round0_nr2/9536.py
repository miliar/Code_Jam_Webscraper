#include <iostream>
#include <string>
#include <vector>

#define LENGTH	101

using namespace std;

int main() {
  int T, n;
  char input[LENGTH];
  string panString;
  vector<bool> pancakes;

  cin >> T;
  cin.getline (input, LENGTH);
  
  for (int t = 1; t <= T; ++t) {
    //reading input and transforming it into bool vector
    cin.getline (input, LENGTH);
    panString = input;
    
    n = panString.size();
    pancakes.resize(n);
    
    int vecIter = 0;
    for (string::iterator strIt = panString.begin(); strIt != panString.end(); ++strIt) {
      if (*strIt == '+') {
	pancakes[vecIter] = true;
      } else {
	pancakes[vecIter] = false;
      }
      ++vecIter;
    }
        
    //performing greedy algorithm
    int maneuver = 0;
    int i;
    bool tmp;
    while (n > 0) {
      
      i = n - 1;
      while (i >= 0 && pancakes[i] == true) {
	--i;
      }
      n = i + 1;
      
      if (n == 0) break;
      
      if (pancakes[0] == true) {
	while(i >= 0 && pancakes[i] != true) {
	  --i;
	}
      }
      
      if (i == 0) {
	pancakes[0] = !pancakes[0];
      } else {
	for (int j = 0; j < (i + 1)/2; ++j) {
	  tmp = !pancakes[j];
	  pancakes[j] = !pancakes[i - j];
	  pancakes[i - j] = tmp;
	}
	if (i % 2 == 0) {
	  pancakes[i/2] = !pancakes[i/2];
	}
      }
      
      ++maneuver;
    }
    
    cout << "Case #" << t << ": " << maneuver << endl;
    
  }
  
  return 0;
}