#ifndef PROBLEM_H
#define PROBLEM_H

#include <vector>
#include <string>

class Problem
{
    public:
        std::vector<std::string> header;
        std::vector< std::vector<std::string> > cases;

        Problem();
};

#endif
