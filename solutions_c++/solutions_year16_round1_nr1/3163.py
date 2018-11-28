//
//  main.cpp
//
//  Google Code Jam 2k16 - Round 1A - Problem A
//
//  I regret everything seen here, but maybe I'll (re)learn some things.

#include <iostream>
#include <vector>
#include <string>
// #include <cmath>

using namespace std;

string tin, tout;

int main(int argc, const char * argv[]) {
    int cases, current;
    
    
    cin >> cases;
    for (current=1; current<=cases; ++current) {
        cout << "Case #" << current << ": ";
        
        cin >> tin;
        
        tout = tin[0];
        
        for (int q=1; q<tin.length(); q++) {
            char c = tin[q];
            if (c < tout[0]) {
                tout.append(1, c);
            } else {
                tout.insert(0, 1, c);
            }
        }
        cout << tout;
        
        cout << endl;
    }
}

