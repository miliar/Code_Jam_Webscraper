#include <algorithm>
#include <iostream>
#include <string>
#include <set>
using namespace std;

int main() {

    int cases;
    cin >> cases;

    for( int i = 0; i < cases; i++) {
        string pancakes;
        cin >> pancakes;
        int flips = 0;

        while(1) {
            for (int i = 0; i < pancakes.size(); i++) {
                if(pancakes[i+1] != '-' && pancakes[i] == '-') {
                    flips++;
                    for ( int j = 0; j < (i + 1); j++) {
                        if(pancakes[j] == '-') {
                            pancakes[j] = '+';
                        }
                        else if(pancakes[j] == '+') {
                            pancakes[j] = '-';
                        }
                    }
                }
            }

            int b = 0;
            for (auto i : pancakes) {
                if (i == '-') {
                    b = 1;
                }

            }
            if (b == 0) {
                break;
            }
        }
        cout << "Case #" << i+1 << ": "<<flips <<endl;

    }


}

