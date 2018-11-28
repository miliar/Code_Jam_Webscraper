#include <iostream>
#include <fstream>
#include <unordered_map>
#include <cstring>

using namespace std;

int T, N, J;

int main()
{
    ifstream fin("C-large.in");
    ofstream fout("C-large.out");
    fin >> T;
    for (int i = 0; i < T; ++ i)
    {
        fin >> N >> J;
        fout << "Case #" << i + 1 << ": " << endl;
        int num = 1;
        bool finish = false;
        for (int j = 1; j < N - 1; j += 2)
        {
            if (num > J) break;
            for (int k = 2; k < N - 1; k += 2)
            {
                if (num > J) break;
                for (int p = j + 2; p < N - 1; p += 2)
                {
                    if (num > J) break;
                    for (int q = k + 2; q < N - 1; q += 2)
                    {
                        if (num > J) break;
                        num += 1;
                        for (int r = 0; r < N; ++ r)
                        {
                            if (r == 0 || r == N - 1 || r == j || r == k || r == p || r == q)
                            {
                                fout << 1;
                            }
                            else
                            {
                                fout << 0;
                            }
                        }
                        fout << " 3 2 3 2 7 2 3 2 3\n";
                    }
                }
            }
        }
    }
    return 0;
}

