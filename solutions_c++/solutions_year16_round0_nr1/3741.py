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

void compute_case(int caseid, std::ifstream& infile, std::ofstream& outfile) {
    std::string Nstr;
    infile >> Nstr;
    InfInt N(Nstr);
    std::vector<bool> vec(10, false);

    int k = 1;
    bool success = false;
    while (N != InfInt(0) && k < 9999999) {
        if (!cover(k, N, vec)) {
            break; // overflow
        }
        success = covered(vec);
        if (success) {
            break;
        }
        ++ k;
    }
    if (success) {
        InfInt N2 = InfInt(k) * InfInt(N);
        outfile << "Case #" << caseid << ": " << N2.toString() << std::endl;
    } else {
        outfile << "Case #" << caseid << ": INSOMNIA" << std::endl;
    }
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
