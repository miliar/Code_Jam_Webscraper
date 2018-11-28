#include <iostream>
#include <string>
using namespace std;

int main() {
  int T;
  cin >> T;
  for (int cas = 1; cas <= T; ++cas) {
    int smax;
    string people;
    cin >> smax >> people;
    int friends = 0, standing = 0;
    for (int i = 0; i < people.size(); ++i) {
      if (people[i] != '0') {
        if (standing < i) {
          friends += i - standing;
          standing = i;
        }
        standing += people[i] - '0';
      }
    }
    cout << "Case #" << cas << ": " << friends << endl;
  }
}
