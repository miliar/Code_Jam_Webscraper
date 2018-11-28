#include <iostream>
#include <map>
#include <vector>
#include <bitset>
#include <cstdlib>
#include <cmath>

using namespace std;

unsigned long convert_to_base(string& str, int base)
{
    char *start = &str[0];
    char *end;
    return strtoul(start, &end, base);
}

unsigned long convert_to_any_base(bitset<32>& bitSet, const int bits, int base)
{
    unsigned long sum = 0;
    for (int i = 0; i < bits; i++) {
        sum += bitSet[i] * pow(base, i);
    }
    return sum;
}

int main()
{
    int T, N, J;
    int count = 0;

    cin >> T;
    cin >> N;
    cin >> J;

    string minString = "1" + string(N-2, '0') + "1";
    string maxString = string(N, '1');

    bitset<32> min(minString);
    bitset<32> max(maxString);

    const unsigned long uMin = min.to_ulong();
    const unsigned long uMax = max.to_ulong();

    cout << "Case #1:" << endl;
    for (unsigned long i = uMin; i <= uMax; ++i) {
        bitset<32> b(i);
        string strVal = b.to_string().substr(32 - N);

        if ((strVal.front() != '1') || (strVal.back() != '1')) {
            // Skip jam coins that does not begin and end with 1:s
            continue;
        }

        // Calculate for each base 2-10
        bool primeNumber;
        for (int base = 2; base <= 10; ++base) {
            primeNumber = true;
            //unsigned long val = convert_to_base(strVal, base);
            unsigned long val = convert_to_any_base(b, N, base);

            // Check prime
            unsigned long n = 1;
            do {
                n++;
                if (val % n == 0) {
                    primeNumber = false;
                    break;
                }

            } while (!primeNumber || (n < sqrt(val)));

            // If the value is a prime in any base skip this value
            if (primeNumber) {
                break;
            }
        }

        if (!primeNumber) {
            // Calculate divisors
            cout << strVal << " ";
            // Find divisor
            for (int base = 2; base <= 10; base++) {
                //unsigned long n = convert_to_base(strVal, base);
                unsigned long n = convert_to_any_base(b, N, base);
                //cout << "n: " << n << endl;
                for (unsigned long m = 2; m < n; m++) {
                    //cout << "m: " << m << endl;
                    if ((n % m) == 0) {
                        cout << m << " ";
                        break;
                    }
                }
            }

            cout << endl;

            count++;

            if (count == J) break;
        }
    }

    return 0;
}

