#include <fstream>
#include <vector>
#include <string>


void compute_case(int caseid, std::ifstream& infile, std::ofstream& outfile) {
    size_t smax;
    std::string s;
    infile >> smax >> s;
    std::vector<int> vec;
    size_t nbelow = 0;
    size_t nrequired = 0;
    size_t nask = 0;
    for (auto ichar: s) {
        int ncurr = int(ichar - '0');
        int nadded = 0;
        if (nrequired > nbelow) {
            nadded = (nrequired - nbelow);
            nask += nadded;
        }
        nbelow += ncurr + nadded;
        ++ nrequired;
    }
    outfile << "Case #" << caseid << ": " <<  nask << std::endl;
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
