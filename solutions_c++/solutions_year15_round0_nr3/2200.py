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
        int L;
        fin >> L;
        int X;
        fin >> X;
        string S;
        fin >> S;

        string str;
        for (int i = 0; i < X; i++)
        {
            str += S;
        }

        int a[10000] = {0};
        int b[10000] = {0};
        int c[10000] = {0};
        int d[10000] = {0};
        for (int i = 0; i < L * X; i++)
        {
            switch (str[i])
            {
            case 'i':
                a[i] = 2;
                break;
            case 'j':
                a[i] = 3;
                break;
            case 'k':
                a[i] = 4;
                break;
            }
            b[i] = a[i];
        }

        d[L*X-1] = a[L*X-1];
        for (int i = 0; i < L * X - 1; i++)
        {
            d[L*X-1 - i - 1] = func(a[L*X-1 - i - 1], d[L*X-1 - i]);
        }

        string ans = "NO";
        for (int i = 0; (i < L * X - 1) && (ans == "NO"); i++)
        {
            if (b[i] == 2)
            {
                for (int x = 0; x < L * X; x++)
                {
                    c[x] = a[x];
                }

                for (int k = i + 1; k < L * X - 1; k++)
                {
                    if (c[k] == 3)
                    {
                        //for (int m = k + 1; m < L * X - 1; m++)
                        //{
                        //    c[m+1] = func(c[m], a[m+1]);
                        //}

                        //if (c[L*X-1] == 4)
                        if (d[k+1] == 4)
                        {
                            ans = "YES";
                            break;
                        }
                    }
                    c[k+1] = func(c[k], a[k+1]);
                }
            }
            b[i+1] = func(b[i], a[i+1]);
        }

        fout << "Case #" << j+1 << ": " << ans << endl;
    }

    return (0);
}
