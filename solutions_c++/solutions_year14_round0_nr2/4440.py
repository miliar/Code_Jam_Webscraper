#include <fstream>
#include <sstream>
#include <stdio.h>
#include "test_case.h"

int main(int argc, char* argv[])
{
    /* Accept an input file as an argument */
    if (argc != 2)
        return 1; /* Otherwise quit */

    std::ifstream input_file(argv[1]);
    std::string line;
    int count = 0;
     
    while(std::getline(input_file, line))
    {
        if (count != 0)
        {
            /* Process a test case, next 1 line */
            /* Create test case */
            TestCase tcase(count, line);
            /* Find solution and print to std out */
            tcase.FindSolution();
        }

        ++count;
    }

    return 0;
}

