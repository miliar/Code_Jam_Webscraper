//
//  main.cpp
//  CodeJam
//
//  Created by Ben Forsyth on 3/31/14.
//  Copyright (c) 2014 Ben Forsyth. All rights reserved.
//

#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <assert.h>

using namespace std;



bool readIntFromLine(ifstream& fStream, int& intValue) {
    string   line;
    if (!getline(fStream, line))
        return false;
    
    stringstream lineStream(line);
    lineStream >> intValue;
    return true;
}

bool readVectorFromLine(ifstream& fStream, vector<int>& intVector) {
    string line;
    if (!getline(fStream, line)) {
        assert(false);
        return false;
    }

    int card;
    stringstream lineStream(line);
    while(lineStream >> card)
    {
        intVector.push_back(card);
    }
    
    return true;
}

struct arrangment {
    vector<int> row;
};

void compareRows(const vector<int>&row1, const vector<int>& row2) {
    vector<int> matches;
    for(int i = 0; i < row1.size(); i++) {
        const int cardNumber = row1.at(i);
        for(int j = 0; j < row2.size(); j++) {
            if (row2.at(j) == cardNumber)
                matches.push_back(cardNumber);
        }
    }
    
    if (matches.size() == 0)
        cout << "Volunteer cheated!";
    else if (matches.size() > 1)
        cout << "Bad magician!";
    else
        cout << matches.front();
}

int main(int argc, const char * argv[])
{
    if (argc < 2) {
        cout << "missing path to input file" << endl;
        exit(-1);
    }
    
    ifstream file(argv[1]);
    string   line;

    int totalCases;
    if(getline(file, line))
        totalCases = atoi(line.c_str());
    
    assert(totalCases != 0);

    for (int i = 0; i < totalCases; i++)
    {
        
        int answer1;
        readIntFromLine(file, answer1);
        
        vector<arrangment> first;
        for (int i = 0; i < 4; i++) {
            arrangment cards;
            readVectorFromLine(file, cards.row);
            first.push_back(cards);
        }
        
        int answer2;
        readIntFromLine(file, answer2);
        
        vector<arrangment> second;
        for (int i = 0; i < 4; i++) {
            arrangment cards;
            readVectorFromLine(file, cards.row);
            second.push_back(cards);
        }
        
        cout << "Case #" << i + 1 << ": ";
        compareRows(first.at(answer1 - 1).row, second.at(answer2 - 1).row);
        cout << endl;
    }
    
    file.close();
    
    return 0;
}

