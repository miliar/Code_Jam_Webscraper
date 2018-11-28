#include <cstdio>
#include <cstdint>
#include <cmath>
#include <algorithm>
#include <array>

void SolveCase(FILE*, uint64_t);

int main(int argc, char** argv) {
    if (argc != 2) {
        printf("No filename entered.\n");
        return -1;
    }

    FILE * inputFile = nullptr;
    fopen_s(&inputFile, argv[1], "r");
    if (inputFile == NULL) {
        printf("Unable to open file %s.\n", argv[1]);
        return -1;
    }

    uint64_t numOfTestCases = 0;
    fscanf_s(inputFile, "%I64u", &numOfTestCases);
    //printf_s("There are %I64u Test Cases.\n", numOfTestCases);

    for (uint64_t i = 0; i < numOfTestCases; i++) {
        SolveCase(inputFile, i + 1);
    }

    fclose(inputFile);
}

bool digits[10];

void SolveCase(FILE* inputFile, uint64_t index) {
    printf("Case #%I64u: ", index);

    uint64_t startNum = 0;
    fscanf_s(inputFile, "%I64u", &startNum);
    //printf_s("The start number is %I64u.\n", startNum);

    if (startNum == 0) {
        printf_s("INSOMNIA\n");
        return;
    }

    for (uint64_t i = 0; i < 10; i++) {
        digits[i] = false;
    }

    uint64_t currentValue = startNum;
    uint64_t tempValue = currentValue;
    while (true) {
        tempValue = currentValue;
        while (tempValue != 0) {
            digits[tempValue % 10] = true;
            tempValue = tempValue / 10;
        }

        bool allDigitsFound = true;
        for (uint64_t i = 0; i < 10; i++) {
            if (digits[i] == false) {
                allDigitsFound = false;
                i = 10;
            }
        }

        if (allDigitsFound) {
            printf_s("%I64u\n", currentValue);
            return;
        }

        currentValue += startNum;
    }
}