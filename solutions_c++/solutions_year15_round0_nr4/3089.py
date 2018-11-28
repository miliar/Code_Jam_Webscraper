//
//  Omino.cpp
//  Qualification-2015
//
//  Created by Ethan Kim on 4/11/15.
//  Copyright (c) 2015 Ethan Kim. All rights reserved.
//


#include <string>
#include <fstream>
#include <iostream>
#include <sstream>

using namespace std;

string getWinner(int size, int b, int c);

int main(int argc, const char * argv[]) {
    
    char* filename = (char*)argv[1];
    ifstream infile(filename);

    string line;
    int caseTotal = 0, lineNum = 0;
    while (getline(infile, line))
    {
        if (lineNum == 0) {
            caseTotal = stoi(line);
        } else {
            // check input line here
            
            istringstream iss(line);
            int x = 0, r = 0, c = 0;
            
            iss >> x >> r >> c;
            /*
            int x = stoi(line.substr(0,line.find_first_of(" ")));
            int r = stoi(line.substr(line.find_first_of(" ")+1));
            int c = stoi(line.substr(line.find_first_of(" ")+1));
             */
            cout << "Case #" << lineNum << ": " <<  getWinner(x, r, c) << endl;
        }
        lineNum++;
    }
    // check total line check here
    
    return 0;
}

string getWinner(int x, int r, int c) {
    
    if (x >= 7) {
        //cout << "hole : " << x << "," << r << "," << c <<  endl;
        return "RICHARD";
    } else if ((r*c) < x) {
        //cout << "small : " << x << "," << r << "," << c <<  endl;
        return "RICHARD";
    } else if (((r*c)% x) != 0) {
        //cout << "mod : " << x << "," << r << "," << c <<  endl;
        return "RICHARD";
    }
    
    // shorter length
    for (int s = 1; s <= (x+1)/2; s++) {
        //logner length
        for (int l = x - s + 1; (l >= s && l*s >= x ) ; l--){
            if (r < s || c < s ) {
                //cout << "length short: " << x << "," << r << "," << c <<  "(" << l <<  "," << s <<  ")" <<  endl;
                return "RICHARD";
            }
            if (r < l && c < l ) {
                //cout << "length long: " << x << "," << r << "," << c <<  "(" << l <<  "," << s <<  ")" <<  endl;
                return "RICHARD";
            }
        }

    }
    
    if (x >= 4 && (r < 3 || c < 3 )) {
        //cout << "special : " << x << "," << r << "," << c <<  endl;
        return "RICHARD";
    }
    
    //cout << "input : " << x << "," << r << "," << c <<  endl;
    return "GABRIEL";
}
