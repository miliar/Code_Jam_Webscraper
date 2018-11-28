//
//  main.cpp
//
//  Google Code Jam 2k16 - Qualifying Round - Problem A
//
//  I regret everything seen here, but maybe I'll (re)learn some things.

#include <iostream>
#include <vector>
// #include <string>
// #include <cmath>

using namespace std;
typedef unsigned long long numtype;

int main(int argc, const char * argv[]) {
    int cases, current;
    numtype n, jr, onen;
    int q, f, digits[10];
    
    cin >> cases;
    for (current=1; current<=cases; ++current) {
        cout << "Case #" << current << ": ";
        cin >> n;
        
        if (n==0) {
            cout << "INSOMNIA" << endl;
            continue; // next case
        }
        
        // reset digits
        for (q=0; q<10; q++) {
            digits[q] = 0;
        }
        
        onen = n;
        f = 0;
        while (f == 0) {
            // scan current number for digits
            jr = n;
            while (jr) {
                f = jr % 10;
                jr = jr / 10; // notation?  integer div backslash gone?
                if (digits[f] == 0) digits[f] = 1;
            }
        
            // check if all digits found yet
            f = 1;
            for (q=0; q<10; q++) {
                f = f & digits[q];
                if (f == 0) break;
            }
            
            if (f == 1) {
                cout << n << endl;
                break; // done with case
            } else {
                n += onen;
                // thru to next n step
            }
        } // per n add
        
    } // per case
}

