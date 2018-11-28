//
//  main.cpp
//  Bleatrix
//
//  Created by Grant Pollerd on 10/04/2016.
//  Copyright © 2016 Grant Pollerd. All rights reserved.
//

#include <sstream>
#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <vector>

using namespace std;  // since cin and cout are both in namespace std, this saves some text


void bleat(int num){
    
    if (num == 0){
        cout << "INSOMNIA" << endl;
        return;
    }
    long bigNum = 99999999999;
    long tempNum = num;
    
    stringstream ss;
    ss << num;
    string str = ss.str();
    vector<bool> found(10,false);
    int foundCount = 0;
    long foundIndex = -1;
    int count = 2;
    
    while(foundCount < 10 && tempNum < bigNum){
        for(string::iterator itr = str.begin(); itr < str.end(); itr++){
            if(*itr != '-' && *itr != '.'){
                foundIndex = ((long)*itr) - 48;
                if(!found[foundIndex]) {
                    found[foundIndex] = true;
                    foundCount++;
                    if (foundCount == 10){
                        cout << str << endl;
                        break;
                    }
                }
            }
        }
        tempNum = num * count;
        count++;
        stringstream ss1;
        ss1 << tempNum;
        str = ss1.str();
        if (tempNum > bigNum) {
            cout << "INSOMNIA" << endl;
        }
        
    }
    
}

int main() {
    int t, n;

    cin >> t;  // read t. cin knows that t is an int, so it reads it as such.

    for (int i = 1; i <= t; ++i) {
        cin >> n;  // read n and then m.
        cout << "Case #" << i << ": ";
        bleat(n);
        
    }
    return 0;
}












