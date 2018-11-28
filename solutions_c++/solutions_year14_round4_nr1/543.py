// CppPractice.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <vector>
#include <set>
#include <string>


int Solve(int X, std::multiset<int>& sizes)
{
    int res = 0;
    while (sizes.size() > 0)
    {
        auto e = sizes.end();
        e--;
        int s = *e;
        sizes.erase(e);
        
        auto up = sizes.upper_bound(X-s);
        if (up != sizes.begin())
        {
            up--;
            sizes.erase(up);
        }

        res++;
    }
    return res;
}

int _tmain(int argc, _TCHAR* argv[])
{
    int T = 0;
    std::cin >> T;
    for (int i = 0; i < T; i++)
    {
        int N = 0;
        int X = 0;
        std::cin >> N >> X;

        std::multiset<int> sizes;

        for (int j = 0; j < N; j++)
        {
            int tmp;
            std::cin >> tmp;
            sizes.insert(tmp);
        }

        int res = Solve(X, sizes);

        std::cout << "Case #" << i+1 << ": ";
        std::cout << res;
            
        std::cout  << std::endl;
    }

	return 0;
}

