#include <fstream>
#include <vector>
#include <string>
#include <cmath>


void compute_case(int caseid, std::ifstream& infile, std::ofstream& outfile) {
    std::size_t K, C, S;
    infile >> K >> C >> S;
    std::vector<size_t> positions;

    size_t offset = C > 1 ? std::pow(K, C-1) : 0;
    for (size_t idx = 0; idx < K; ++ idx) {
        positions.push_back(1 + idx + (idx * offset));
    }
    outfile << "Case #" << caseid << ":";
    for (auto pos: positions) {
        outfile << ' ' << pos;
    }
    outfile << std::endl;
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
