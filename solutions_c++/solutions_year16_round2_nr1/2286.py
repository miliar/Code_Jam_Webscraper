#include <iostream>
#include <fstream>
#include <inttypes.h>
#include <cmath>
#include <string>
#include <cstdlib>

using namespace std;

int main()
{
    int64_t i, j, k, T, z, w, x, r, f, v, g, h, io, o;
    char junk, array[2001];
    ifstream filin;
    ofstream filout;
    filin.open ("input.txt");
    filout.open ("output.txt");
    filin >> T;
    for (i = 0; i < T; i++)
    {
        filout << "Case #" << i + 1 << ": ";
        z = w = x = r = f = v = g = h = io = o = 0;
        filin >> array;
        for (j = 0; array[j] != '\0'; j++)
        {
            if (array[j] == 'Z')
                z++;
            if (array[j] == 'W')
                w++;
            if (array[j] == 'X')
                x++;
            if (array[j] == 'R')
                r++;
            if (array[j] == 'F')
                f++;
            if (array[j] == 'V')
                v++;
            if (array[j] == 'G')
                g++;
            if (array[j] == 'H')
                h++;
            if (array[j] == 'I')
                io++;
            if (array[j] == 'O')
                o++;
        }
        for (k = 0; k < z; k++)
            filout << "0";
        for (k = 0; k < (o - z - w - r + h - g + z); k++)
            filout << "1";
        for (k = 0; k < w; k++)
            filout << "2";
        for (k = 0; k < h - g; k++)
            filout << "3";
        for (k = 0; k < r - h + g - z; k++)
            filout << "4";
        for (k = 0; k < f - r + h - g + z; k++)
            filout << "5";
        for (k = 0; k < x; k++)
            filout << "6";
        for (k = 0; k < v - f + r - h + g - z; k++)
            filout << "7";
        for (k = 0; k < g; k++)
            filout << "8";
        for (k = 0; k < io - g - x - f + r - h + g - z; k++)
            filout << "9";
        filout << endl;
    }
    filin.close ();
    filout.close ();
    return 0;
}
