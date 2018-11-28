//
//  main.cpp
//  Getting the Digits
//
//  Copyright © 2016 Robotex. All rights reserved.
//


#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

std::string removeCharsOnce(std::string s, std::string chars)
{
    for (long i=s.length()-1; i>=0; --i)
    {
        for (long j=chars.length()-1; j>=0; --j)
        {
            if (s[i] == chars[j])
            {
                s.erase(i,1);
                chars.erase(j,1);
            }
        }
    }
    return s;
}

int main(int argc, const char * argv[]) {
    // insert code here...
    if (argc != 2)
    {
        std::cout << "Pass the test case as argument" << std::endl;
        return 1;
    }
    
    std::ifstream fin(argv[1]);
    std::ofstream fout("output.txt");
    unsigned int T;
    std::vector<std::string> numbers = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
    std::vector<size_t> countNumbers(10);
    
    fin >> T;
    fin.ignore();
    for (unsigned i = 1; i <= T; ++i)
    {
        std::string S;
        
        std::getline(fin, S);
        
        fout << "Case #" << i << ": ";
        countNumbers[0] = std::count(S.begin(), S.end(), 'Z'); // 0
        countNumbers[2] = std::count(S.begin(), S.end(), 'W'); // 2
        countNumbers[4] = std::count(S.begin(), S.end(), 'U'); // 4
        countNumbers[6] = std::count(S.begin(), S.end(), 'X'); // 6
        countNumbers[8] = std::count(S.begin(), S.end(), 'G'); // 8
        
        for (int i = 0; i < countNumbers[0]; ++i) S=removeCharsOnce(S, numbers[0]);
        for (int i = 0; i < countNumbers[2]; ++i) S=removeCharsOnce(S, numbers[2]);
        for (int i = 0; i < countNumbers[4]; ++i) S=removeCharsOnce(S, numbers[4]);
        for (int i = 0; i < countNumbers[6]; ++i) S=removeCharsOnce(S, numbers[6]);
        for (int i = 0; i < countNumbers[8]; ++i) S=removeCharsOnce(S, numbers[8]);
        
        countNumbers[1] = std::count(S.begin(), S.end(), 'O'); // 1
        countNumbers[3] = std::count(S.begin(), S.end(), 'H'); // 3
        countNumbers[5] = std::count(S.begin(), S.end(), 'F'); // 5
        countNumbers[7] = std::count(S.begin(), S.end(), 'S'); // 7

        for (int i = 0; i < countNumbers[1]; ++i) S=removeCharsOnce(S, numbers[1]);
        for (int i = 0; i < countNumbers[3]; ++i) S=removeCharsOnce(S, numbers[3]);
        for (int i = 0; i < countNumbers[5]; ++i) S=removeCharsOnce(S, numbers[5]);
        for (int i = 0; i < countNumbers[7]; ++i) S=removeCharsOnce(S, numbers[7]);
        
        countNumbers[9] = std::count(S.begin(), S.end(), 'I'); // 9
        
        for (int i=0; i < 10; ++i)
            for (int j=0; j<countNumbers[i]; ++j)
                fout << std::to_string(i);
        fout << std::endl;
    }
    return 0;
}
