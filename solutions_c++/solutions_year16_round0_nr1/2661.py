// basic file operations
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

void cancelDigits(int input, vector<bool>& allDigits) {
    while (input != 0) {
        int digit = input % 10;
        input = input / 10;
        allDigits[digit] = true;
    }
}

double countSheep(int input) {
    if (input == 0) {
        return -1;
    }

    bool allDigitsInit[10] = {false, false, false, false, false, false, false, false, false, false};
    vector<bool> allDigits (10);
    allDigits.assign(allDigitsInit, allDigitsInit + 10);

    // remove 0's
    int zeroCount = 0;
    while (input % 10 == 0) {
        zeroCount += 1;
        input = input / 10;
    }
    if (zeroCount != 0) {
        allDigits[0] = true;
    }

    double current = input;
    while (true) {
        // cancel the digits
       cancelDigits(current, allDigits);
       int numCanceled = 0;
       for (int i = 0; i < 10; i++) {
            if (allDigits[i]) numCanceled += 1;
       }
       //cout << current << "--" << numCanceled << endl;
       if (numCanceled == 10) {
            break;
       }
       current += input;
    }

    //cout << "+++" << current << endl;
    for (int i = 0; i < zeroCount; i++) {
        current = current * 10;
    }
    return current;
}



int main () {
    string fileName = "data1";
    string outputFileName = "result1";
    string line;

    ifstream dataFile("thefile.txt");
    dataFile.open(fileName);

    // read # of test cases
    getline(dataFile, line);
    int numTests = stoi(line);

    // read all test inputs
    vector<int> testInputs(numTests);
    for (int i = 0; i < numTests; i++) {
        getline(dataFile, line);
        testInputs[i] = stoi(line);
    }
    dataFile.close();

    // print test inputs
    ofstream resultFile;
    resultFile.open(outputFileName, ofstream::out | ofstream::trunc);
    for (int i = 0; i < numTests; i++) {
        cout << "||" << testInputs[i] << "||" << endl;
        int result = countSheep(testInputs[i]);
        if (result == -1) {
            resultFile << "Case #" << i + 1 << ": " << "INSOMNIA" << endl;
            cout << "Case #" << i + 1 << ": " << "INSOMNIA" << endl; 
        } else {
            resultFile << "Case #" << i + 1 << ": " << result << endl;
            cout << "Case #" << i + 1 << ": " << result << endl;
        }
    }
    resultFile.close();

    return 0;
}



