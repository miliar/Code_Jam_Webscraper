//
//  main.cpp
//  Revenge of the Pancakes
//
//  Created by Corey Woodfield on 4/9/16.
//  Copyright © 2016 Corey Woodfield. All rights reserved.
//

#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, const char * argv[]) {
    ifstream in;
    in.open(argv[1]);
    int tests;
    in >> tests;
    ofstream out;
    out.open(argv[2]);
    for (int i = 0; i < tests; ++i) {
        string pancakes;
        bool plusToMinus = false;
        int switches = 0;
        in >> pancakes;
        char lastPancake = pancakes[0];
        for (int j = 1; j < pancakes.length(); ++j) {
            if (lastPancake != pancakes[j]) {
                if (lastPancake == '+') plusToMinus = true;
                ++switches;
            }
            lastPancake = pancakes[j];
        }
        if (lastPancake != '+') {
            ++switches;
        }
        out << "Case #" << (i + 1) << ": " << switches;
        if (i != tests - 1) out << endl;
    }
    return 0;
}
