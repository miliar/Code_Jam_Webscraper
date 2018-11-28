#include <iostream>
#include <fstream>
#include <string>

int processArray(char stack[], int length) {
    bool flag = true;
    int counter = 0;
    int lastPositive = length - 1;
    while (flag) {
        flag = false;
        for (int i = lastPositive; i >= 0; --i) {
            if (stack[i] == '-') {
                lastPositive = i;
                flag = true;
                break;
            }
        }
        if (flag) {
            ++counter;
            for (int j = lastPositive; j >= 0; --j) {
                if (stack[j] == '-') {
                    stack[j] = '+';
                } else if (stack[j] == '+') {
                    stack[j] = '-';
                }
            }
        }
    }
    return counter;
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
        outputFile << "Case #" << (i + 1) << ": " << processArray((char *)line.c_str(), line.size()) << std::endl;
    }
    outputFile.flush();
    outputFile.close();
}
