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

using namespace std;

int q[4][4] =
{
    {1, 2, 3, 4},
    {2, -1, 4, -3},
    {3, -4, -1, 2},
    {4, 3, -2, -1}
};

int func(int a, int b)
{
    int c = 1;
    if (a * b < 0)
    {
        c *= -1;
    }

    if (a < 0)
    {
        a *= -1;
    }
    if (b < 0)
    {
        b *= -1;
    }
    
    a--;
    b--;

    return (c * q[a][b]);
}

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
    for (int j = 0; j < T; j++)
    {
        int X;
        fin >> X;
        int R;
        fin >> R;
        int C;
        fin >> C;

        string ans;
        if (X == 1)
        {
            ans = "GABRIEL";
        }
        else if (X == 2)
        {
            if (R * C % 2 == 1)
            {
                ans = "RICHARD";
            }
            else
            {
                ans = "GABRIEL";
            }
        }
        else if (X == 3)
        {
            if (R * C % 3 != 0)
            {
                ans = "RICHARD";
            }
            else if (R * C == 3)
            {
                ans = "RICHARD";
            }
            else
            {
                ans = "GABRIEL";
            }
        }
        else
        {
            if (R * C % 4 != 0)
            {
                ans = "RICHARD";
            }
            else if (R * C == 4 || R * C == 8)
            {
                ans = "RICHARD";
            }
            else
            {
                ans = "GABRIEL";
            }
        }

        fout << "Case #" << j+1 << ": " << ans << endl;
    }

    return (0);
}
