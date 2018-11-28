#include <iostream>
#include <cstdio>
#include <string.h>

using namespace std;

int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    unsigned int T, N;
    bool digits[10];
    unsigned int countDigits;
    cin >> T;

    for (int i = 1; i <= T; ++i) {
        cin >> N;

        if (N == 0) {
            cout << "Case #" << i << ": " << "INSOMNIA" << endl;
            continue;
        }

        memset(&digits, false, sizeof(bool) * 10);
        countDigits = 0;

        unsigned int multiplier = 0;
        unsigned long long result;
        while (countDigits < 10) {
            result = N * ++multiplier;

            while(result > 0) {
                int currentDigit = result % 10;

                if (!digits[currentDigit]) {
                    digits[currentDigit] = true;
                    ++countDigits;
                }

                result /= 10;
            }
        }

        cout << "Case #" << i << ": " << N * multiplier << endl;
    }

	return 0;
}
