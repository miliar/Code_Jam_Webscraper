// A.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <sstream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cmath>
#include <bitset>
#include <unordered_map>
#include <unordered_set>

#include "bigInt.h"
// BigInt::Rossi n1 ("314159265358979323846264338327950288419716939937510", BigInt::DEC_DIGIT);
// int stoi (const string& str, size_t* idx = 0, int base = 10);
// string to_string (val);

#define FOR(i,n) for (int (i) = 0; (i) < (n); i++)

int main(void)
{
    int t = 0;
    std::cin >> t;
    
    FOR(i,t)
    {
        std::string str;
        std::cin >> str;

        std::string res = str;

        //int flag[26] = {0};
        //for (auto a : str)
            //flag[a-'A']++;

        std::vector<std::string> trace;
        int j = 0;
        trace.push_back(str.substr(j++, 1));
        while (j < str.length() && !trace.empty())
        {
            std::vector<std::string> tmp;
            for (auto s : trace)
            {
                tmp.push_back(str.substr(j,1) + s);
                tmp.push_back(s + str.substr(j,1));
            }

            std::sort(tmp.begin(), tmp.end());

            j++;
            trace.clear();
            trace.push_back(*tmp.rbegin());
        }

        for (auto s : trace)
        {
            if (res < s)
                res = s;
        }

        std::cout << "Case #" << i+1 << ": " << res << std::endl;
    }

	return 0;
}

