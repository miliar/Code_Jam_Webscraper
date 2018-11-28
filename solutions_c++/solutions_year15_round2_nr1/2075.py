// gj.cpp
//

#include <assert.h>

#include <fstream>
#include <sstream>
#include <stack>
#include <iomanip>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <algorithm>
#include <utility>

using namespace std;

typedef unsigned char uchar;
typedef unsigned int uint;
typedef unsigned __int64 uint64;

#define EPS (1E-10)
#define PI 3.1415926535897932384626433832795

uint64 s[1000010];

uint64 rev(uint64 x)
{
    uint64 r = 0;
    while (x)
    {
        r *= 10;
        r += x % 10;
        x /= 10;
    }

    return r;
}

int main(int argc, char* argv[])
{
    uint64 cases;
    cin >> cases;

    uint64 d = 10,
        q = 1;

    for (uint64 i = 1; i <= 1000000; ++i)
    {
        if (i % d == 0)
        {
            d *= 10;
            q *= 10;
        }

        if (i % 10 != 0)
        {
            uint64 rv = rev(i);
            if (rv < i)
                s[i] = min(s[i - 1], s[rv]) + 1;
            else
                s[i] = s[i - 1] + 1;
        }
        else
            s[i] = s[i - 1] + 1;
    }

    for (uint64 cs = 1; cs <= cases; ++cs)
    {
        uint64 n;
        cin >> n;

        cout << "Case #" << cs << ": " << s[n] << "\n";
    }

    return 0;
}
