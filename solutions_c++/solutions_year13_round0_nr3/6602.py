#include <cmath>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <complex>

using namespace std;

const char* OUTPUT_FILE_NAME = "FairAndSquare.out";

bool isPalindrome(int number) {
    ostringstream stringBuilder;
    stringBuilder << number;
    string numberString = stringBuilder.str();

    // Loop through half first character to check.
    for (int i = 0; i < numberString.length() / 2; i++) {
        // If corresponding characters not matched, return false.
        if (numberString.at(i) != numberString.at(numberString.length() - i - 1)) {
            return false;
        }
    }

    return true;
}

bool isSquareNumber(int number) {
    // Get square root.
    double squareRoot = sqrt(number);

    // If after decimal is not 0, return false.
    if (squareRoot - (int) squareRoot != 0) {
        return false;
    }

    return true;
}

int getNumberOfFairAndSquares(int start, int end) {
    int count = 0;

    // Loop from start to end to find.
    for (int number = start; number <= end; number++) {
        /*
         * If current number is a palindrome and square number, check it's
         * square root.
         */
        if (isPalindrome(number) && isSquareNumber(number)) {
            // Get square root.
            int squareRoot = (int) sqrt(number);

            // If the square root is a palindrome, increment count.
            if (isPalindrome(squareRoot)) {
                count++;
            }
        }
    }

    return count;
}

int main(int argc, char** argv) {
    int numberOfTestCases;
    string input;
    int start, end;
    istringstream inputParser;
    ostringstream outputBuilder;

    // Get number of test cases.
    getline(cin, input);
    inputParser.str(input);
    inputParser >> numberOfTestCases;

    // Get test cases.
    for (int i = 0; i < numberOfTestCases; i++) {
        getline(cin, input);

        // Get bounds.
        inputParser.clear();
        inputParser.str(input);
        inputParser >> start >> end;

        // Check palindromes and add to output.
        outputBuilder << "Case #" << (i + 1) << ": "
                << getNumberOfFairAndSquares(start, end) << '\n';
    }

    // Display output.
    cout << outputBuilder.str();

    // Write to file.
    ofstream fileWriter;
    fileWriter.open(OUTPUT_FILE_NAME);
    fileWriter << outputBuilder.str();
    fileWriter.close();

    return EXIT_SUCCESS;
}

