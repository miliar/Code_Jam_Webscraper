#include <cstdio>
#include <cstdint>
#include <cmath>
#include <algorithm>
#include <array>

char binaryString[16];

void writeBinaryNumber(uint64_t num) {
    uint64_t i = 0;
    while (num != 0) {
        if (num % 2 == 0) {
            binaryString[16-i-1] = '0';
        }
        else {
            binaryString[16-i-1] = '1';
        }
        num = num >> 1;
        i++;
    }
}

uint64_t getBaseFromBinary(uint64_t base) {
    uint64_t total = 0;
    uint64_t addValue = 1;
    for (uint64_t i = 0; i < 16; i++) {
        if (binaryString[16-i-1] == '0') {
            addValue *= base;
            continue;
        }

        total += addValue;
        addValue *= base;
    }
    return total;
}

void WriteResult(uint64_t num) {
    printf_s("%s ", binaryString);
    for (uint64_t i = 2; i < 11; i++) {
        uint64_t result = getBaseFromBinary(i);
        //printf("%I64u ", result);
        if (result % 2 == 0) {
            printf("2 ");
        }
        else if (result % 3 == 0) {
            printf("3 ");
        }
        else if (result % 5 == 0) {
            printf("5 ");
        }
        else if (result % 7 == 0) {
            printf("7 ");
        }
        else {
            printf("FAIL ");
        }
    }
    printf_s("\n");
}

int main(int argc, char** argv) {
    printf_s("Case #1:\n");

    uint64_t startIndex = 0x8001;

    writeBinaryNumber(startIndex);

    uint64_t totalCount = 0;
    for (uint64_t j = startIndex; (j < startIndex + 500000) || (totalCount >= 5); j+=2) {
        bool itemFound = true;
        writeBinaryNumber(j);
        //printf_s("%s ", binaryString);
        for (uint64_t i = 2; i < 11; i++) {
            uint64_t result = getBaseFromBinary(i);
            //printf("%I64u ", result);
            if (result % 2 == 0) {
                //printf("2 ");
            }
            else if (result % 3 == 0) {
                //printf("3 ");
            }
            else if (result % 5 == 0) {
                //printf("5 ");
            }
            else if (result % 7 == 0) {
                //printf("7 ");
            }
            else {
                //printf("FAIL ");
                itemFound = false;
            }
        }
        if (itemFound) {
            totalCount++;
            WriteResult(j);
        }
        if (totalCount == 50) {
            break;
        }
        //printf_s("\n");
    }
}
