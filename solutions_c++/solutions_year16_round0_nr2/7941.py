//
//  main.cpp
//  Revenge of the Pancakes
//
//  Copyright © 2016 Robotex. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <set>

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
    std::string S;
    auto flipfun = [] (char c) { return c=='-'?'+':'-'; };
    
    fin >> T;
    fin.ignore();
    for (unsigned i = 1; i <= T; ++i)
    {
        std::getline(fin,S);
        
        unsigned int flips = 0;
        
        for (std::string::reverse_iterator it = S.rbegin(); it != S.rend(); ++it)
        {
            if (*it == '+')
                continue;
            if (S.front() == '-')
            {
                std::reverse(it, S.rend());
                std::transform(it, S.rend(), it, flipfun);
            }
            else
            {
                std::string::reverse_iterator searchit;
                for (searchit = it; *searchit!='+'; ++searchit);
                std::reverse(searchit, S.rend());
                transform(searchit, S.rend(), searchit, flipfun);
            }
            ++flips;
        }
        
        fout << "Case #" << i << ": " << flips << std::endl;
    }
    return 0;
}
