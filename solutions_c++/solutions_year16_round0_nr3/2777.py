#define _CRT_SECURE_NO_WARNINGS
#include <cmath>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <iterator>
#include <ctime>
#include <iomanip>

using namespace std;

long long get_num(char const* s, long long base)
{
    long long res = 0;
    long long mul = 1;
    while (*s)
    {
        if (*s == '1')
            res += mul;

        mul *= base;
        ++s;
    }

    return res;
}

bool is_prime(long long num, long long& div)
{
    for (long long i = 2; i * i <= num; ++i)
    {
        if ((num % i) == 0)
        {
            div = i;
            return true;
        }
    }

    return false;
}

int main()
{
    int CASES = 1;
    //cin >> CASES;
    for (int CASE = 1; CASE <= CASES; ++CASE)
    {
        int n = 16, j = 50;
        //int n = 32, j = 500;
        //cin >> n >> j;

        int have = 0;
        string buff(n, '1');
        long long divs[11];

        set<string> why_not;

        printf("Case #%d:\n", CASE);
        while (have < j)
        {
            for (int i = 1; i < n - 1; ++i)
                buff[i] = (rand() % 2) ? '1' : '0';

            bool ok = true;
            for (int i = 2; i <= 10; ++i)
            {
                if (!is_prime(get_num(buff.c_str(), i), divs[i]))
                {
                    ok = false;
                    break;
                }
            }

            if (ok && !why_not.count(string(buff)))
            {
                ++have;
                reverse(buff.begin(), buff.end());
                printf("%s", buff.c_str());
                for (int i = 2; i <= 10; ++i)
                    cout << " " << divs[i];
                cout << endl;
                why_not.insert(string(buff));
            }
        }
    }


    return 0;
}
