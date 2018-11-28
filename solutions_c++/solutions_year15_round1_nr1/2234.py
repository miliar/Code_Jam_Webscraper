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

uint64 m[10000];

int main(int argc, char* argv[])
{
    uint64 cases;
    cin >> cases;

    for (uint64 cs = 1; cs <= cases; ++cs)
    {
        uint64 n;
        cin >> n;

        for (uint64 i = 0; i < n; ++i)
            cin >> m[i];

        uint64 y = 0,
               d = 0;

        for (uint64 i = 1; i < n; ++i)
        {
            if (m[i] < m[i - 1])
            {
                uint64 v = m[i - 1] - m[i];
                y += v;

                if (d < v)
                    d = v;
            }
        }

        uint64 z = 0;
        for (uint64 i = 0; i < n - 1; ++i)
        {
            if (m[i] < d)
                z += m[i];
            else
                z += d;
        }
            
        cout << "Case #" << cs << ": " << y << ' ' << z << "\n";
    }

    return 0;
}
