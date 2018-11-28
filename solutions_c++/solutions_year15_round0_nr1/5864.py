#include <cstdlib>
#include <iostream>
#include <fstream>
#include <stdexcept>
#include <string>
#include <vector>

std::string
data_directory = "C:\\tmp\\GCJ\\2015_Standing_Ovation\\";

void
solve(
        std::ofstream& outfile,
        const uint32_t test_index,
        const std::vector<uint32_t>& shyness)
{
    uint32_t invited = 0;
    uint32_t applauding_so_far = 0;
    for (size_t i = 0; i < shyness.size(); i++) {
        if (applauding_so_far < i) {
            uint32_t invite = i - applauding_so_far;
            applauding_so_far += invite;
            invited += invite;
        }
        applauding_so_far += shyness.at( i);
    }

    outfile << "Case #" << test_index << ": " << invited << std::endl;
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
    const std::string inpath = data_directory + "A-large.in";
    const std::string outpath = data_directory + "A-large.out";

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

    std::vector<std::vector<uint32_t>> cases;
    for (size_t i = 0; i < test_count; i++) {
        uint32_t test_size;
        infile >> test_size;
        //std::cout << "test_size=" << test_size << std::endl;

        cases.push_back( std::vector<uint32_t>());
        cases.back().reserve( test_size);

        std::string test_list;
        infile >> test_list;

        for (size_t j = 0; j <= test_size; j++) {
            cases.back().push_back( stoi( test_list, j, 1));
        }

        //for (size_t j = 0; j <= test_size; j++) {
        //    std::cout << cases.back().at(j) << " ";
        //}
        //std::cout << std::endl;
    }

    for (size_t i = 0; i < test_count; i++) {
        solve( outfile, i+1, cases.at( i));
    }

    infile.close();
    outfile.close();
}