//============================================================================
// Name        : task1.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <array>
#include <iostream>
#include <fstream>
#include <stdint.h>
#include <string>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <limits>
#include <iostream>
#include <utility>
#include <fstream>
#include <deque>

typedef unsigned __int128 ui128;

ui128 convert(std::string& s)
{
    ui128 res = 0;
    for (int n = 0; n < s.size(); ++n)
    {
        if (s[n] == '+')
        {
            res |= (ui128(1) << n);
        }
    }
    return res;
}

ui128 genmask(int n)
{
    ui128 res = 0;
    for (int i = 0; i < n; ++i)
    {
        res |= (ui128(1) << i);
    }
    return res;
}

void print(ui128 coin, int n)
{
    for (int i = 0; i < n; ++i)
    {
        if (coin & (ui128(1) << i))
        {
            std::cout << '+';
        }
        else
        {
            std::cout << '-';
        }
    }
}

ui128 transpose(ui128 coin, int n, ui128 mask)
{
    for (int i = 0; i < n / 2; ++i)
    {
        ui128 m1 = ui128(1) << i;
        ui128 m2 = ui128(1) << (n - i - 1);

        bool b1 = (coin & m1) != 0;
        bool b2 = (coin & m2) != 0;

        if (b1)
        {
            coin &= (~m2 & mask);
        }
        else
        {
            coin |= m2;
        }

        if (b2)
        {
            coin &= (~m1 & mask);
        }
        else
        {
            coin |= m1;
        }
    }

    if (n % 2 == 1)
    {
        ui128 mm = ui128(1) << (n / 2);
        bool bb = (coin & mm) != 0;
        if (bb)
        {
            coin &= (~mm & mask);
        }
        else
        {
            coin |= mm;
        }
    }

    return coin;
}

bool check(ui128 coin, ui128 mask)
{
    return (coin & mask) == mask;
}

int numleft(ui128 coin, int n)
{
    int k = 0;
    for (int i = 0; i < n; ++n)
    {
        if ((coin & (ui128(1) << (n - i - 1))) == 0)
        {
            break;
        }

        ++ k;
    }

    return k;
}

int qcount(ui128 coin, int n)
{
    int k = 0;
    int prev = (coin & 1);
    for (int i = 1; i < n; ++i)
    {
        int b = (coin >> i) & 1;
        if (b == prev)
        {
            ++ k;
        }
        prev = b;
    }

    return k;
}

struct ts
{
    ui128 coin = 0;
    int deep = 0;

    void print(int n)
    {
        std::cout << "{"; 
        ::print(coin, n); 
        std::cout << ", " << deep << "}";
    }
};

int main()
{
	std::fstream f;
	f.open("A-small.in");

	int T = 0;
	f >> T;

    __int128 t = 0;
    int maxdeep = 1000000;

	for (int i = 0; i < T; ++i)
	{
        std::string s;
        f >> s;
        int N = s.size();

        //std::deque<ts> stack;

        ui128 coin = convert(s);
        //ui128 mask = genmask(N);

        //ts item;
        //item.coin = coin;
        //item.deep = 0;
        //stack.push_back(item);

        std::cout << "Case #" << (i + 1) << ": ";

        int qorig = qcount(coin, N);
        //item.print(N);
        int metric = N - qorig;
        if (coin >> (N - 1) == 1)
        {
            metric --;
        }
        std::cout << metric << std::endl;

        /*int mindeep = maxdeep;
        int bestq = 0;

        while (not stack.empty())
        {
            ts item = stack.front();
            stack.pop_front();

            //std::cout << "In: ";
            //item.print(N);
            //std::cout << std::endl;

            if (item.deep >= mindeep)
            {
                //std::cout << "Too deep" << std::endl;
                continue; 
            }

            int q = qcount(item.coin, N);
            //item.print(N);
            //std::cout << q << std::endl;
            if (q < bestq)
            {
                continue;
            }
            bestq = q;

            if (check(item.coin, mask))
            {
                //std::cout << "Deep min " << item.deep << std::endl;
                mindeep = item.deep;
            }

            for (int i = 0; i < N; ++i)
            {
                ui128 nextcoin = transpose(item.coin, i + 1, mask);
                int q = qcount(nextcoin, N);
                if (q >= bestq)
                {
                    ts nextitem;
                    nextitem.coin = nextcoin;
                    nextitem.deep = item.deep + 1;
                    stack.push_back(nextitem);
                    //std::cout << q << std::endl;
                }
            }

            if (stack.size() > 1000000000)
            {
                std::cout << ":((((" << std::endl;
                break;
            }
        }

        std::cout << mindeep << std::endl;*/
	}
}












