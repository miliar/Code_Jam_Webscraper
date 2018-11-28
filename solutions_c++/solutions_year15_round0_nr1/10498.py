#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int solveCase(string testCase) {
    int invitesNeeded = 0;
    int standing = 0;
    int requiredToStand = 0;
    int row = 2;
    while (row < testCase.length()) {
        // Solve invites needed for the row
        int requiredToStand = row - 2;
        int invite = requiredToStand - standing;
        invite = invite <= 0 ? 0 : invite;
        invitesNeeded += invite;
        
        // Update standing
        standing += testCase.at(row) - '0' + invite;
        
        row++;
    }
    return invitesNeeded;
}

int main(int argc, char *argv[]) {
    string inputFileName;
    string outputFileName;

    // Read cli arguments;
    if (argc == 2) {
        inputFileName = string(argv[1]) + ".in";
        outputFileName = string(argv[1]) + ".out";
    } else {
        std::cerr << "Usage: " << argv[0] << " input" << std::endl;
        return 1;
    }

    // Open input & output files
    ifstream inputFile;
    ofstream outputFile;
    inputFile.open(inputFileName);
    if (!inputFile.is_open()) {
        std::cerr << "Could not open file" << inputFileName << std::endl;
        return 1;
    }
    outputFile.open(outputFileName);
    if (!outputFile.is_open()) {
        std::cerr << "Could not open file" << outputFileName << std::endl;
        return 1;
    }

    // Solve
    string line;
    getline(inputFile, line);
    int i = 1;
    while (getline(inputFile, line)) {
        outputFile << "Case #" << i++ << ": " << solveCase(line) << "\n";
    }

    // Cleanup
    inputFile.close();
    outputFile.close();

    return 0;
}
