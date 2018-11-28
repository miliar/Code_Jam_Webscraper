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

    char pancakeString[MAX_PANCAKES + 1];
    fscanf_s(inputFile, "%s", pancakeString, (int)MAX_PANCAKES+1);
    //printf_s("The pancake string is %s\n", pancakeString);

    uint64_t currentPancakeCount = strlen(pancakeString);
    for (uint64_t i = 0; i < currentPancakeCount; i++) {
        pancakes[i] = (pancakeString[i] == '+');
    }

    uint64_t flipCount = 0;
    while (true) {
        bool allHappy = true;
        for (uint64_t i = 0; i < currentPancakeCount; i++) {
            allHappy = pancakes[i];
            if (!allHappy) {
                i = currentPancakeCount;
            }
        }
        if (allHappy) {
            printf_s("%I64u\n", flipCount);
            return;
        }

        // If the first pancake is happy flip all adjacant happy pancakes
        if (pancakes[0]) {
            uint64_t index = 0;
            while (pancakes[index] || index == currentPancakeCount) {
                pancakes[index] = false;
                index++;
            }
        }
        //Otherwise flip up to last unhappy one
        else {
            uint64_t endIndex = currentPancakeCount;
            while (pancakes[endIndex - 1]) {
                endIndex--;
            }

            bool tempStack[MAX_PANCAKES];
            for (uint64_t i = 0; i < endIndex; i++) {
                tempStack[endIndex - i - 1] = !(pancakes[i]);
            }
            for (uint64_t i = 0; i < endIndex; i++) {
                pancakes[i] = tempStack[i];
            }
        }
        flipCount++;
    }

}