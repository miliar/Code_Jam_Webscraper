#include <iostream>
#include <fstream>
#include <string>

std::string getLastWord(std::string orgWord) {
    std::string lastWord;
    int size = orgWord.size();
    lastWord += orgWord.at(0);
    for (int i = 1; i < size; ++i) {
        if (orgWord.at(i) >= lastWord.at(0)) {
            lastWord = (orgWord.at(i) + lastWord);
        } else {
            lastWord += orgWord.at(i);
        }
    }
    return lastWord;
}

void main() {
    std::string line;
    int caseNumber = 0;
    std::ifstream inputFile;
    std::ofstream outputFile;
    inputFile.open("input.txt");
    outputFile.open("output.txt");
    inputFile >> caseNumber;
    std::getline(inputFile, line);
    for (int i = 0; i < caseNumber; ++i) {
        std::getline(inputFile, line);
        outputFile << "Case #" << (i + 1) << ": " << getLastWord(line) << std::endl;
    }
    inputFile.close();
    outputFile.flush();
    outputFile.close();
}
