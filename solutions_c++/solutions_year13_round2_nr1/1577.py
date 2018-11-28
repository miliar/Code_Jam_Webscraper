#include <algorithm>
#include <fstream>
#include <iostream>
#include <vector>

long solveProblemA(long a, std::vector<long> motes)
{
    long initialA = a;
    std::vector<long>::size_type n = motes.size();
    if (a <= 1) return n;

    long result = n;
    long current = n;
    long i = 0;

    while (i < n)
    {
        if (a > motes[i])
        {
            a += motes[i];
            ++i;
            --current;
        }
        else
        {
            while (a <= motes[i])
            {
                a += a - 1;
                ++current;
            }
        }

        if (result > current)
            result = current;
    }

    return result;
}

void problemA(std::ifstream& fin)
{
    std::ofstream fout("C:\\CodeJam\\problemA.out");

    int t = 0;
    fin >> t;

    for (int i = 1; i <= t; ++i)
    {
        long a = 0;
        int n = 0;
        fin >> a >> n;

        std::vector<long> motes;
        motes.reserve(n);

        for (int j = 0; j < n; ++j)
        {
            long mote = 0;
            fin >> mote;
            motes.push_back(mote);
        }

        std::sort(motes.begin(), motes.end());

        fout << "Case #" << i << ": " << solveProblemA(a, motes) << std::endl;
    }

    fout.close();
}
