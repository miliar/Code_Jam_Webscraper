//-----------------------------------------------------------------------------
// Template for G00gle C0de Jam :-)
//-----------------------------------------------------------------------------

#include <cstdlib>
#include <fstream>
#include <iostream>
#include <iterator>
#include <vector>
#include <string>


void solution(int test, std::vector<std::string>& data, std::ofstream& ofs) {
    ofs << "Case #" << test+1 << ": ";
    /* Start coding here */

	int max = std::stoi(data[1 + test * 2]);
    std::string range(data[2 + test * 2]);
    std::vector<int> audience;
    audience.reserve(max + 1);
    for (unsigned int i = 0; i < range.size(); ++i) {
        audience.push_back(range[i] - '0');
    }

std::cout << "Test case " << test + 1 << std::endl;
std::cout << "Size " << audience.size() << std::endl;
    
    unsigned int number = 0;
    unsigned int sum = 0;
    for (unsigned int i = 1; i < audience.size(); ++i) {
        std::cout << "i=" << i << " and sum=" << sum << std::endl;
        sum += audience[i - 1];
        if (sum < i) {
            ++number;
            ++sum;
        }
    }

    ofs << number;

    /* End */
    ofs << std::endl;
}


int
main(int argc, char *argv[])
{
    std::string bin_name(argv[0]);

    if(argc < 2) {
        std::cerr << "Usage : " << bin_name << " [dataFile]" << std::endl;
        return EXIT_FAILURE;
    }

    std::ifstream data_file(argv[1]);
    std::vector<std::string> data((std::istream_iterator<std::string>(data_file)), std::istream_iterator<std::string>());

    //for(std::vector<std::string>::iterator it = data.begin(); it != data.end(); ++it)
    //    std::cout << *it << ' ' << std::endl;

    std::ofstream ofs("res.out", std::ofstream::out);

    const int nb_tests_case = std::stoi(data[0]);
    for(int i = 0; i < nb_tests_case; ++i) {
        solution(i, data, ofs);
    }

    ofs.close();

    return EXIT_SUCCESS;
}
