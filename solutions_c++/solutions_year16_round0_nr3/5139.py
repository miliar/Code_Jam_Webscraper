#include <iostream>
#include <vector>
#include <map>
#include <cmath>
#include <unordered_map>
#include <set>
#include <cstdint>
#include <bitset>

using namespace std;

#define debug(...) fprintf(stderr, __VA_ARGS__)
//#define debug(format, ...)

#define BASE_LIMIT 10
#define NUM_BITS 32

vector<int> primes =
{ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79,
  83, 89, 97, 101 };

uint64_t getNumber(bitset<NUM_BITS>& bits, int base) {
    uint64_t number = 0;
    for (unsigned i=0; i < bits.size(); ++i) {
        if (bits.test(i))
            number += pow(base, i);
    }
    return number;
}

int getK(uint64_t number) {
    int num = -1;
    for (unsigned i=0; i < primes.size(); ++i) {
        if (number % primes.at(i) == 0)
            return primes.at(i);
    }
    return num;
}

void changeBits(bitset<NUM_BITS>& bits) {
    uint64_t newNum = bits.to_ullong();
    bitset<NUM_BITS> newBits(newNum + 0b10);
    bits = newBits;
}

int main(int argc, char* argv[])
{
    string inputFile = "input.in";
    string outputFile = "output.out";

    if (argc >= 3) {
        inputFile = argv[1];
        outputFile = argv[2];
        debug("Using inputFile \"%s\" and outputFile \"%s\"\n", inputFile.c_str(), outputFile.c_str());
    }

    freopen(inputFile.c_str(), "r", stdin);
    freopen(outputFile.c_str(), "w", stdout);

    int tc;
    cin >> tc;

    int N, J;
    cin >> N >> J;

    debug("CoinJam with %d testcases: N %d, J %d\n", tc, N, J);
    bitset<NUM_BITS> bits;
    bits.set(0);
    bits.set(N-1);

    printf("Case #%d:\n", 1);

    for (int i=0; i < J; ++i) {
        vector<int> kVector;
        do {
            kVector.resize(0);

            for (int base = 2; base <= BASE_LIMIT; ++base) {
                uint64_t number = getNumber(bits, base);
                int K = getK(number);
                if (K > 0) {
                    kVector.insert(kVector.end(), K);
                } else {
                    changeBits(bits);
                    break;
                }
            }
        } while (kVector.size() != BASE_LIMIT-1);

        string result = bits.to_string();
        size_t onePos = result.find_first_of('1');
        result = result.substr(onePos);
        printf("%s", result.c_str());
        for (int j=0; j < BASE_LIMIT-1; ++j) {
            printf(" %d", kVector.at(j));
        }
        printf("\n");

        changeBits(bits);
    }

    return 0;
}
