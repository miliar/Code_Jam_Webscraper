#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;

int main () {
  long long t;
  cin >> t;
  string pancakes;
  for (int i = 0; i < t; i++) {
    cin >> pancakes;
    long long numOfReverses=0;
    char prefixIs = pancakes[0];
    for (int j = 0; j < pancakes.size()-1; j++) {
      while (j < pancakes.size() && pancakes[j] == prefixIs) {
// 	cout << "same " << prefixIs << endl;
	j++;
      }
      //changed
      if (j < pancakes.size()) {
// 	cout << "changed " << prefixIs << " to " << pancakes[j] << endl;
	prefixIs = pancakes[j];
	numOfReverses++;
	j --;
      }
    }
    if (prefixIs == '+') {
      cout << "Case #" << i + 1 << ": " << numOfReverses << endl;
    } else {
      cout << "Case #" << i + 1 << ": " << numOfReverses + 1 << endl;
    }
  }
  return 0;
}