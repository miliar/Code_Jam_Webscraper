#include <cstdlib>
#include <iostream>
#include <string>

using namespace std;

int main() {
  string buffer;
  int lines;
  cin >> lines;
  for (int k=1; k<=lines; k++) {
    cin >> buffer;
    bool solved = false;
    int ops = 0;
    int index = buffer.length();
    while (!solved) {
      bool flip = false;
      solved = true;
      for(int i=index; i>=0; i--) {
        if(!flip) {
          if (buffer[i] == '-') {
            solved = false;
            flip = true;
            index = i;
            ++ops;
            buffer[i] = '+';
          }          
        } else {
          if (buffer[i] == '-') {
            buffer[i] = '+';
          } else {
            buffer[i] = '-';
          }
        }
      }
      if (index == 0) {
        solved = true;
      }
    }

    cout << "Case #" << k <<": " << ops <<endl;
  }
}
