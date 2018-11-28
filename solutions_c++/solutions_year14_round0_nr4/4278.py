#include <fstream>
#include <sstream>
#include <stdio.h>
#include "test_case.h"

/* This program uses C++ 11 features
 * Please use -std=c++0x if compiling with g++ */
int main(int argc, char* argv[])
{
    /* Accept an input file as an argument */
    if (argc != 2)
        return 1; /* Otherwise quit */

    std::ifstream input_file(argv[1]);
    std::string line;
    int count = 0;
    int num_blocks = 0;
    std::vector<std::string> two_lines;
     
    while(std::getline(input_file, line))
    {
        if (count != 0)
        {
            /* Process a test case, next 3 lines */
            num_blocks = atoi(line.c_str());
            /* Get Naomi's block masses */
            std::getline(input_file, line);
            two_lines.push_back(line);
            /* Get Ken's block masses */
            std::getline(input_file, line);
            two_lines.push_back(line);

            /* Create test case */
            TestCase tcase(count, num_blocks, two_lines);
            /* Find solution and print to std out */
            tcase.FindSolution();
            two_lines.clear();
        }

        ++count;
    }

    return 0;
}

