#include <iostream>
#include <vector>
#include <sstream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
#include <cstdlib>
using namespace std;


template<typename T>
string to_string(const T& t) {
    ostringstream os;
    os << t;
    return os.str();
}

int main() {
    // Initialization and Input

    ifstream inFile;

    inFile.open("C:\\Users\\Junaid\\Documents\\Assignment_1\\Assignment1-InputsOutputs\\input\\40.in");

    int cases;
	inFile >> cases;
    int x;
    vector< vector<int> > firstRow;
    vector< vector<int> > secondRow;
    vector<int> firstAnswers;
    vector<int> secondAnswers;
    vector<int> tempvector;
    for (int i = 0; i < cases; i++) {
        inFile >> x;
        firstAnswers.push_back(x);
        for (int j = 0; j < 16; j++) {
            inFile >> x;
            tempvector.push_back(x);
        }
        firstRow.push_back(tempvector);
        tempvector = {};
        inFile >> x;
        secondAnswers.push_back(x);
        for (int j = 0; j < 16; j++) {
            inFile >> x;
            tempvector.push_back(x);
        }
        secondRow.push_back(tempvector);
        tempvector = {};
    }

    string ans;
    int count;
    int start;
    int end;
    int flag = 0;
    vector<int> a;
    vector<int> b;
    for (int i = 0; i < cases; i++) {
        if (firstAnswers[i] == 1) {
            start = 0;
            end = 4;
        } else if (firstAnswers[i] == 2) {
            start = 4;
            end = 8;
        } else if (firstAnswers[i] == 3) {
            start = 8;
            end = 12;
        } else if (firstAnswers[i] == 4) {
            start = 12;
            end = 16;
        }

        for (int j = start; j < end; j++) {
            a.push_back(firstRow[i][j]);
        }


        if (secondAnswers[i] == 1) {
            start = 0;
            end = 4;
        } else if (secondAnswers[i] == 2) {
            start = 4;
            end = 8;
        } else if (secondAnswers[i] == 3) {
            start = 8;
            end = 12;
        } else if (secondAnswers[i] == 4) {
            start = 12;
            end = 16;
        }

        for (int j = start; j < end; j++) {
            b.push_back(secondRow[i][j]);
        }

        flag = 0;
        count = 0;
        for (int p = 0; p < 4; p++) {
            for (int q = 0; q < 4; q++) {
                if (a[p] == b[q] && count > 0) {
                    count++;
                    flag = 1;
                    ans = "Case #" + to_string(i+1) + ": Bad magician!";
                    break;
                } else if (a[p] == b[q] && count == 0) {
                    count++;
                    flag = 1;
                    ans = "Case #" + to_string(i+1) + ": " + to_string(b[q]);
                } else if (flag == 0) {
                    ans = "Case #" + to_string(i+1) + ": Volunteer cheated!";
                }
            }
        }
        cout << ans << endl;
        a = {}; b = {};
    }
    return 0;
}
