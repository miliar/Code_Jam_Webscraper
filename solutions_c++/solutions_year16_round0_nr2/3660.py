//
//  main.cpp
//
//  Google Code Jam 2k16 - Qualifying Round - Problem B
//
//  I regret everything seen here, but maybe I'll (re)learn some things.

#include <iostream>
#include <vector>
#include <string>
// #include <cmath>

using namespace std;

int main(int argc, const char * argv[]) {
    int cases, current;
    
    int cursor, polarity, cp, flips;
    string pile;
    
    
    cin >> cases;
    for (current=1; current<=cases; ++current) {
        cout << "Case #" << current << ": ";
        flips = 0;
        cin >> pile;
        
        // trusting nonzero pile size
        if (pile[pile.length()-1] == '+') {
            polarity = 1;
        } else {
            polarity = 0;
        }
        
        for (cursor = (int)pile.length()-1; cursor >= 0; cursor--) { // end null included in length
            cp = (pile[cursor] == '+')? 1 : 0;
            if (polarity == 0 && cp == 1) flips += 2;
            polarity = cp;
        }
        if (polarity == 0) flips++;
        
        cout << flips << endl;
    }
}

