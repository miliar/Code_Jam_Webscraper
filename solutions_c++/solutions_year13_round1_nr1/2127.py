#include <cstdio>
#include <vector>
#include <deque>
#include <queue>
#include <map>
#include <algorithm>
#include <functional>
#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <string.h>
#define _USE_MATH_DEFINES
#include <math.h>
#include <sstream>
#include <stack>

using namespace std;

int main(int argc, const char **argv)
{
    if (argc != 2)
    {
        fprintf(stderr, "Error:%d\n", __LINE__);
        return -1;
    }

    ifstream fin(argv[1]);
    ofstream fout("out.txt");

    int T;
    fin >> T;

    for (int tc = 0; tc < T; tc++)
    {
        int r, t;
        fin >> r >> t;

        int ret = 0;

        int z = 3;
        if (r % 2 == 0)
        {
            z = 1;
        }

        for (; r > 1; r -= 2)
        {
            t += 2 * (r-1) - 1;
            ret--;
        }

        int i = 0;
        for (; t >= (4 * i) + z; ret++, i++)
        {
            t -= (4 * i) + z;
        }

        fout << "Case #" << tc+1 << ": " << ret << endl;
    }

    return (0);
}
