#include <iostream>
#include <stdio.h>
#include <algorithm>

using namespace std;

int checkDone(long long int digits[]) {
    for (long long int i = 0; i < 10; i++) {
        if (digits[i] == 0)
            return 0;
    }
    return 1;
}

void update(long long int digits[], int n) {
    while (n != 0) {
        digits[n % 10] = 1;
        n /= 10;
    }
}

int main() {
    long long int T;
    scanf("%lld", &T);
    string s;
    long long int len;
    long long int n;
    long long int digits[10];
    long long int i, j;
    for (i = 1; i <= T; i++) {
        scanf("%lld", &n);
        if (n == 0) {
            printf("Case #%lld: INSOMNIA\n", i);
            continue;
        }
        for (j = 0; j < 10; j++)
            digits[j] = 0;
        j = 1;
        long long int temp;
        while (1) {
            temp = j * n;
            update(digits, temp);
            if (checkDone(digits))
                break;
            j++;
        }
        printf("Case #%lld: %lld\n", i, temp);
    }
    return 0;
}
