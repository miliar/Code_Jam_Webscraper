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

int main(int argc, const char **argv)
{
    if (argc != 2)
    {
        fprintf(stderr, "Error:%d\n", __LINE__);
        return -1;
    }

    ifstream fin(argv[1]);
    ofstream fout("out.txt");

    int f;

    int T;
    fin >> T;
    for (int j = 0; j < T; j++)
    {
        int R, C, W;
        fin >> R >> C >> W;

        int ans = C;
        switch (C)
        {
        case 4:
        {
            switch (W)
            {
            case 2:
            {
                ans = 3;
                break;
            }
            }
            break;
        }
        case 5:
        {
            switch (W)
            {
            case 2:
            case 3:
            {
                ans = 4;
                break;
            }
            }
            break;
        }
        case 6:
        {
            switch (W)
            {
            case 2:
            case 3:
            {
                ans = 4;
                break;
            }
            case 4:
            {
                ans = 5;
                break;
            }
            }
            break;
        }
        case 7:
        {
            switch (W)
            {
            case 2:
            case 3:
            case 4:
            {
                ans = 5;
                break;
            }
            case 5:
            {
                ans = 6;
                break;
            }
            }
            break;
        }
        case 8:
        {
            switch (W)
            {
            case 2:
            case 3:
            case 4:
            {
                ans = 5;
                break;
            }
            case 5:
            {
                ans = 6;
                break;
            }
            case 6:
            {
                ans = 7;
                break;
            }
            }
            break;
        }
        case 9:
        {
            switch (W)
            {
            case 3:
            {
                ans = 5;
                break;
            }
            case 2:
            case 4:
            case 5:
            {
                ans = 6;
                break;
            }
            case 6:
            {
                ans = 7;
                break;
            }
            case 7:
            {
                ans = 8;
                break;
            }
            }
            break;
        }
        case 10:
        {
            switch (W)
            {
            case 2:
            case 3:
            case 4:
            case 5:
            {
                ans = 6;
                break;
            }
            case 6:
            {
                ans = 7;
                break;
            }
            case 7:
            {
                ans = 8;
                break;
            }
            case 8:
            {
                ans = 9;
                break;
            }
            }
            break;
        }
        }

        fout << "Case #" << j+1 << ": " << ans << endl;
    }

    return (0);
}
