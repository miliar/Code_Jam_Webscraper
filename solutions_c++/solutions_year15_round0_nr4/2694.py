#include <cstdlib>
#include <fstream>
#include <iostream>
#include <cmath>
#include <stdexcept>
#include <string>
#include <vector>

std::string
data_directory = "C:\\Users\\fusr\\data\\projects\\GCJ\\2015_Ominous_Omino\\source\\data\\";

struct input_t {
    int32_t x;
    int32_t r;
    int32_t c;
};

bool
richard = true;

bool
gabriel = false;

bool
solve_internal(
        const input_t& input)
{
    // can contain hole in the middle
    if (input.x >= 7) {
        std::cout << "r1 ";
        return richard;
    }

    // can create a big enough to overlap
    if (input.x > input.r && input.x > input.c) {
        std::cout << "r2 ";
        return richard;
    }

    // cannot possibly fill all space without overlapping
    if (((input.r * input.c) % input.x) != 0) {
        std::cout << "r3 ";
        return richard;
    }

    // can create a shape that cannot be fit in
    if ((input.x - (std::min( input.r, input.c) + 1)) >= std::min( input.r, input.c)) {
        std::cout << "r4 ";
        return richard;
    }

    if (input.x > 3 && (input.r * input.c) < input.x * 3) {
        std::cout << "r5 ";
        return richard;
    }

    std::cout << "g  ";
    return gabriel;
}

bool solve_internal2(
        const input_t& input)
{

}

void
solve(
        std::ofstream& outfile,
        const uint32_t test_index,
        const input_t& input)
{
    if (solve_internal(input) == richard) {
        std::cout   << "Case #" << test_index << ": RICHARD" << " " << input.x << " " << input.r << " " << input.c << std::endl;
        outfile     << "Case #" << test_index << ": RICHARD" << std::endl;
    } else {
        std::cout   << "Case #" << test_index << ": GABRIEL" << " " << input.x << " " << input.r << " " << input.c << std::endl;
        outfile     << "Case #" << test_index << ": GABRIEL" << std::endl;
    }
}

uint32_t
stoi(
        std::string value,
        size_t begin,
        size_t size)
{
    char* pend;
    const uint32_t convert_value = strtoul( value.substr( begin, size).c_str(), &pend, 10);
    return convert_value;
}

int
main(
        int argc,
        char* argv[]) {
    const std::string test = "D-small-attempt2";
    const std::string inpath = data_directory + test + ".in";
    const std::string outpath = data_directory + test + ".out";

    std::ifstream infile( inpath);
    if (!infile.good()) {
        throw std::runtime_error("Cannot open: " + inpath);
    }

    std::ofstream outfile( outpath);
    if (!outfile.good()) {
        throw std::runtime_error("Cannot open: " + outpath);
    }

    uint32_t test_count;
    infile >> test_count;
    //std::cout << "test_count=" << test_count << std::endl;

    std::vector<input_t> cases;
    for (size_t i = 0; i < test_count; i++) {
        input_t input;

        infile >> input.x;
        infile >> input.r;
        infile >> input.c;

        cases.push_back( input);
    }

    for (size_t i = 0; i < test_count; i++) {
        solve( outfile, i+1, cases.at( i));
    }

    infile.close();
    outfile.close();
}