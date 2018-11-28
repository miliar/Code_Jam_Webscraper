#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
  int T;
  cin >> T;

  for(int tt = 1; tt <= T; tt++) {
    int smax;
    string shyness;
    cin >> smax >> shyness;
    int current_standing = 0;
    int friends_added = 0;
    for(int i = 0; i < shyness.size(); i++) {
      int n = shyness[i] - '0';
      if (n > 0) {
        if (i > current_standing) {
          friends_added += i-current_standing;
          current_standing += i-current_standing;
        }
        current_standing += n;
      }
    
    }
    
    cout << "Case #" << tt << ": " << friends_added << endl;

  }

  return 0;
}
