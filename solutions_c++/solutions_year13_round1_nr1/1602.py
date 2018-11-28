#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <vector>
#include <iostream>
#include <list>
#include <string>
#include <queue>
#include <numeric>
#include <algorithm>
#include <set>
#include <sstream>
#include <cmath>
#include <map>
#include <stack>
#include <ctime>
#include <cstring>
#include <cassert>

typedef signed char int8;
typedef unsigned char uint8;
typedef signed int int32;
typedef unsigned int uint32;
typedef signed long long int64;
typedef unsigned long long uint64;

#define mp(a, b) std::make_pair(a, b)
using namespace std;

int main()
{
    int CASES;
    cin >> CASES;
    for (int CASE = 1; CASE <= CASES; ++CASE)
    {
        uint64 r, t;
        cin >> r >> t;

        uint32 res = 0;

        while (t >= (r + 1) * (r + 1) - (r * r))
        {
            ++res;
            t -= (r + 1) * (r + 1) - (r * r);
            r += 2;
        }





        printf("Case #%d: %d\n", CASE, res);
    }
    return 0;
}
