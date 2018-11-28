#include <iostream>
#include <string>
#include <cmath>
#include <bitset>
#include <vector>

using namespace std;

typedef unsigned int uint;
typedef unsigned long long uint64;
uint vals[11];

//calculate primes
vector<bool> sieve;
vector<uint64> primes;

uint64 convertVal(uint64 val, uint64 base)
{
    uint64 result = 0;
    int i = 0; 
    while (val > 0)
    {
        result += (val % 10) * pow(base, i);
        val /= 10;
        i++;
    }

    return result;
}

uint64 incrementVal(uint64 val)
{
    uint64 result = 0;

    // convert to actual base 2 and add 2
    val = convertVal(val, 2);
    val += 2;

    uint64 i = 0;

    // reinterpret in base 10
    while (val)
    {
        result += pow(10, i) * (val & 0x01);
        val >>= 1;
        i++;
    }

    return result;
}

int main()
{
    cout << "Case #1: " << endl;

    uint64 val = 1000000000000001;
    bool prime = false;

    sieve.resize(33333335);
    // generate primes 
    sieve[0] = true;
    sieve[1] = true;

    for (uint64 i = 2; i < 33333335; i++)
    {
        // find next empty one
        if (sieve[i] == false)
        {
            for (uint64 j = i + i; j < 33333335; j += i)
            {
                sieve[j] = true;
            }
        }
    }

    for (uint64 i = 0; i < 33333335; i++)
    {
        if (sieve[i] == false)
        {
            primes.push_back(i);
        }
    }

    uint  J = 0;
    while (val < 1111111111111111 && J < 50)
    {
        // base 10 case:
        for (uint64 i = 0; i < primes.size(); i++)
        {
            if (!(val % primes[i]) && val != primes[i])
            {
                vals[10] = primes[i];
                break;
            }

            if (i+1 == primes.size())
            {
                prime = true;
            }
        }
        // all other bases
        for (uint base = 2; base < 10 && !prime; base++)
        {
            uint64 converted = convertVal(val, base);

            // find divisor
            for (uint64 i = 0; i < primes.size(); i++)
            {
                if (!(converted % primes[i]) && converted != primes[i])
                {
                    vals[base] = primes[i];
                    break;
                }

                if (i + 1 == primes.size())
                {
                    prime = true;
                }
            }
        }

        if (prime == false)
        {
            cout << val << " ";
            for (int i = 2; i <= 10; i++)
            {
                cout << vals[i] << " ";
            }
            cout << endl;
            J++;
        }
        else
        {
            //cout << val << endl;
        }

        val = incrementVal(val);
        prime = false;
    }
    return 0;
}