#include <fstream>
#include <vector>
#include <string>
#include "sercantutar-infint-6af5513/InfInt.h"
#define INFINT_USE_EXCEPTIONS

bool cover(size_t k, InfInt& N, std::vector<bool>& vec) {
    try {
        InfInt N2 = InfInt(k) * N;
        size_t ndigits = N2.numberOfDigits();
        for (size_t i = 0; i < ndigits; ++ i) {
            auto idigit = (int)N2.digitAt(i);
            vec[idigit] = true;
        }
    } catch(...) {
        return false;
    }
    return true;
}

bool covered(const std::vector<bool>& vec) {
    size_t nnz = 0;
    for (auto i: vec) { nnz += (i ? 1 : 0); }
    return nnz==10;
}

bool all_happy(const std::string& str) {
    for (auto chr: str) {
        if (chr != '+') return false;
    }
    return true;
}
void flip_next(std::string& str) {
    if (str.size() < 1) return;
    auto char1 = str[0];
    auto char2 = char1 == '+' ? '-' : '+';
    auto idx = str.find_first_of(char2);
    if (idx == std::string::npos) idx = str.size();
    // at this index, the string flips
    for (size_t jdx = 0; jdx < idx; ++ jdx) {
        str[jdx] = char2;
    }
}

void compute_case(int caseid, std::ifstream& infile, std::ofstream& outfile) {
    std::string Nstr;
    infile >> Nstr;

    size_t i = 0;
    while (!all_happy(Nstr)) {
        flip_next(Nstr);
        ++ i;
    }
    outfile << "Case #" << caseid << ": " << i << std::endl;
}

int main(int argc, char** argv)
{
    std::string fname(argv[1]);
    std::ifstream infile(fname);
    std::ofstream outfile(fname + "-out");
    int ncases;
    infile >> ncases;
    for (auto idx = 0; idx < ncases; ++ idx) {
        compute_case(idx + 1, infile, outfile);
    }
}
