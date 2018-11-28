//
//  main.cpp
//
//  Google Code Jam 2k16 - Qualifying Round - Problem D
//
//  I regret everything seen here, but maybe I'll (re)learn some things.

#include <iostream>
#include <vector>
// #include <string>
// #include <cmath>

using namespace std;

typedef unsigned long long numtype;

// self-relegating to worst solution every time, only good for small solution set
// because need food

// range of pow function?  promote to double long or just rewrite?

// lolz rewroted
numtype bapow(numtype base, numtype exponent) {
    numtype accum = 1;
    while (exponent) {
        accum *= base;
        exponent--;
    }
    
    return accum;
}

int main(int argc, const char * argv[]) {
    int cases, current;
    
    int k, c, s;
    
    cin >> cases;
    for (current=1; current<=cases; ++current) {
        cout << "Case #" << current << ": ";
        
        cin >> k >> c >> s;
        
        numtype step = (bapow(k, c) - 1);
        if (k-1) step /= (k-1);

        cout << 1;
        numtype b = 1 + step;
        
        for (int q=1; q<s; q++) {
            cout << " " << b;
            b += step;
        }
        
        cout << endl;
    }
}

