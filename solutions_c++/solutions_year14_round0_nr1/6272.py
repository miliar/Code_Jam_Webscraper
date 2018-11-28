//
//  main.cpp
//  CodeJam1
//
//  Created by Aleem Haji on 2014-04-11.
//  Copyright (c) 2014 Inner Geek inc. All rights reserved.
//

#include <iostream>
#include <vector>

std::vector<std::string> split(std::string string, char along)
{
    std::vector<std::string> split;
    size_t iters = string.length();
    size_t start = 0;
    int i = 0;
    for ( ; i < iters; ++i ) {
        if ( string[i] == along ) {
            std::string sub = std::string(string.data() + start, i-start);
            split.push_back(sub);
            start = i + 1;
        }
    }
    std::string sub = std::string(string.data() + start, i-start);
    split.push_back(sub);
    
    return split;
}

std::string stdinLineXofY(int x, int y)
{
    std::string temp;
    std::string retval;
    int current = 0;
    while ( current < x ) {
        std::getline(std::cin, temp);
        ++current;
    }
    retval = temp;
    while ( current < y ) {
        std::getline(std::cin, temp);
        ++current;
    }
    return retval;
}

std::string stdinLineNGivenByFirstLineOfY(int y)
{
    std::string temp;
    std::getline(std::cin, temp);
    int guess = atoi(temp.data());
    
    return stdinLineXofY(guess, 4);
}

int main(int argc, const char * argv[])
{
    std::string temp;
    std::getline(std::cin, temp);
    int iters = atoi(temp.data());

    int counts[16];

    for ( int i = 0; i < iters; ++i )
    {
        memset(counts, 0, 16 * sizeof(int));
        
        std::string firstRow = stdinLineNGivenByFirstLineOfY(4);
        std::string secondRow = stdinLineNGivenByFirstLineOfY(4);
        
        std::vector<std::string> digits = split(firstRow, ' ');
        std::vector<std::string> temp = split(secondRow, ' ');
        digits.insert(digits.end(), temp.begin(), digits.end());

        for ( int i = 0; i < 8; ++i ) {
            ++counts[atoi(digits[i].data()) - 1];
        }
        
        bool badMagician = false;
        bool winner = false;
        int index = -1;
        for ( int i = 0; i < 16; ++i ) {
            if ( counts[i] == 2 && !winner ) {
                winner = true;
                index = i;
            }
            else if ( counts[i] == 2 ) {
                badMagician = true;
                index = -1;
            }
        }
        
        std::cout << "Case #" << i + 1 << ": ";
        if ( badMagician == true ) {
            std::cout << "Bad magician!";
        }
        else if ( winner == false ) {
            std::cout << "Volunteer cheated!";
        }
        else {
            std::cout << index + 1;
        }
        std::cout << "\n";
    }
    return 0;
}
