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

#define flip(a) ((a) == '+' ? '-' : '+')

int main()
{
    int CASES;
    cin >> CASES;
    for (int CASE = 1; CASE <= CASES; ++CASE)
    {
        string s;
        cin >> s;

        int res = 0;
        int idx = s.size() - 1;

        while ((idx = s.rfind('-')) != string::npos)
        {
            if (s[0] == '+')
            {
                int start = 0;
                while (s[start] == '+')
                {
                    s[start] = '-';
                    ++start;
                }

                ++res;
            }

            for (int i = 0; i < idx / 2 + (idx & 1); ++i)
            {
                char tmp = flip(s[i]);
                s[i] = flip(s[idx - i]);
                s[idx - i] = tmp;
            }

            if (idx % 2 == 0)
                s[idx / 2] = flip(s[idx / 2]);

            ++res;
        }

        printf("Case #%d: %d\n", CASE, res);
    }


    return 0;
}
