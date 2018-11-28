#include <iostream>
#include <fstream>

void parseNumber(long long number, int *flag) {
    while (number) {
        int digit = number % 10;
        number = number / 10;
        switch (digit) {
        case 0:
            (*flag) = ((*flag) & 0x0FFE);
            break;
        case 1:
            (*flag) = ((*flag) & 0x0FFD);
            break;
        case 2:
            (*flag) = ((*flag) & 0x0FFB);
            break;
        case 3:
            (*flag) = ((*flag) & 0x0FF7);
            break;
        case 4:
            (*flag) = ((*flag) & 0x0FEF);
            break;
        case 5:
            (*flag) = ((*flag) & 0x0FDF);
            break;
        case 6:
            (*flag) = ((*flag) & 0x0FBF);
            break;
        case 7:
            (*flag) = ((*flag) & 0x0F7F);
            break;
        case 8:
            (*flag) = ((*flag) & 0x02FF);
            break;
        case 9:
            (*flag) = ((*flag) & 0x01FF);
            break;
        }
    }
}

void main() {
    int caseNumber = 0;
    std::ifstream inputFile;
    std::ofstream outputFile;
    inputFile.open("input.txt");
    outputFile.open("output.txt");
    inputFile >> caseNumber;
    for (int i = 0; i < caseNumber; ++i) {
        long startNumber = 0;
        inputFile >> startNumber;
        if (startNumber == 0) {
            outputFile << "Case #" << (i + 1) << ": INSOMNIA" << std::endl;
        } else {
            int counter = 1;
            int flag = 0x03FF;
            long long resultNumber = counter * startNumber;
            while (flag) {
                parseNumber(resultNumber, &flag);
                if (flag) {
                    resultNumber = (++counter) * startNumber;
                }
            }
            outputFile << "Case #" << (i + 1) << ": " << resultNumber << std::endl;
        }
    }
    outputFile.flush();
    outputFile.close();
}
