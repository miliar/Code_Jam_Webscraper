// CppPractice.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <iostream>
#include <vector>
#include <set>
#include <string>


int Solve(std::vector<int>& numbers)
{
    int res = 0;

    int left = 0;
    int right = 0;
    int N = numbers.size();

    for (int i = 0; i < N; i++)
    {
        int pos = -1;
        int val = std::numeric_limits<int>::max();

        for (int j = left; j < N - right; j++)
        {
            if (numbers[j] < val)
            {
                val = numbers[j];
                pos = j;
            }
        }

        if (pos - left < N - 1 - pos - right)
        {
            res += pos - left;

            for (int j = pos; j > left; j--)
            {
                numbers[j] = numbers[j-1];
            }

            left ++;
        }
        else
        {
            res += N-1 -pos - right;

            for (int j = pos; j < N - right - 1; j++)
            {
                numbers[j] = numbers[j+1];
            }

            right ++;

        }

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
        std::cin >> N;

        std::vector<int> numbers;

        for (int j = 0; j < N; j++)
        {
            int tmp;
            std::cin >> tmp;
            numbers.push_back(tmp);
        }

        int res = Solve(numbers);

        std::cout << "Case #" << i+1 << ": ";
        std::cout << res;
            
        std::cout  << std::endl;
    }

	return 0;
}

