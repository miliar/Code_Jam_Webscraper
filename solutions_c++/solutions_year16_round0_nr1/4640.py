//
//  main.cpp
//  Counting Sheep
//
//  Created by Corey Woodfield on 4/8/16.
//  Copyright © 2016 Corey Woodfield. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <map>

using namespace std;

int main(int argc, const char * argv[]) {
    ifstream in;
    in.open(argv[1]);
    int tests;
    in >> tests;
    ofstream out;
    out.open(argv[2]);
    for (int i = 0; i < tests; ++i) {
        map<char,int> digits = {{'0',0},{'1',1},{'2',2},{'3',3},{'4',4},{'5',5},{'6',6},{'7',7},{'8',8},{'9',9}};
        int n;
        in >> n;
        if (n == 0) {
            out << "Case #" << (i + 1) << ": INSOMNIA";
        } else {
            int counter = 1;
            int answer = 0;
            while (digits.size()) {
                string nStr = to_string(n * counter);
                for (int j = 0; j < nStr.length(); ++j) {
                    if (digits.count(nStr[j])) {
                        digits.erase(nStr[j]);
                        if (digits.size() == 0) {
                            break;
                        }
                    }
                }
                answer = n * counter;
                ++counter;
            }
            out << "Case #" << (i + 1) << ": " << answer;
        }
        if (i != tests - 1) {
            out << endl;
        }
    }
    return 0;
}
