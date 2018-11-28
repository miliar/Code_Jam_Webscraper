#include <iostream>
#include <string>
using namespace std;

int main() {
  int t;
  cin >> t;
  for(int cc = 1; cc <= t; cc++) {
    string s, result ="";
    cin >> s;
    result += s[0];
    for(int i = 1; i < (int)s.size(); i++) {
      if(s[i] >= result[0])
	result = s[i] + result;
      else
	result = result + s[i];
    }

    cout << "Case #" << cc << ": " << result << endl;
  }
  return 0;
}
