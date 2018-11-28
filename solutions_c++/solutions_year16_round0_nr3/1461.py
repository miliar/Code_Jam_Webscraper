#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <vector> 
#include <cstdint>
#include <cmath>
#include <boost/multiprecision/cpp_int.hpp>

using namespace std;
using namespace boost::multiprecision;

uint128_t calculate_value(int base, uint128_t jamcoin, int size ) {
    uint128_t value = 0;
    uint128_t bitval = 1;
    for (int i = 0; i < size; i++) {
        value += ((jamcoin & (1 << i)) >> i) * bitval;
        bitval *= base;
    }
    return value;
}

uint128_t divisor(uint128_t value) {
    if (value % 2 == 0) {
        return 2;
    } else if (value % 3 == 0) {
        return 3;
    } else {
        uint128_t test = 5;
        while (test <= 10000) {
        //while (test*test <= value) {
            if (value % test == 0) {
                return test;
            } else if (value % (test + 2) == 0) {
                return test + 2;
            }
            test += 6;
        }
    }
    return -1; // no divisor found
}

void print_jamcoin(uint128_t jamcoin, unsigned int size) {
    for (int i = size - 1; i >= 0; i--) {
        if (jamcoin & (1 << i)) {
            std::cout << "1";
        } else {
            std::cout << "0";
        }
    }
    std::cout << " ";
}

uint128_t next_jamcoin(uint128_t jamcoin, unsigned int size) {
    uint128_t val = jamcoin >> 1;
    val = ((val + 1) << 1) | 1;
    return val;
}

int main(int argc, char **argv) {
    int tests;
    cin >> tests;

    for (int i = 1; i <= tests; i++) {
        int size, num;
        cin >> size >> num;

        uint128_t jamcoin = (1 << (size - 1)) | 1;

        int found = 0;
        cout << "Case #" << i << ":" << endl;
        while (found < num) {
            std::vector<uint128_t> divisors;
            bool pass = true;
            //print_jamcoin(jamcoin, size);

            // Verify number is not prime in base
            for (int base = 2; base <= 10; base++) {
                uint128_t value = calculate_value(base, jamcoin, size);
                //std::cout << "    Base " << base << " value = " << value << endl;
                // Verify not prime
                uint128_t div = divisor(value);
                if (div == -1) {
                    //std::cout << "               Prime" << std::endl;
                    pass = false;
                    break;
                } else {
                    //std::cout << "               Divisor = " << div << std::endl;
                    divisors.push_back(div);
                }
            }

            if (pass) {
               found++;
                print_jamcoin(jamcoin, size);
               for (const auto & v: divisors) {
                   std::cout << v << " ";
               }
               std::cout << endl;
            }

            jamcoin = next_jamcoin(jamcoin, size);
        }
    }
    
    return 0;
}



