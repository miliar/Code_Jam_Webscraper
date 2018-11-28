#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output-A-Large.txt", "w", stdout);

    long long T, caseNo = 1, N, digits[12], rem, allFound, i, mainNum, num;

    scanf("%lld", &T);

    while (T--) {
        scanf(" %lld", &N);

        if (N == 0) printf("Case #%lld: INSOMNIA\n", caseNo++);
        else {
            mainNum = N;
            memset(digits, 0, sizeof(digits));

            while (1) {
                allFound = 1;
                num = N;

                while (num != 0) {
                    rem = num % 10;
                    digits[rem]++;
                    num /= 10;
                }

                for (i = 0; i < 10; i++) {
                    if (digits[i] == 0) {
                        allFound = 0;
                        break;
                    }
                }

                if (allFound == 1) {
                    printf("Case #%lld: %lld\n", caseNo++, N);
                    break;
                }

                N += mainNum;
            }
        }
    }

    return 0;
}
