/**
 * @brief      Google CodeJam 2016 qualification round C Coin Jam
 * @author     krikit (krikit@naver.com)
 * @copyright  Copyright (C) 2016-, No right reserved. ;)
 */


//////////////
// includes //
//////////////
#include <cmath>
#include <iostream>
#include <set>
#include <string>
#include <vector>


/**
 * @biref       whether prime number or not
 * @param  num  number to test
 * @return      prime or not
 */
int64_t is_prime(int64_t num) {
    if (num <= 1) return false;
    if (num % 2 == 0) return false;
    for (int64_t i = 3; i * i <= num; i += 2) {
        if (num % i == 0) return false;
    }
    return true;
}


/**
 * @brief       small case
 * @param  nnn  N
 * @param  jjj  J
 */
void small(int nnn, int jjj) {
    std::cout << "Case #1:" << std::endl;
    for (int64_t i = 0; i <= ((1 << 14) - 1); ++i) {
        std::string bin_str = "1" + std::bitset<14>(i).to_string() + "1";
        std::vector<int64_t> nums;    // converted numbers with base 2 ~ 10
        for (int base = 2; base <= 10; ++base) {
            int64_t num_base = strtol(bin_str.c_str(), NULL, base);
            if (is_prime(num_base)) break;
            nums.push_back(num_base);
        }
        if (nums.size() < 9) continue;
        std::cout << bin_str;
        for (std::vector<int64_t>::const_iterator iter = nums.begin(); iter != nums.end(); ++iter) {
            if (*iter % 2 == 0) {
                std::cout << " 2";
                continue;
            }
            for (int64_t prime = 3; prime * prime <= *iter; prime += 2) {
                if (*iter % prime == 0) {
                    std::cout << " " << prime;
                    break;
                }
            }
        }
        std::cout << std::endl;
        if (--jjj <= 0) break;
    }
}


void large() {
}


//////////
// main //
//////////
int main(int argc, char** argv) {
    int num_cases, nnn, jjj;
    std::cin >> num_cases >> nnn >> jjj;
    if (nnn == 16 && jjj == 50) {
        small(nnn, jjj);
    } else if (nnn == 32 && jjj == 500) {
        large();
    } else {
        std::cerr << "unknown data set" << std::endl;
        return -1;
    }
    return 0;
}
