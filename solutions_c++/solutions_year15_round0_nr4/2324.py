//-----------------------------------------------------------------------------
// Template for G00gle C0de Jam :-)
//-----------------------------------------------------------------------------

#include <cstdlib>
#include <fstream>
#include <iostream>
#include <iterator>
#include <vector>
#include <string>


static const std::string gab("GABRIEL");
static const std::string ric("RICHARD");
static const std::string err("ERROR");

std::string bruteforce(int x, int r, int c)
{
    switch(x)
    {
        case 1:
            switch(r)
            {
                case 1:
                    if ( c == 1) {
                        return gab;
                    }
                    else if (c == 2) {
                        return gab;
                    }
                    else if (c == 3) {
                        return gab;
                    }
                    else {
                        return gab;
                    }
                    break;
                case 2:
                    if ( c == 1) {
                        return gab;
                    }
                    else if (c == 2) {
                        return gab;
                    }
                    else if (c == 3) {
                        return gab;
                    }
                    else {
                        return gab;
                    }
                    break;
                case 3:
                    if ( c == 1) {
                        return gab;
                    }
                    else if (c == 2) {
                        return gab;
                    }
                    else if (c == 3) {
                        return gab;
                    }
                    else {
                        return gab;
                    }
                    break;
                case 4:
                    if ( c == 1) {
                        return gab;
                    }
                    else if (c == 2) {
                        return gab;
                    }
                    else if (c == 3) {
                        return gab;
                    }
                    else {
                        return gab;
                    }
                    break;
                default:
                    return err;
                    break;
            }
            break;
        case 2:
            switch(r)
            {
                case 1:
                    if ( c == 1) {
                        return ric;
                    }
                    else if (c == 2) {
                        return gab;
                    }
                    else if (c == 3) {
                        return ric;
                    }
                    else {
                        return gab;
                    }
                    break;
                case 2:
                    if ( c == 1) {
                        return gab;
                    }
                    else if (c == 2) {
                        return gab;
                    }
                    else if (c == 3) {
                        return gab;
                    }
                    else {
                        return gab;
                    }
                    break;
                case 3:
                    if ( c == 1) {
                        return ric;
                    }
                    else if (c == 2) {
                        return gab;
                    }
                    else if (c == 3) {
                        return ric;
                    }
                    else {
                        return gab;
                    }
                    break;
                case 4:
                    if ( c == 1) {
                        return gab;
                    }
                    else if (c == 2) {
                        return gab;
                    }
                    else if (c == 3) {
                        return gab;
                    }
                    else {
                        return gab;
                    }
                    break;
                default:
                    return err;
                    break;
            }
            break;
        case 3:
            switch(r)
            {
                case 1:
                    if ( c == 1) {
                        return ric;
                    }
                    else if (c == 2) {
                        return ric;
                    }
                    else if (c == 3) {
                        return ric;
                    }
                    else {
                        return ric;
                    }
                    break;
                case 2:
                    if ( c == 1) {
                        return ric;
                    }
                    else if (c == 2) {
                        return ric;
                    }
                    else if (c == 3) {
                        return gab;
                    }
                    else {
                        return ric;
                    }
                    break;
                case 3:
                    if ( c == 1) {
                        return ric;
                    }
                    else if (c == 2) {
                        return gab;
                    }
                    else if (c == 3) {
                        return gab;
                    }
                    else {
                        return gab;
                    }
                    break;
                case 4:
                    if ( c == 1) {
                        return ric;
                    }
                    else if (c == 2) {
                        return ric;
                    }
                    else if (c == 3) {
                        return gab;
                    }
                    else {
                        return ric;
                    }
                    break;
                default:
                    return err;
                    break;
            }
            break;
        case 4:
            switch(r)
            {
                case 1:
                    if ( c == 1) {
                        return ric;
                    }
                    else if (c == 2) {
                        return ric;
                    }
                    else if (c == 3) {
                        return ric;
                    }
                    else {
                        return ric;
                    }
                    break;
                case 2:
                    if ( c == 1) {
                        return ric;
                    }
                    else if (c == 2) {
                        return ric;
                    }
                    else if (c == 3) {
                        return ric;
                    }
                    else {
                        return ric;
                    }
                    break;
                case 3:
                    if ( c == 1) {
                        return ric;
                    }
                    else if (c == 2) {
                        return ric;
                    }
                    else if (c == 3) {
                        return ric;
                    }
                    else {
                        return gab;
                    }
                    break;
                case 4:
                    if ( c == 1) {
                        return ric;
                    }
                    else if (c == 2) {
                        return ric;
                    }
                    else if (c == 3) {
                        return gab;
                    }
                    else {
                        return gab;
                    }
                    break;
                default:
                    return err;
                    break;
            }
            break; 
        default:
            return err;
            break;
    }
}

void solution(int test, std::vector<int>& data, std::ofstream& ofs) {
    ofs << "Case #" << test+1 << ": ";
    /* Start coding here */

    int x = data[1 + test*3];
    int r = data[1 + test*3 + 1];
    int c = data[1 + test*3 + 2];

    std::string name = bruteforce(x, r, c);

    ofs << name;

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
    std::vector<int> data((std::istream_iterator<int>(data_file)), std::istream_iterator<int>());

    //for(std::vector<int>::iterator it = data.begin(); it != data.end(); ++it)
    //    std::cout << *it << ' ' << std::endl;

    std::ofstream ofs("res.out", std::ofstream::out);

    const int nb_tests_case = data[0];
    for(int i = 0; i < nb_tests_case; ++i) {
        solution(i, data, ofs);
    }

    ofs.close();

    return EXIT_SUCCESS;
}
