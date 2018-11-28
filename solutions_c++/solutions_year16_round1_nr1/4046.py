#include<iostream>
#include<string>
using namespace std;

int main() {
  int t;
  cin >> t;
  for (int i = 1 ; i <= t; i++) {
    string s;
    cin >> s;
    string res(1, s[0]);
    for (int j = 1; j < s.length(); j++) {
      if (res[0] > s[j]) {
        res = res + s[j];
      } else {
        string temp(1, s[j]);
        res = temp.append(res);
      }   
    }   
    cout << "Case #" << i << ": " << res << endl;
  }
  return 0;
}

