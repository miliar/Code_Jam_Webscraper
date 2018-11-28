#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <bitset>
#include <sstream>

typedef unsigned long long int ullint;

struct Jamcoin {
    std::string value_str;
    std::vector<ullint> divisors;
};

std::string int_to_bin_string(ullint v, ullint n) {
    std::stringstream sstr;
    const ullint shift = n - 1;
    const unsigned mask = 1 << shift;
    for ( ullint i = 1; i <= shift + 1; i++ ) {
        sstr << ( v & mask ? '1' : '0' );
        v <<= 1;
    }
    return sstr.str();
}

unsigned long long int get_val_for_base(Jamcoin jc, ullint b) {
    unsigned long long int val = 0;
    ullint len = jc.value_str.length();
    for (ullint i = 0; i < len; i++) {
        val += (jc.value_str[i] - '0') * std::pow(b, len - i - 1);
    }
    return val;
}

ullint find_divisor(ullint v) {
    // special case: even values
    if (v % 2 == 0) {
        return 2;
    }
    // odd values
    //special case: multiples of 3 and 5
    std::string val_str = std::to_string(v);
    // multiples of 5
    if (val_str.back() == '5') return 5;
    // multiples of 3
    ullint digits_sum = 0;
    for (ullint i = 0 ; i < val_str.length(); i++) {
        digits_sum += (val_str[i] - '0');
    }
    if (digits_sum % 3 == 0) return 3;
    
    ullint d = 7;
    std::vector<ullint> bad_divs;
    while (d < sqrt(v)) {
//        bool potential_div = true;
//        for (auto bad_div : bad_divs) {
//            if (d % bad_div == 0) {
//                // skip this div
//                potential_div = false;
//                break;
//            }
//        }
//        if (potential_div) {
            if (v % d == 0) {
                return d;
            }// else {
//                bad_divs.push_back(d);
//            }
//        } else {
//            bad_divs.push_back(d);
//        }
        
        d += 2;
    }
    return 0;
}

ullint find_divisor_light(ullint v) {
    // special case: even values
    if (v % 2 == 0) {
        return 2;
    }
    // odd values
    //special case: multiples of 3 and 5
    std::string val_str = std::to_string(v);
    // multiples of 5
    if (val_str.back() == '5') return 5;
}

bool verify_jamcoin(Jamcoin &jc) {
    // check for each basis interpretation:
    // - value must not be prime
    // - value must have a non-trivial divisor
    for (ullint b = 10; b >= 2; b--) {
        unsigned long long int val_base = get_val_for_base(jc, b);
//        std::cout << "base : " << b << ", val : " << val_base;
        ullint div = find_divisor(val_base);
//        std::cout << ", div : " << div << std::endl;
        if (div == 0) {
            return false;
        } else {
            jc.divisors.insert(jc.divisors.begin(), div);
//            jc.divisors.push_back(div);
        }
    }
    if (jc.divisors.size() == 9) {
        return true;
    }
    return false;
}

std::vector<Jamcoin> get_jamcoins(ullint n, ullint j) {
    // n = length of jamcoins
    // j = number of jamcoins to produce
    ullint min_val = std::pow(2, n - 1) + 1; // minimum value of jamcoin
    ullint max_val = std::pow(2, n) - 1; // maximum value of jamcoin
    ullint current_val = min_val;
    
    // produce enough jamcoins
    std::vector<Jamcoin> jamcoins;
    while (jamcoins.size() < j && current_val <= max_val) {
        // produce an extra jamcoin
        // value are incremented by 2 because only odd numbers finish with the digit 1 in binary
//        std::cout << "current_val = " << current_val << std::endl;
        Jamcoin jamcoin;
        jamcoin.value_str = int_to_bin_string(current_val, n);
        current_val += 2;
        // Check jamcoin and add it if it's valid
        if (verify_jamcoin(jamcoin)) {
            jamcoins.push_back(jamcoin);
            // print out
            std::cout << jamcoin.value_str;
            for (auto divisor : jamcoin.divisors) {
                std::cout << " " << divisor;
            }
            std::cout << std::endl;
        }
    }
    return jamcoins;
}

int main() {
    
    Jamcoin jc;
    jc.value_str = "1000000001001101";
//    std::cout << verify_jamcoin(jc) << std::endl;
    
    ullint t, n, j;
    std::cin >> t;  // read T
    for (ullint i = 1; i <= t; ++i) {
        std::cin >> n >> j;  // read N and J
        std::cout << "Case #" << i << ":" << std::endl;
        std::vector<Jamcoin> jamcoins = get_jamcoins(n, j);
//        for (auto jamcoin : jamcoins) {
//            std::cout << jamcoin.value_str;
//            for (auto divisor : jamcoin.divisors) {
//                std::cout << " " << divisor;
//            }
//            std::cout << std::endl;
//        }
    }
}
