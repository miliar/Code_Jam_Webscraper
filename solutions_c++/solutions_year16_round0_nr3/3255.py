#include <fstream>
#include <iostream>
#include <vector>
#include <string>
#include <cassert>
#include <cmath>
#include <algorithm>

size_t is_prime(size_t num) {
    size_t nmax = (size_t)ceil(sqrt(num)) + 1;
    if (nmax > num) nmax = num;
    for (size_t idx = 2; idx < nmax; ++ idx) {
        if (num % idx == 0) {
            return idx;
        }
    }
    return (size_t)~0;
}
size_t interpret(size_t num, size_t base, size_t basein=2) {
    size_t numout = 0;
    size_t basemult = 1;
    while (num != 0) {
        numout += (num % basein) * basemult;
        num /= basein;
        basemult *= base;
    }
    return numout;
}
std::string base2str(size_t num, size_t width) {
    std::string s(width, '0');
    size_t num2 = num;
    size_t idx = 0;
    while (num2 != 0) {
        if (num2 % 2) { s[idx] = '1'; }
        num2 /= 2;
        ++ idx;
    }
    std::reverse(s.begin(), s.end());
    return s;
}
void test_base2() {
    assert(base2str(10, 5) == "01010");
    assert(base2str(30, 10) == "0000011110");
}
void test_interpret() {
    assert(interpret(5, 2, 2) == 5);
    assert(interpret(15, 2, 2) == 15);
    assert(interpret(155, 2, 2) == 155);
    assert(interpret(1559999, 2, 2) == 1559999);
    assert(interpret(5, 10, 2) == 101);
    assert(interpret(10, 10, 2) == 1010);
    assert(interpret(26, 10, 2) == 11010);
    assert(interpret(26, 7, 2) == 2751);
}
size_t is_prime(size_t num, size_t base, size_t basein=2) {
    size_t number = interpret(num, base, basein);
    return is_prime(number);
}
void test_is_prime() {
    assert(is_prime(5, 2) == (size_t)~0);
    assert(is_prime(3, 2) == (size_t)~0);
    assert(is_prime(13, 2) == (size_t)~0);
    assert(is_prime(14, 2) == 2);
    assert(is_prime(15, 2) == 3);
    assert(is_prime(17, 2) == (size_t)~0);
    assert(is_prime(29, 2) == (size_t)~0);
    assert(is_prime(30, 2) == 2);
    assert(is_prime(37, 2) == (size_t)~0);
    assert(is_prime(38, 2) == 2);
    assert(is_prime(73, 2) == (size_t)~0);
    assert(is_prime(74, 2) == 2);
    assert(is_prime(361, 2) == 19);
    assert(is_prime(26, 7, 2) == 3);
}

void run_tests() {
    test_interpret();
    test_base2();
    test_is_prime();
}

void compute_case(int caseid, std::ifstream& infile, std::ofstream& outfile) {
    size_t N, J;
    infile >> N >> J;

    size_t nfound = 0;
    outfile << "Case #" << caseid << ":" << std::endl;

    for (size_t inshell = 0;
            inshell < std::pow(2, N-2) && nfound < J;
            ++ inshell) {
        std::vector<size_t> divisors;
        size_t candidate = inshell * 2 + 1 + pow(2, N-1);
        for (size_t base = 2; base < 11; ++ base) {
            auto divisor = is_prime(candidate, base);
            if (divisor == (size_t)~0) {
                break;
            }
            divisors.push_back(divisor);
        }
        if (divisors.size() == 9) {
            ++ nfound;
            outfile << '1' << base2str(inshell, N-2) << '1';
            for (auto d: divisors) {
                outfile << ' ' << d;
            }
            outfile << std::endl;
        }
        else {
            std::cerr << '1' << base2str(inshell, N-2) << '1' << ": ";
            std::cerr << "divisors found:" << divisors.size() << std::endl;
        }
    }
}

int main(int argc, char** argv)
{
    run_tests();
    std::string fname(argv[1]);
    std::ifstream infile(fname);
    std::ofstream outfile(fname + "-out");
    int ncases;
    infile >> ncases;
    for (auto idx = 0; idx < ncases; ++ idx) {
        compute_case(idx + 1, infile, outfile);
    }
}
