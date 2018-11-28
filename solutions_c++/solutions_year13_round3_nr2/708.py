#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

string solveProblemB(long x, long y)
{
    string result;
    bool increase = true;

    if (x < 0)
    {
        increase = false;
        x = -x;
    }

    for (long i = 0; i < x; ++i)
        result += increase ? "WE" : "EW";

    increase = true;
    if (y < 0)
    {
        increase = false;
        y = -y;
    }

    for (long i = 0; i < y; ++i)
        result += increase ? "SN" : "NS";

    return result;
}

void problemB(std::ifstream& fin)
{
    std::ofstream fout("C:\\CodeJam\\problemB.out");

    int t = 0;
    fin >> t;

    for (int i = 1; i <= t; ++i)
    {
        long x, y;
        fin >> x >> y;
        fout << "Case #" << i << ": " << solveProblemB(x, y) << std::endl;
    }

    fout.close();
}
