#include <iostream>
#include <vector>
// #include <string>

using namespace std;

int main() {

  // exit(1);
  int numCases;
  cin >> numCases;
  for(int i = 1; i <= numCases; i++) {
    string thing;
    cin >> thing;

    int cost = 0;
    bool plus = true;

    for(int j = thing.length() - 1; j >= 0; j--) {
      if(plus != (thing[j] == '+')) {
        plus = !plus;
        cost++;
      }
    }

    cout << "Case #" << i << ": " << cost << endl;

  }
}