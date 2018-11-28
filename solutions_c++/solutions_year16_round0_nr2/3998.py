#include <iostream>
#include <string>
#include <vector>

using namespace std;

enum State { smile, blank, startblank };

int main() {
    int T;
    cin >> T;
    for(int i = 1; i <= T; i++) {
        string pancakes;
        cin >> pancakes;
        int flips = 0;
        State s = smile;
        if(pancakes[0] == '-') {
            s = startblank;
        }

        for(int j = 1; j < pancakes.size(); j++) {
           if(pancakes[j] == '+') {
              if(s == blank) {
                  flips += 2;
              }
              else if(s == startblank) {
                  flips +=1;
              }
              s = smile;
           }
           else if(s == smile) {
                   s = blank;
           }
                  
        }
        if(pancakes.back() == '-') {
            if(s == startblank) {
            flips += 1;
            }
            else {
                flips += 2;
            }
        }
        cout << "Case #" << i << ": " << flips << endl;
    }
}
