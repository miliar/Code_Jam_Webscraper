#include <bits/stdc++.h>
using namespace std;

int main(){
  int n;
  n = 0;
  cin >> n;
  for (int i = 0; i < n; i++) {
    stringstream ss;
    string str;
    cin >> str;
    ss << str[0];
    for (int j = 1; j < str.size(); j++){
       if (str[j] >= ss.str()[0]) {
         string t = ss.str();
         ss.seekp(0);
         ss << str[j];
         ss << t;
       } else {
         ss << str[j];
       }
    }
    cout << "Case #" << i+1 << ": " << ss.str() << endl;
  }
}
