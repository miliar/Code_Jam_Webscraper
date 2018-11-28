#include <iostream>
#include <cstdlib>
#include <fstream>
#include <cmath>

using namespace std;

typedef unsigned long long int ULLINT;

bool IsPalindrome(const ULLINT&);
ULLINT IsPerfectSquare (const ULLINT&);

int main() {

    fstream fileObj;
    int NUM_TESTS = 0;

    char fName[] = "D-small.in";
    fileObj.open(fName, ios::in);

    if (fileObj == NULL) {
        cerr << "Can't open file" << endl;
        exit(-1);
    }

    fileObj >> NUM_TESTS;
    cout << "Number of test cases: " << NUM_TESTS << endl;

    for (int tIndex = 0; tIndex < NUM_TESTS; tIndex++) {
    
        ULLINT minB, maxB, lbound, ubound;
        fileObj >> minB;
        fileObj >> maxB;
//        cout << minB << " " << maxB << endl;
    
        lbound = IsPerfectSquare(minB);
        ubound = (ULLINT) sqrt(maxB);

//        cout << lbound << ", " << ubound << endl;

        int countFS = 0;
        for (ULLINT i = lbound; i <= ubound; i++) {
            int i2 = i * i;
            if (IsPalindrome(i) && IsPalindrome(i2)) {
                countFS++;
//                cout << "FOUND!! : " << i << endl << endl;
            }
        }
        
        cout << "Case #" << tIndex + 1 << ": " << countFS << endl;
    }
     
    return 1;
}

bool IsPalindrome (const ULLINT& num) {
    
    int numDigits = log10(num) + 1;
//    cout << "Number: " << num << endl 
//         << numDigits << ", ";

    if (numDigits == 1)
        return true;

    ULLINT maxNumber = 1;
    for (int i = 0; i < numDigits; i++)
        maxNumber *= 10;
    
//    cout << maxNumber << endl;
    ULLINT indA = 10, indB = maxNumber;

    int Flag = 0;
    for (int i = 0; i < numDigits/2 ; i++) {
        int digitA = (num % indA) / (indA/10);
        int digitB = (num % indB) / (indB/10);
        
//        cout << digitA << " == " << digitB << endl;
        if (digitA != digitB) {
            Flag = 1;
            break;
        }

        indA *= 10;
        indB *= 10;
    }

    if (Flag == 0)
        return true;

    else
        return false;
}

ULLINT IsPerfectSquare (const ULLINT& num) {
    
    int num_2 = (ULLINT) sqrt(num);
    if (num == num_2 * num_2)
        return num_2;
    else
        return num_2 + 1;
}

