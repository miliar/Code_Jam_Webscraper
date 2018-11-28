#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES
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

int main()
{
    int CASES;
    cin >> CASES;
    for (int CASE = 1; CASE <= CASES; ++CASE)
    {
        string s; int k;
        cin >> s >> k;
        int flips = 0;

        for (int i = 0; i < s.size() - k + 1; ++i)
        {
            if (s[i] == '-')
            {
                for (int j = i; j < i + k; ++j)
                    s[j] = s[j] == '-' ? '+' : '-';

                ++flips;
            }
        }

        if (s.find('-') == string::npos)
            printf("Case #%d: %d\n", CASE, flips);
        else
            printf("Case #%d: IMPOSSIBLE\n", CASE);

    }

    return 0;
}
