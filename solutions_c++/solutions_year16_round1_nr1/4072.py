#include<iostream>
#include<string>

using namespace std;

string calculate(string s) {
  if (s.length() <= 1) {
    return s;
  } else {
    int max = 0;
    for (int i = 1; i < s.length(); i++) {
      if (s[i] >= s[max]) {
        max = i;
      }
    }
    return s[max] + calculate(s.substr(0, max)) + s.substr(max + 1);
  }
}

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    string s;
    cin >> s;
    string r = calculate(s);
    cout << "Case #" << t << ": " << r << endl;
  }
  return 0;
}
