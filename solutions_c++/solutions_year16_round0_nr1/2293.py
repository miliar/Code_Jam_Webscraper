#include <unordered_map>
#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

int total;
int digitCounted[10];
long long testCaseIndex;

void purgeDigits() {
    for (int i=0; i<10; ++i) {
        digitCounted[i] = 0;
    }
}

void PutDigitsIn(long long num) {
    long long test = num;
    int removedDigit;
restartput:
    if (test < 10) {
        digitCounted[test] = 1;
        return;
    }
    removedDigit = test % 10; // 12345 -> check 5
    digitCounted[removedDigit] = 1; // add 5
    test = (long long)floor(test / 10); // 12345 -> 1234.5 -> 1234.0
    goto restartput;
}

bool checkIfFullDigits() {
    for (int i=0; i<10; ++i) {
        if (digitCounted[i] == 0) {
            return false;
        }
    }
    return true;
}

long long sleepsAt(long long start) {
    if (start == 0) { return -1; }
    long long current = start;
    
restart:
    
    PutDigitsIn(current);
    if (checkIfFullDigits() == true) {
        return current;
    }
        
    current = current + start;
    goto restart;
}

int main()
{
    purgeDigits();
    
    cin >> total;
    for (testCaseIndex = 1 ; testCaseIndex <= total; ++testCaseIndex) {
        purgeDigits();
        long long testcase;
        cin >> testcase;
        long long result;
        
        result = sleepsAt(testcase);
        
        if (result > -1) {
            cout << "Case #" << testCaseIndex << ": " << result << endl;
        } else {
            cout << "Case #" << testCaseIndex << ": INSOMNIA" << endl;
        }
    }
    return 0;
}

