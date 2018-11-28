#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>

using namespace std;

typedef unsigned int uint;

struct Test {
    uint rowBegin, rowEnd, gridBegin[4][4], gridEnd[4][4];
};

void GetGrid(ifstream * file, uint (&grid)[4][4]) {
    string line;

    for (uint column = 0; column < 4; ++column) {
        getline(*file, line);

        uint start = 0, end = line.find(' ');

        for (uint row = 0; row < 4; ++row) {
            if (end != string::npos) {
                stringstream(line.substr(start, end - start)) >> grid[column][row];
                start = end + 1, end = line.find(' ', start);
            } else if (row == 3) {
                stringstream(line.substr(start, end)) >> grid[column][row];
            }
        }
    }
}

int main(int argc, char * argv[]) {
    if (argc < 2) {
        return 0;
    }

    ifstream fileInput(argv[1]);

    string name = argv[1]; name = name.substr(0, name.length() - 3); name.append(".out");
    ofstream fileOutput(name);

    if (!fileInput.is_open() || !fileOutput.is_open()) { return 2; }
    
    fileOutput.clear();

    string line;
    uint tests = 0;
    getline(fileInput, line); stringstream(line) >> tests;

    vector<Test> cases(tests);

    for (vector<Test>::iterator currentCase = cases.begin(); currentCase != cases.end(); ++currentCase) {
        getline(fileInput, line); stringstream(line) >> currentCase->rowBegin;
        GetGrid(&fileInput, currentCase->gridBegin);


        getline(fileInput, line); stringstream(line) >> currentCase->rowEnd;
        GetGrid(&fileInput, currentCase->gridEnd);
    }

    uint caseNumber = 0;

    for (vector<Test>::iterator currentCase = cases.begin(); currentCase != cases.end(); ++currentCase, ++caseNumber) {
        uint card = 0;

        uint * begin = currentCase->gridBegin[currentCase->rowBegin - 1];
        uint * end = currentCase->gridEnd[currentCase->rowEnd - 1];

        bool bad = false;

        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                if (begin[i] == end[j]) {
                    if (card == 0) {
                        card = begin[i];
                    } else {
                        bad = true;
                        break;
                    }
                }
            }

            if (bad) { break; }
        }

        fileOutput << "Case #" << (caseNumber + 1) << ": ";

        if (bad) {
            fileOutput << "Bad magician!" << endl;
        } else if (card != 0) {
            fileOutput << card << endl;
        } else {
            fileOutput << "Volunteer cheated!" << endl;
        }
    }

    return 0;
}