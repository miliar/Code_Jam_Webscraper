#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <deque>
#include <stack>
#include <sstream>

using namespace std;

int main(int argc, char *argv[]) {
  size_t T;
  cin >> T;
  for (size_t i = 1; i <= T; ++i) {
    size_t Smax;
    cin >> Smax;
    string shyness;
    cin >> shyness;
    size_t result = 0;
    size_t peopleStanding = 0;
    for (size_t j = 0; j <= Smax; ++j) {
      // get people standing now
      if (peopleStanding < j) {
        result += j - peopleStanding;
        peopleStanding = j;
      }
      peopleStanding += shyness[j] - '0';
    }
    cout << "Case #" << i << ": " << result << endl;
  }
  return 0;
}