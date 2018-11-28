#include <bits/stdc++.h>

#define DEBUG 1

using namespace std;

#if DEBUG
    FILE* input = fopen("input.txt", "r");
    FILE* output = fopen("output.txt", "w");
    #define scanf(...) fscanf(input, __VA_ARGS__)
    #define printf(...) fprintf(output, __VA_ARGS__)
#endif // DEBUG

typedef unsigned long long ull;

int main()
{
    int T;
    scanf("%d", &T);

    for (int t = 1; t <= T; t++) {
        int digitsFound = 0;
        bool foundDigit[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

        ull curNum, i;
        scanf("%llu", &curNum);

        for (i = 1; i < 100000; i++) {
            if (curNum == 0) {
                break;
            }

            ull testNum = curNum*i;
            while (testNum > 0) {
                int digit = testNum % 10;
                testNum /= 10;

                if (!foundDigit[digit]) {
                    foundDigit[digit] = true;
                    digitsFound++;
                }
            }

            if (digitsFound == 10) {
                break;
            }
        }

        if (digitsFound < 10) {
            printf("Case #%d: INSOMNIA\n", t);
        } else {
            printf("Case #%d: %llu\n", t, curNum*i);
        }
    }
    return 0;
}
