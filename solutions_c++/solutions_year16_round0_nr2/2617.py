#include <iostream>
#include <string>

using namespace std;

int main () {
  int testc;
  cin >> testc;
  
  for (int t = 1; t <= testc; t++) {
    string stack;
    cin >> stack;
    
    string sstack = "";
    for (int i = 0; i < (int) stack.size(); i++) {
      if (i == 0 || stack[i] != stack[i - 1]) {
        sstack += stack[i];
      }
    }

    int ans = (int) sstack.size();
    if (sstack.back() == '+') {
      ans--;
    }
    
    cout << "Case #" << t << ": " << ans << endl;
  }
}
