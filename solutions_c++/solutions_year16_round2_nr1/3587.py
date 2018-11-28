#include <fstream>
#include <vector>
#include <string>
#include <sstream>


bool matches(const std::string& needles, const std::string& hay, std::string& removed) {
    std::string op = hay;
    for (auto ichar: needles) {
        auto pos = op.find(ichar);
        if (pos == std::string::npos) {
            return false;
        }
        op.erase(pos, 1);
    }
    removed = op;
    return true;
}

std::string removenum(const std::string& num, const std::string& s) {
    std::string op = s;
    for (auto ichar: num) {
        auto pos = op.find(ichar);
        op.erase(pos, 1);
    }
    return op;
}

const std::vector<std::string> numbers = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

const std::string numeral="0123456789";

bool interpret_as(const std::string& longstring,
                  size_t index,
                  std::string state,
                  std::string& finalstate) {
    if (index == numbers.size())
        return false;

    auto target = numbers[index];
    std::string removed;
    if (matches(target, longstring, removed)) {
        if (removed.empty()) {
            state += numeral[index];
            finalstate = state;
            return true;
        }
        if (interpret_as(removed, index, state + numeral[index], finalstate))
            return true;
        return interpret_as(longstring, index+1, state, finalstate);
    } else {
        return interpret_as(longstring, index+1, state, finalstate);
    }
}

void compute_case(int caseid, std::ifstream& infile, std::ofstream& outfile) {
    std::string s;
    infile >> s;

    std::string finalstate;
    interpret_as(s, 0, "", finalstate);

    outfile << "Case #" << caseid << ": " <<  finalstate << std::endl;
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
