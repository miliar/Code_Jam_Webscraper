#include <fstream>
#include <sstream>
#include <vector>
#include <iostream>
#include <iterator>
#include <algorithm>
#include <string>
#include <stdio.h>
/* Obtain Boost Libraries at www.boost.org 
 * You can also install boost on Debian systems using:
 * apt-get install libboost-dev */
#include <boost/algorithm/string.hpp>

void FindSolution(int index, int sm, std::vector<int> S);

int main(int argc, char* argv[])
{
    /* Accept an input file as an argument */
    if (argc != 2)
        return 1; /* Otherwise quit */

    std::ifstream input_file(argv[1]);
    std::string line;
    std::vector<std::string> tokens; 
    std::vector<int> tcase;

    int len = 0;
    int count = 0;

    std::getline(input_file, line);
    //int num_lines = atoi(line.c_str());
    
    while(std::getline(input_file, line))
    {
        boost::split(tokens, line, boost::is_any_of(" "), boost::token_compress_on);
        len = tokens[1].length();
        for (int j=0; j<len; j++)
        {
            tcase.push_back(tokens[1][j] - '0'); 
        }
        FindSolution(count, atoi(tokens[0].c_str()), tcase);
        tcase.clear();
        ++count;
    }

    return 0;
}

void FindSolution(int index, int sm, std::vector<int> S)
{
    // Trivial cases
    if (sm == 0)
    {
        printf("Case #%d: %d\n",index+1,0);
        return;
    }    
    
    // Case when S_0 >= S_max
    if(S[0] >= sm)
    {
        printf("Case #%d: %d\n",index+1,0);
        return;
    }

    // All non-zero case
    bool found_zero = false;
    for (unsigned int i=0; i< S.size(); i++)
    {
        if (S[i] == 0)
            found_zero = true;
    }
    if (!found_zero)
    {
        printf("Case #%d: %d\n",index+1,0);
        return;
    }

    // General case
    unsigned int num_friends = 0;
    unsigned int num_standing = 0;
    unsigned int friends_to_add = 0;
    for (unsigned int i=0; i< S.size(); i++)
    {
        if (i == 0)
            num_standing = S[i];
        else if (S[i] != 0)
        {
            if(i > num_standing)
            {
                friends_to_add = i - num_standing;
                num_friends += friends_to_add;
                num_standing += friends_to_add;
                num_standing += S[i];
            }
            else
                num_standing += S[i];
        }
    }

    printf("Case #%d: %d\n",index+1,num_friends);
}
