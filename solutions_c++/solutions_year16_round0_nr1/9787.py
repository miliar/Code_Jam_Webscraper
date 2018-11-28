#include <cstdio>
bool digits[10];

int solve (int num) {
    int count = 0, times = 0, result = num, aDigit;
    do {
        ++times;
        num = result * times;
        while (num > 0 && count < 10) {
            aDigit = num % 10;
            num /= 10;
            if ( !digits[aDigit] ) {
                digits[aDigit] = true;
                ++count;
            }
        }
    } while (count < 10);
    return result * times;
}

int main () {
    int testCaseMax, testCase = 0, num, result;
    scanf("%d", &testCaseMax);
    while (testCaseMax--) {
        scanf("%d", &num);
        if (num == 0) {
            printf("Case #%d: INSOMNIA\n", ++testCase);
        }
        else {
            for (unsigned i = 0; i < 10; ++i)
                digits[i] = false;

            result = solve(num);
            printf("Case #%d: %d\n", ++testCase, result);
        }
    }
    return 0;
}
