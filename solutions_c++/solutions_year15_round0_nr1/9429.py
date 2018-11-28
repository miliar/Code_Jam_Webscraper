#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
  size_t ntests;
  cin >> ntests;

  for(size_t test=0 ; test < ntests ; test++) {
    int s_max;
    int acc = 0, friends = 0;
    string numbers;
    cin >> s_max;
    cin >> numbers;
    for(int i=0 ; i < s_max ; i++) {
      acc += stoi(numbers.substr(i,1));
      if(acc <= i+1) {
	friends += i+1 - acc;
	acc = i+1;
      }
    }
    cout << "Case #" << test + 1 << ": " << friends << endl;
  }
}
