//
//  main.cpp
//  B
//
//  Created by Jonas Blåsås Lønnum on 09.04.2016.
//  Copyright © 2016 blasas. All rights reserved.
//

#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;

string flip(string s) {
    string flipped = "";
    
    for(int i = 0; i < s.size(); i++) {
        string c(1, s[i]);
        if(c == "-") {
            flipped = flipped + "+";
        } else {
            flipped = flipped + "-";
        }
    }
    
    return flipped;
}

bool isAllHappy(string s) {
    bool allHappy = true;
    
    for(int j = 0; j < s.size(); j++) {
        string c(1, s[j]);
        if(c == "-") {
            allHappy = false;
            break;
        }
    }
    
    return allHappy;
}

bool isAllBlank(string s) {
    bool allBlank = true;
    
    for(int j = 0; j < s.size(); j++) {
        string c(1, s[j]);
        if(c == "+") {
            allBlank = false;
            break;
        }
    }
    
    //cout << endl << endl << "isAllBlank? <-> " << s << endl << endl;
    
    return allBlank;
}

int main(int argc, const char * argv[]) {
    
    FILE *fin = freopen("/Users/Jonas/Documents/Development/C++/CodeJam/QualRound2016/B/B/B-large.in", "r", stdin);
    assert( fin!=NULL );
    FILE *fout = freopen("/Users/Jonas/Documents/Development/C++/CodeJam/QualRound2016/B/B/B-large.out", "w", stdout);
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++){
        cout << "Case #" << t << ": ";
        
        string pancakes = "";
        cin >> pancakes;
        string res = flip(pancakes);
        string copyOfPancakes = pancakes;
        
        int numberOfFlips = 0;
        
        // do flipping stuff
        if(!isAllHappy(pancakes)) {
            if(isAllBlank(pancakes)) {
                numberOfFlips = 1;
            } else {
                for(int i = 0; i < (copyOfPancakes.size()-1) && !isAllHappy(copyOfPancakes); i++) {
                    string thisOne(1, copyOfPancakes[i]);
                    string nextOne(1, copyOfPancakes[i+1]);
                    if(thisOne != nextOne) {
                        string flipString((i+1), copyOfPancakes[0]);
                        flipString = flip(flipString);
                        numberOfFlips++;
                        int length = (int)copyOfPancakes.size() - (i+1);
                        int index = (i+1);
                        string whatsLeft = copyOfPancakes.substr(index, (index+length)-1);
                        copyOfPancakes = flipString + whatsLeft;
                    }
                    if(isAllBlank(copyOfPancakes)) {
                        copyOfPancakes = flip(copyOfPancakes);
                        numberOfFlips++;
                    }
                }
            }
        }
        
        cout << numberOfFlips << endl;
        
    }
    //cout << "FINISH!" << endl;
    return 0;
}