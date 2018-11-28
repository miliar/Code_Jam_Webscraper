#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {

  int T;
  cin >> T;

  for(int test = 1; test <= T; ++test) {

    string pancakes;
    cin >> pancakes;

    vector<char> vec;
    char current, prev = 0;

    for(int i = 0; i < pancakes.size(); ++i) {
      char pancake = pancakes[i];
      if(pancake == '+') {
        if(prev != pancake) vec.push_back('+');
      } else if(pancake == '-') {
        if(prev != pancake) vec.push_back('-');
      }
      prev = pancake;
    }

    // for(int it = 0; it != vec.size(); ++it) {
    //   cout << vec[it];
    // }

    int result = vec.size();
    if(vec.back() == '+') result--;
    cout << "Case #" << test << ": " << result;

    cout << endl;
    vec.clear();

  }

  return 0;
}
