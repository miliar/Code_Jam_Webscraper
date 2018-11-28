//
//  main.cpp
//  GCJ_1
//
//  Created by Sivasathivel Kandasamy on 2014-04-12.
//  Copyright (c) 2014 Sakthi K. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <string>
#define ROWS 4
#define COLS 4

using namespace std;

int main(int argc, const char * argv[])
{

    ifstream in_file("/Users/sivasathivelkandasamy/Projects/Tutorials/C++/Google Code Jam/Qualification Round/GCJ_1/input.in");
    int nCases;
    int first_row;
    int second_row;
    int first_deck[4][4];
    int second_deck[4][4];
    if (!in_file.is_open()) {
        cout<<"File Error"<<endl;
        return 1;
    }
    ofstream out_file("/Users/sivasathivelkandasamy/Projects/Tutorials/C++/Google Code Jam/Qualification Round/GCJ_1/result.out");
    
    
    in_file >> nCases;
    for (int c = 0; c < nCases; c++) {
        //Load Data into Matrices
        in_file>>first_row;
        for (int r = 0; r < ROWS; r++) {
            in_file>>first_deck[r][0];
            in_file>>first_deck[r][1];
            in_file>>first_deck[r][2];
            in_file>>first_deck[r][3];
        }
        
        in_file >> second_row;
        for (int r = 0; r < ROWS; r++) {
            in_file>>second_deck[r][0];
            in_file>>second_deck[r][1];
            in_file>>second_deck[r][2];
            in_file>>second_deck[r][3];
        }
        
        //Compare Rows to identify the Card...
        int CARD_FOUND = 0;
        int nCards = 0;
        int col = 0;
        for (int cf=0; cf < COLS; cf++) {
            for (int cs = 0; cs < COLS; cs++) {
                if (first_deck[first_row-1][cf] == second_deck[second_row-1][cs]) {
                    col = cf;
                    CARD_FOUND  = 1;
                    nCards++;
                }
            }
        }
        if (CARD_FOUND) {
            if (nCards == 1) {
                cout<<"Case #"<<c+1<<": "<<first_deck[first_row-1][col]<<endl;
                out_file<<"Case #"<<c+1<<": "<<first_deck[first_row-1][col]<<endl;
            }
            else {
                cout<<"Case #"<<c+1<<": "<<"Bad magician!"<<endl;
                out_file<<"Case #"<<c+1<<": "<<"Bad magician!"<<endl;
            }
        }
        else
        {
            cout<<"Case #"<<c+1<<": "<<"Volunteer cheated!"<<endl;
            out_file<<"Case #"<<c+1<<": "<<"Volunteer cheated!"<<endl;
        }
        
    }
    in_file.close();
    
    return 0;
}

