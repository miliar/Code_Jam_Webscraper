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
        int s_max;
        fin >> s_max;
        int a;
        fin >> a;

        int friends = 0;
        int b[1000] = {0};
        int c[1000] = {0};

        for (int i = 0; i <= s_max; i++)
        {
            b[s_max - i] = a % 10;
            a = a / 10;
        }

        c[0] = b[0];
        for (int i = 0; i < s_max; i++)
        {
            c[i + 1] = b[i + 1] + c[i];
        }

//        for (int i = 0; i <= s_max; i++)
//        {
////            fout << b[i] << " ";
//            fout << c[i] << " ";
//        }

        int sum = 0;
        for (int i = 1; i <= s_max; i++)
        {
            int d = i - c[i - 1];
            if (d > friends)
            {
                friends = d;
            }
        }

        fout << "Case #" << j+1 << ": " << friends << endl;
    }

    return (0);
}
