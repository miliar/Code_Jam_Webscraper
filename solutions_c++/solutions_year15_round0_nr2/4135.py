//-----------------------------------------------------------------------------
// Template for G00gle C0de Jam :-)
//-----------------------------------------------------------------------------

#include <cstdlib>
#include <fstream>
#include <iostream>
#include <iterator>
#include <vector>
#include <string>
#include <set>
#include <list>


int solution(int test, std::vector<int>& data, int next, std::ofstream& ofs) {
    ofs << "Case #" << test+1 << ": ";
    /* Start coding here */

    int indice = next + data[next] + 1; 

    std::multiset<int> plates;
    for (int i = 0; i < data[next]; ++i) {
        plates.insert(data[1 + next + i]);
    }

    std::multiset<int> plates1;
    for (int i = 0; i < data[next]; ++i) {
        plates1.insert(data[1 + next + i]);
    }

    std::list<int> results;
    std::list<int> results1;

    size_t time = 0;
    bool condition = true;

    while (condition) {
        std::multiset<int>::reverse_iterator rit = plates.rbegin();
        int value = *rit;
        //std::cout << "Max dans le multiset " << value << std::endl;
        results.push_back(time + value);
        if (time == 0 && value == 2) {
            condition = false;
            break;
        }
        if (value <= 2) {
            condition = false;
            break;
        }
        std::multiset<int>::iterator it = plates.end();
        --it;
        plates.erase(it);
        if (value & 0x01) {
            plates.insert(value/2 + 1);
            plates.insert(value/2);
        }
        else {
            plates.insert(value/2);
            plates.insert(value/2);
        }
        ++time;
    }


    time = 0;
    condition = true;

    while (condition) {
        std::multiset<int>::reverse_iterator rit = plates1.rbegin();
        int value = *rit;
        //std::cout << "Max dans le multiset " << value << std::endl;
        results1.push_back(time + value);
        if (time == 0 && value == 2) {
            condition = false;
            break;
        }
        if (value <= 2) {
            condition = false;
            break;
        }
        std::multiset<int>::iterator it = plates1.end();
        --it;
        plates1.erase(it);
        if (value == 9) {
            plates1.insert(3);
            plates1.insert(6);
        }
        else if (value & 0x01) {
            plates1.insert(value/2 + 1);
            plates1.insert(value/2);
        }
        else {
            plates1.insert(value/2);
            plates1.insert(value/2);
        }
        ++time;
    }


    results.sort();
    results1.sort();
    ofs << std::min(results.front(), results1.front());

    /* End */
    ofs << std::endl;
    return indice;
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
    std::vector<int> data((std::istream_iterator<int>(data_file)), std::istream_iterator<int>());

    //for(std::vector<int>::iterator it = data.begin(); it != data.end(); ++it)
    //    std::cout << *it << ' ' << std::endl;

    std::ofstream ofs("res.out", std::ofstream::out);

    int next = 1;
    const int nb_tests_case = data[0];
    for(int i = 0; i < nb_tests_case; ++i) {
        next = solution(i, data, next, ofs);
    }

    ofs.close();

    return EXIT_SUCCESS;
}
