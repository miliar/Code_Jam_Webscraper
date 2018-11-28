#include <iostream>
#include <assert.h>
#include <tgmath.h>

#define TRUE 1
#define FALSE 0
#define TOTAL_DIGITS 10

using namespace std;

long findEndTerm (long startNumber, int digits[TOTAL_DIGITS]);
void checkDigitsIntoArray (long number, int digits[TOTAL_DIGITS]);
int arrayTotal (int digits[TOTAL_DIGITS]);

int main() {
    int testCases, caseCounter;
    long startNumber;
    int testArray[10] = {1,1,1,1,1,1,1,1,1,1};
    assert (arrayTotal(testArray) == TRUE);

    cin >> testCases;

    for (caseCounter = 0; caseCounter < testCases; caseCounter ++){
        cin >> startNumber;
        long stoppingNumber;
        int digits[TOTAL_DIGITS] = {0,0,0,0,0,0,0,0,0,0};
        if (startNumber == 0){
            cout << "Case #" << caseCounter + 1 << ": " << "INSOMNIA" << endl;

        } else {
            stoppingNumber = findEndTerm(startNumber, digits);
            cout << "Case #" << caseCounter + 1 << ": " << stoppingNumber << endl;
        }
    }

    return EXIT_SUCCESS;
}

long findEndTerm (long startNumber, int digits[TOTAL_DIGITS]){
    long number = 0;
    do {
        number += startNumber;
        checkDigitsIntoArray(number, digits);
    } while (arrayTotal(digits) == FALSE);
    return number;
}

void checkDigitsIntoArray (long number, int digits[TOTAL_DIGITS]){
    long thisDigit;
    do {
        long numberMinusLastDigit = number/10;
        numberMinusLastDigit *= 10;
        thisDigit = number - numberMinusLastDigit;
        number = number / 10;
        digits[thisDigit] = 1;
    } while (number > 0);
}

int arrayTotal (int digits[TOTAL_DIGITS]){
    int arrayCounter;
    int digitsSeen = 0;
    int allDigitsSeen = FALSE;
    for (arrayCounter = 0; arrayCounter < TOTAL_DIGITS; arrayCounter ++){
        if (digits[arrayCounter] == 1){
            digitsSeen ++;
        }
    }
    if (digitsSeen == TOTAL_DIGITS){
        allDigitsSeen = TRUE;
    }
    return allDigitsSeen;
}