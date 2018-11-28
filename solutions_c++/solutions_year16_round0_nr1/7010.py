#include <iostream>

using namespace std;

#define MAX_ITERATIONS 1000

void reset(bool digits[], int &iterations, bool &asleep);
void updateDigits(bool digits[], int number);
bool isAsleep(bool digits[]);

int main() {

    int testCases, number, iterations;
    bool digits[10], asleep;

    cin >> testCases;
    for(int i = 1; i <= testCases; i++) {
        cin >> number;
        reset(digits, iterations, asleep);
        do {
            iterations++;
            updateDigits(digits, number * iterations);
            asleep = isAsleep(digits);
        } while(iterations <= MAX_ITERATIONS && !asleep);
        if(asleep) {
            cout << "Case #" << i << ": " << number * iterations << endl;
        } else {
            cout << "Case #" << i << ": INSOMNIA" << endl;
        }
    }

    return 0;
}

void reset(bool digits[], int &iterations, bool &asleep) {
    iterations = 0;
    asleep = false;
    for(int i = 0; i < 10; i++) {
        digits[i] = false;
    }
}

void updateDigits(bool digits[], int number) {
    while(number != 0) {
        digits[number % 10] = true;
        number = number / 10;
    }
}

bool isAsleep(bool digits[]) {
    bool asleep = true;
    for(int i = 0; i < 10; i++) {
        asleep = asleep & digits[i];
    }
    return asleep;
}
