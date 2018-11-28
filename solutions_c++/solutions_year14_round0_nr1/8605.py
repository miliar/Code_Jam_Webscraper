#include <iostream>
#include <string>
#include <sstream>

using namespace std;

int trickResult(int * firstRow, int * secondRow) {
    bool found = false;
    bool repeat = false;
    int result = 0;

    for(int i = 0; i < 4; i++) {
        for(int j = 0; j < 4; j++) {
            if(firstRow[i] == secondRow[j]) {
                if(!found) {
                    found = true;
                    result = firstRow[i];
                } else {
                    repeat = true;
                }
            }
        }
    }

    if(!found) {
        return -1;
    }

    if(found && !repeat) {
        return result;
    }

    if(found && repeat) {
        return -2;
    }

    return 0;
}

int main() {
    
    string line;
    int i =0;
    
    getline(cin,line);
    int numCases = 0;
    stringstream (line) >> numCases;
       
    for(int caseNum = 1; caseNum <= numCases; caseNum++) {
        int firstRow, secondRow;
        int row1Numbers[] = {1,2,3,4};
        int row2Numbers[] = {1,2,3,4};

        getline(cin,line);
        stringstream (line) >> firstRow;
        for(int i = 1; i <= 4; i++) {
            getline(cin,line);
            if(i == firstRow) {
                stringstream stream(line);
                for(int j = 0; j < 4; j++)
                    stream >> row1Numbers[j];
            }
        }
        
        getline(cin,line);
        stringstream (line) >> secondRow;
        for(int i = 1; i <= 4; i++) {
            getline(cin,line);
            if(i == secondRow) {
                stringstream stream(line);
                for(int j = 0; j < 4; j++)
                    stream >> row2Numbers[j];
            }
        }

        int result = trickResult(row1Numbers, row2Numbers);

        cout << "Case #" << caseNum << ": ";

        switch(result) {
            case -1: 
                cout << "Volunteer cheated!" << endl;
                break;
            case -2:
                cout << "Bad magician!" << endl;
                break;
            default:
                cout << result << endl;
                break;
        }
    }

    return 0;
}
