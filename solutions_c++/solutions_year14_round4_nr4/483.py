// CppPractice.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <string>

int Count(std::set<std::string>& strings)
{
    std::set<std::string> dif;

    for (const std::string& string : strings)
    {
        for (int i = 0; i < string.size(); i++)
        {
            dif.insert(string.substr(0, i+1));
        }
    }

    return 1 + dif.size();
}

int Solve(std::vector<std::string>& s, int N, int& res, int& num)
{
    int maxSub = 1 << (2*s.size());

    res = 0;
    num = 0;

    for (int sub = 0; sub < maxSub; sub++)
    {
        std::vector<std::set<std::string>> split(N);

        int set = sub;
        bool ok = true;
        for (int j = 0; j < s.size(); j++)
        {
            int val = set & 3;
            set = set >> 2;
            if (val >= N)
            {
                ok = false;
                break;
            }

            split[val].insert(s[j]);

        }

        if (!ok)
            continue;
        
        int r = 0;
        for (int j = 0; j < N; j++)
        {
            if (split[j].size() == 0)
            {
                ok = false;
                break;
            }
            r += Count(split[j]);
        }

        if (!ok)
            continue;


        if (r >= res)
        {
            if (r == res)
            {
                num = (num + 1) % 1000000007;
            }
            else
            {
                res = r;
                num = 1;
            }
        }
    }
    return 0;
}

int _tmain(int argc, _TCHAR* argv[])
{

    std::istream* pis = &std::cin;

    //std::fstream fis(argv[1], std::fstream::in);
    //pis = &fis;
    
    
    std::istream& is = *pis;


    int T = 0;
    is >> T;
    for (int i = 0; i < T; i++)
    {
        int N = 0;
        int M = 0;

        is >> M >> N;

        std::vector<std::string> s;

        for (int j = 0; j < M; j++)
        {
            std::string tmp;
            is >> tmp;
            s.push_back(tmp);
        }

        int res;
        int num;
        Solve(s, N, res, num);

        std::cout << "Case #" << i+1 << ": ";
        std::cout << res << " " << num;
            
        std::cout  << std::endl;
    }

	return 0;
}

