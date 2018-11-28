#include <iostream>
#include <string>

using namespace std;

int main() {
  int T;
  cin >> T;
  for(int t = 1; t <= T; t++) {
    string input;
    cin >> input;
    string current_word("");
    current_word += input[0]; // add first letter to current_word
    for(int i = 1; i < input.size(); i++) {
      if(input[i] >= current_word[0]) {
        current_word = input[i] + current_word;
      } else {
        current_word = current_word + input[i];
      }
    }
    cout << "Case #" << t << ": " << current_word << endl;
  }
}
