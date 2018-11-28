#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string flip(string s) {
    for (int i=0; i<s.length(); i++) {
        s[i] = s[i] == '+' ? '-' : '+';
    }
    return s;
}
int count(string s) {
    if (s.length() == 1) {
        return s[0] == '+' ? 0 : 1;
    } else {
        return s[s.length()-1] == '+' ? count(s.substr(0, s.length()-1)) : 1 + count(flip(s.substr(0, s.length()-1)));
    }
}
int main () {
    int n;
    cin >> n;
    getchar();
    for (int i=0; i<n; i++) {
        int res = 0;
        string s;
        cin >> s;
        cout << "Case #" << i+1 << ": " << count(s) << endl;
     }
  return 0;
}
