//============================================================================
// Name        : Magic.cpp
// Author      : fff
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <iostream>
#include <fstream>
#include <string>
#include <cstdio>
#include <vector>
using namespace std;

void handleOneRound(ifstream& myfile, vector<int>& first) {
    size_t givenRow = 0;
    myfile >> givenRow;
    size_t consume = givenRow - 1;
    int meal = 0;
    for (size_t j = 0; j < consume; j++) {
        for (size_t k = 0; k < 4; k++) {
            myfile >> meal;
        }
    }
    int rowNumber = 0;
    for (size_t k = 0; k < 4; k++) {
        myfile >> rowNumber;
        first.push_back(rowNumber);
    }

    size_t rowsToSkip = 4 - givenRow;

    for (size_t k = 0; k < rowsToSkip; k++) {
        for (size_t k = 0; k < 4; k++) {
            myfile >> meal;
        }
    }

}

int main() {
    string line;

    ifstream myfile("input.txt");
    if (myfile.is_open() == false) {
        cout << "Unable to open file";
        return 0;
    } else {

        size_t numberOfTests = 0;
        myfile >> numberOfTests;

        for (size_t i = 0; i < numberOfTests; i++) {

            vector<int> first;
            handleOneRound(myfile, first);

            vector<int> second;
            handleOneRound(myfile, second);

            size_t count = 0;
            int match = 0;
            for (size_t f = 0; f < 4; f++) {
                for ( size_t j = 0; j < 4; j++ ) {
                    if ( first.at(f) == second.at(j) ) {
                        match  = first.at(f);
                        count++;
                    }
                }
            }

            if ( count == 1 ) {
                cout << "Case #" << i + 1 << ": " << match << endl;
            } else if ( count == 0 ) {
                cout << "Case #" << i + 1 << ": " << "Volunteer cheated!"<< endl;
            } else {
                cout << "Case #" << i + 1 << ": " << "Bad magician!"<< endl;
            }


        }
        myfile.close();
    }

    char a = 'a';
    cin >> a;

}

