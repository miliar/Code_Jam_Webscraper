#include <iostream>
#include <fstream>
#include <cstdint>
#include <set>
#include <boost/multiprecision/gmp.hpp>

using namespace boost::multiprecision;

int main(int argc, char** argv) {
    int n = 16;
    int j = 50;
    int currj = 0;
    std::cout << "Case #1:" << std::endl;

    // build first num;
    mpz_int first = boost::multiprecision::pow(mpz_int(2), n - 1) + 1;
    mpz_int current = first;
    mpz_int last = boost::multiprecision::pow(mpz_int(2), n) - 1;

    while ((current <= last) && currj < j) {
        char strbuf[1000];
        mpz_get_str(strbuf, 2, current.backend().data());
        //std::cout << strbuf << std::endl;
        mpz_int divisors[9];
        bool found2 = true;
        for (unsigned int base = 2; base <= 10; base++) {
            mpz_int tmp;
            mpz_set_str(tmp.backend().data(), strbuf, base);
            //std::cout << tmp << std::endl;
            bool found = false;
            if (tmp % 2 == 0) {
                found = true;
                divisors[base - 2] = 2;
            }
            else {
                //std::cout << tmp2 << std::endl;
                for (unsigned int divisor = 3; divisor <= boost::multiprecision::sqrt(tmp); divisor += 2) {
                    //std::cout << divisor << std::endl;
                    if (tmp % divisor == 0) {
                        found = true;
                        divisors[base - 2] = divisor;
                        break;
                    }
                }
            }
            if (!found) {
                found2 = false;
                break;
            }
        }

        if (found2) {
            std::cout << strbuf;
            for (unsigned int i = 0; i < 9; i++) {
                std::cout << " " << divisors[i];
            }
            std::cout << std::endl;
            currj++;
        }

        current += 2;
    }

    if (currj != j) {
        std::cout << "ACHTUNG" << std::endl;
    }

    return 0;
}