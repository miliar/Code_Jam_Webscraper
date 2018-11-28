#!/usr/bin/env cppsh
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <set>
#include <iterator>
#include <vector>
#include <sstream>
#include <cmath>
#include <queue>

int main(int argc, char* argv[])
{
    std::string str;
    std::getline(std::cin, str);
    const int N = atoi(str.c_str());
    for (int it = 0; it < N; ++it)
    {
        std::getline(std::cin, str); // eat length
        std::vector<int> plates;
        std::getline(std::cin, str); // get numbers
        std::stringstream ss(str);
        int val;
        while (ss >> val)
        {
            plates.push_back(val);
        }
        int a = 0;
        int b = 0;
        int maxDrop = -1;
        for (int i = 0; i < plates.size() - 1; ++i)
        {
            int diff = plates[i+1] - plates[i];
            if (diff < 0)
                a += -diff;
            maxDrop = std::max(maxDrop, -diff);
        }
        for (int i = 0; i < plates.size() - 1; ++i)
        {
            b += std::min(maxDrop, plates[i]);
        }
        std::cout << "Case #" << (it+1) << ": " << a << " " << b << std::endl;
    }
    return 0;
}
