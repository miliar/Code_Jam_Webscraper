#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

int main()
{
    int T, N;
    int res1, res2;
    ifstream input ("input.in");
    if (input.is_open())
    {
        ofstream output ("output.out");
        input >> T;
        for (int i = 0; i < T; i++)
        {
            int m, n;
            res1 = res2 = 0;
            input >> N;
            int* mi = new int[N];
            input >> m;
            mi[0] = m;
            int maxdif = 0;
            for (int j = 1; j < N; j++)
            {
                input >> n;
                mi[j] = n;
                if (n < m)
                {
                    res1 += m - n;
                    if (m - n > maxdif)
                        maxdif = m - n;
                }
                m = n;
            }
            for (int j = 0; j < N - 1; j++)
            {
                if (mi[j] > maxdif)
                {
                    res2 += maxdif;
                }
                else
                    res2 += mi[j];
            }
            output << "Case #" << i + 1 << ": " << res1 << " " << res2 << endl;
        }
    input.close();
    output.close();
    }
    return 0;
}

