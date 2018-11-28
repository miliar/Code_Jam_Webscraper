#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <map>
#include <set>

// using boost 128-bit integer implementation
#include <boost/multiprecision/cpp_int.hpp>

using namespace std;
using namespace boost::multiprecision;

bool is_prime(int128_t n, int128_t& divisor)
{
    // the number will always be atleast 3 ('11' in base 2)
    if (n == 3)
        return true;
    else if (n % 2 == 0)
    {
        divisor = 2;
        return false;
    }
    else if (n % 3 == 0)
    {
        divisor = 3;
        return false;
    }

    int128_t i = 5;
    // limit the divisor to a nominal value to save time
    while (i < 300000)
    {
        if (n % i == 0)
        {
            divisor = i;
            return false;
        }

        i += 2;
    }

    return true;
}

int main(int argc, char** argv)
{
    int T = 0;
    cin >> T;

    for (int i = 0; i < T; i++)
    {
        int N, J;
        cin >> N >> J;

        cout << "Case #" << (i + 1) << ":" << endl;

        // initial the digits of the number
        vector<char> digits(N);
        for (int j = 0; j < N; j++)
        {
            if (j == 0 || j == N - 1)
                digits[j] = '1';
            else
                digits[j] = '0';
        }

        // find J non-prime numbers in all bases 2 - 10
        int count = 0;
        while (true)
        {
            bool prime = false;
            int128_t number;
            vector<int128_t> divisors(9);
            for (int b = 2; b <= 10; b++)
            {
                number = 0;
                int128_t pow = 1;
                for (int d = 0; d < N; d++)
                {
                    number += (digits[d] - '0') * pow;
                    pow *= b;
                }

                int128_t divisor = -1;
                if (is_prime(number, divisor))
                {
                    prime = true;
                    break;
                }

                divisors[b - 2] = divisor;
            }

            if (!prime)
            {
                cout << number << " ";
                for (int b = 2; b <= 10; b++)
                {
                    cout << divisors[b - 2] << " ";
                }
                cout << endl;
                count++;

                if (count == J)
                    break;
            }

            // increment the number
            bool incremented = false;
            for (int d = 1; d < N - 1; d++)
            {
                if (digits[d] == '0')
                {
                    digits[d] = '1';
                    for (int r = d - 1; r > 0; r--)
                        digits[r] = '0';
                    incremented = true;
                    break;
                }
            }

            if (!incremented)
            {
                cout << "IMPOSSIBLE" << endl;
                break;
            }
        }
    }
}