#include <iostream>
#include <unordered_set>
#include <string>
using namespace std;

int main() {
  int T;
  cin >> T;
  for (int i = 1; i <= T; i++) {
    string str;
    cin >> str;
    // cout << str << ": " << endl;
    int num_flips = 0;
    while (str.find("-")!=string::npos) {
      char cur = str[0];
      int ptr = 1;
      while (ptr < str.length() && str[ptr] == cur) {
        ptr++;
      }
      string newstr = "";
      for (int i = ptr-1; i >= 0; i--) {
        if (str[i] == '-') {
          newstr = newstr + "+";
        } else {
          newstr = newstr + "-";
        }
      }
      newstr = newstr + str.substr(ptr);
      str = newstr;
      num_flips++;
      // cout << str << endl;
    }
    cout << "Case #" << i << ": " << num_flips << "\n";
  }
}
