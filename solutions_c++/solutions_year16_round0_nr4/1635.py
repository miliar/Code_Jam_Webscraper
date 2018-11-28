#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    int T;
    fin >> T;

    for (auto t = 0;t < T; t++)
    {
        int K, C, S;
        fin >> K >> C >> S;

        uint64_t step = 1;
        for (auto i = 1; i < C; i++)
            step = step*K + 1;


        fout << "Case #" << (t+1) << ": ";
        uint64_t index = 1;
        for (auto i = 0; i < S; i++)
        {
            fout << index;
            index += step;
            if (i < S-1)
                fout << " ";
        }
        fout << endl;
    }

    return 0;
}