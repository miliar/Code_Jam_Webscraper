// Willie Zhu
// 4-2-2013
// google code jam gcj
// fair-and-square

#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

int numCases;

inline bool isPalindrome(register int a) {

    int digit, num, rev = 0;
    num = a;

    while (a > 0) {
        digit = a % 10;
        rev = rev * 10 + digit;
        a = a / 10;
    }

    return num == rev;

}

int main() {


    ifstream inFile("fair-and-square.in");
    ofstream outFile("fair-and-square.out");

    inFile >> numCases;

    for (int cases = 0; cases < numCases; cases++) {

        int a, b, lowerLimit, upperLimit, numPalindromes = 0;

        inFile >> a >> b;

        lowerLimit = ceil(sqrt(a));
        upperLimit = floor(sqrt(b));

        for (int i = lowerLimit; i <= upperLimit; i++) {

            if (isPalindrome(i)) {

                if (isPalindrome(i * i)) {

                    numPalindromes++;

                }

            }

        }

        outFile << "Case #" << cases + 1 << ": " << numPalindromes << endl;

    }

}
