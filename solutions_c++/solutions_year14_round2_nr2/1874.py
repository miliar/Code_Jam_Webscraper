#include <fstream>
#include <iostream>
#include <vector>
#include <sstream>
#include <string>
#include <cmath>
#include <map>
#include <cstdint>
#include <gmpxx.h>

using namespace std;

const uint64_t m1  = 0x5555555555555555; //binary: 0101...
const uint64_t m2  = 0x3333333333333333; //binary: 00110011..
const uint64_t m4  = 0x0f0f0f0f0f0f0f0f; //binary:  4 zeros,  4 ones ...
const uint64_t h01 = 0x0101010101010101; //the sum of 256 to the power of 0,1,2,3...

unsigned int popcount_3(unsigned long int x) {
    /* Source: wikipedia */
    x -= (x >> 1) & m1;
    x = (x & m2) + ((x >> 2) & m2);
    x = (x + (x >> 4)) & m4;
    return (x * h01)>>56;
}

int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        exit(1);
    }

    ifstream ifs(argv[1]);

    int T;
    ifs >> T;

    unsigned long int A, B, K;

    for (int i = 0; i < T; ++i)
    {
        unsigned long int count = 0;
        ifs >> A >> B >> K;

        for (unsigned long int i = 0; i < A; ++i) {
            for (unsigned long int j = 0; j < B; ++j) {
                if ((i & j) < K) {
                    ++count;
                }
            }
        }

        cout << "Case #" << (i+1) << ": " << count;
        cout << endl;
    }

    return 0;
}
