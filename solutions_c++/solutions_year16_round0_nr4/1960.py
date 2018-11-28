#include <iostream>
#include <fstream>
#include <unordered_map>
#include <cstring>

using namespace std;

unsigned long long T, K, C, S;

int main()
{
    ifstream fin("D-small.in");
    ofstream fout("D-small.out");
    fin >> T;
    for (unsigned long long i = 0; i < T; ++ i)
    {
        fin >> K >> C >> S;
        fout << "Case #" << i + 1 << ": ";
        unsigned long long least = K / C;
        if (K % C != 0) least ++;
        if (S < least)
        {
            fout << "IMPOSSIBLE" << endl;
        }
        else
        {
            for (int j = 0; j < K; ++ j)
            {
                fout << j + 1 << ' ';
            }
//            unsigned long long interval = 1;
//            for (unsigned long long j = 0; j < C - 1; ++ j)
//            {
//                interval *= K;
//            }
//            for (unsigned long long j = 0; j < least; ++ j)
//            {
//                unsigned long long pos = j * C * interval;
//                unsigned long long term = 1;
//                unsigned long long M = C - 1;
//                if (M > K - 1) M = K - 1;
//                for (unsigned long long k = 0; k < M; ++ k)
//                {
//                    pos += (M - k) * term;
//                    term *= K;
//                }
//                fout << pos + 1;
//                if (j < least - 1)
//                {
//                    fout << ' ';
//                }
//            }
            fout << endl;
        }
    }
    return 0;
}
