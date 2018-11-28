//
//  main.cpp
//  Last word
//
//  Created by Corey Woodfield on 4/15/16.
//  Copyright © 2016 Corey Woodfield. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main(int argc, const char * argv[]) {
    ifstream in;
    in.open(argv[1]);
    ofstream out;
    out.open(argv[2]);
    int tests;
    in >> tests;
    cout << in.get();
    for (int i = 0; i < tests; ++i) {
        vector<char> firstWord;
        char cChar = in.get();
        while (cChar != '\n' && cChar != EOF) {
            firstWord.push_back(cChar);
            cChar = in.get();
        }
        string lastWord("");
        lastWord += firstWord[0];
        for (int j = 1; j < firstWord.size(); ++j) {
            if (firstWord[j] >= lastWord[0]) {
                lastWord = firstWord[j] + lastWord;
            } else {
                lastWord += firstWord[j];
            }
        }
        out << "Case #" << i + 1 << ": " << lastWord << endl;
    }
    return 0;
}
