#include <iostream>

using namespace std;


int main(){
  int T;
  string s;
  cin >> T;
  for (int t=0; t<T ; t++) {
    cin >> s;
    string n; n += s[0];
    for (int i=1; i<s.length() ; i++){
      if (s[i] >= n[0]) {
        n = s[i] + n;
      } else {
        n = n + s[i];
      }
    }
    cout << "Case #" << t+1 << ": " << n << endl;
  }
}
