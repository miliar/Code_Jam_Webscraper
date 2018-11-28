#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
using namespace std;

// this is not the flip defined in the problem. this simply flip + and - without changing the order
void flip(string& pancakes, int topI) {
    for (int i = 0; i < topI; i++) {
        if (pancakes[i] == '+') {
            pancakes[i] = '-';
        } else {
            pancakes[i] = '+';
        }
    }
}

// basic idea here is, things with consecutive -/+ are as hard as their dedup'ed version
// e.g. Opt(--+++++--++) <= Opt(-+-+)
// then we can prove Opt(--+++++--++) >= Opt(-+-+)
// so Opt(--+++++--++) == Opt(-+-+)
string dedup(string& initString) {
    int initSize = initString.length();
    if (initSize <= 1) {
        return initString;
    }

    string returnString(initString, 0, 1);

    for (int i = 1; i < initSize; i++) {
        if (initString[i] != initString[i - 1]) {
            returnString.push_back(initString[i]);
        }
    }

    return returnString;
}

// after dedup, we will always have strings like +-+-+-... or -+-+-+...
//
// comparing Opt(S0...Si) and Opt(S0...Si,Si+1):
// 1) it's obvious that if Si+1 == '+', Opt(S0...Si,Si+1/Si+1='+') = Opt(S0...Si)
// 2) if Si+1 == '-', and S0 == '+'
//      Opt(S0...Si,Si+1) = 1 + Opt(Flip(S0...Si),Si+1)
//      since Flip(S0) == Si+1, after dedup, Opt(Flip(S0...Si),Si+1) = Opt(S0...Si) where S0 is '-'
//  so Opt(S0...Si,Si+1/Si+1='-'/S0='+') = 1 + Opt(S0...Si/S0='-')
// 3) if Si+1 == '-', and S0 == '-'
//      by flipping S0-Si+1, we get case 1)
//  so Opt(S0...Si,Si+1/Si+1='-'/S0='-') = 1 + Opt(S0...Si/S0='+')
// 
// with these, we can form a recursion
int solveRecursion(string& deduped, int currentSize) {
    //cout << ">>>" << currentSize << ">>>>" << deduped << endl;
    if (currentSize == 0) {
        return 0;
    }
    if (currentSize == 1) {
        if (deduped[0] == '+') {
            return 0;
        } else {
            return 1;
        }
    }

    if (deduped[currentSize - 1] == '+') {
        //cout << "AA" << endl;
        return solveRecursion(deduped, currentSize - 1);
    } else {
        //cout << "BB" << endl;
        flip(deduped, currentSize - 1);
        return 1 + solveRecursion(deduped, currentSize - 1);
    }
}

int optimalFlip(string& pancakeStack) {
    string deduped = dedup(pancakeStack);
    return solveRecursion(deduped, deduped.length());
}


int main() {
    string fileName = "data1";
    string outputFileName = "result1";
    string line;

    ifstream dataFile;
    dataFile.open(fileName);

    // read # of test cases
    getline(dataFile, line);
    int numTests = stoi(line);

    // read all test inputs
    vector<string> testInputs(numTests);
    for (int i = 0; i < numTests; i++) {
        getline(dataFile, line);
        testInputs[i] = line;
    }
    dataFile.close();

    // print test inputs
    ofstream resultFile;
    resultFile.open(outputFileName, ofstream::out | ofstream::trunc);
    for (int i = 0; i < numTests; i++) {
        cout << "||" << testInputs[i] << "||" << endl;
        int result = optimalFlip(testInputs[i]);
        cout << "Case #" << i + 1 << ": " << result << endl; 
        resultFile << "Case #" << i + 1 << ": " << result << endl;
    }
    resultFile.close();

    return 0;
}
