#include <iostream>
#include <algorithm>
#include <cassert>
using namespace std;

int solve(string shynessString, int maxShy) {
  int sumShyness[maxShy+1]; // sumShyness[i] is sum of shyness from 0 to i inclusive
  int peopleNeeded = 0;
  sumShyness[0] = (int)(shynessString[0]-'0');
  assert(0 <= sumShyness[0] && sumShyness[0] <= 9);
  for (int i = 1; i <= maxShy; i++) {
    if (i - sumShyness[i-1] > peopleNeeded) peopleNeeded = i - sumShyness[i-1];
    sumShyness[i] = sumShyness[i-1] + (int)(shynessString[i]-'0');
    assert(0 <= (int)(shynessString[i]-'0') && (int)(shynessString[i]-'0') <= 9);
  }
  return peopleNeeded;
}

int main () {
  int T;
  cin >> T;
  for (int tc = 1; tc <= T; tc++) {
    int maxShy;
    string shyness;
    cin >> maxShy;
    cin >> shyness;
    cout << "Case #" << tc << ": " << solve(shyness, maxShy) << endl;
  }
}
