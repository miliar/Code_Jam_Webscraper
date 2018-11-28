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

const uint64_t MAX_PANCAKES = 100;
bool pancakes[MAX_PANCAKES];

void SolveCase(FILE* inputFile, uint64_t index) {
    printf("Case #%I64u: ", index);

    char inputString[2002];
    fscanf_s(inputFile, "%s", inputString, 2001);

    //printf_s("The input string is: %s\n", inputString);

    uint64_t letterCount[26];
    for (uint64_t i = 0; i < 26; i++) {
        letterCount[i] = 0;
    }

    uint64_t stringLength = strlen(inputString);
    for (uint64_t i = 0; i < stringLength; i++) {
        letterCount[ inputString[i] - 'A' ]++;
    }

    uint64_t resultCount[10];
    for (uint64_t i = 0; i < 10; i++) {
        resultCount[i] = 0;
    }

    while (letterCount['Z' - 'A'] != 0) {
        resultCount[0]++;
        letterCount['Z' - 'A']--;
        letterCount['E' - 'A']--;
        letterCount['R' - 'A']--;
        letterCount['O' - 'A']--;
    }

    while (letterCount['W' - 'A'] != 0) {
        resultCount[2]++;
        letterCount['T' - 'A']--;
        letterCount['W' - 'A']--;
        letterCount['O' - 'A']--;
    }

    while (letterCount['U' - 'A'] != 0) {
        resultCount[4]++;
        letterCount['F' - 'A']--;
        letterCount['O' - 'A']--;
        letterCount['U' - 'A']--;
        letterCount['R' - 'A']--;
    }

    while (letterCount['F' - 'A'] != 0) {
        resultCount[5]++;
        letterCount['F' - 'A']--;
        letterCount['I' - 'A']--;
        letterCount['V' - 'A']--;
        letterCount['E' - 'A']--;
    }

    while (letterCount['X' - 'A'] != 0) {
        resultCount[6]++;
        letterCount['S' - 'A']--;
        letterCount['I' - 'A']--;
        letterCount['X' - 'A']--;
    }

    while (letterCount['V' - 'A'] != 0) {
        resultCount[7]++;
        letterCount['S' - 'A']--;
        letterCount['E' - 'A']--;
        letterCount['V' - 'A']--;
        letterCount['E' - 'A']--;
        letterCount['N' - 'A']--;
    }

    while (letterCount['G' - 'A'] != 0) {
        resultCount[8]++;
        letterCount['E' - 'A']--;
        letterCount['I' - 'A']--;
        letterCount['G' - 'A']--;
        letterCount['H' - 'A']--;
        letterCount['T' - 'A']--;
    }

    resultCount[1] = letterCount['O' - 'A'];
    resultCount[3] = letterCount['R' - 'A'];
    resultCount[9] = letterCount['I' - 'A'];

    for (uint64_t i = 0; i < 10; i++) {
        while (resultCount[i] != 0) {
            printf_s("%I64u", i);
            resultCount[i]--;
        }
    }
    printf_s("\n");
}