#include <iostream>
#include <fstream>

using namespace std;

ifstream fin ("A.in");
ofstream fout ("A.txt");

int main()
{
    int T; fin >> T;
    for (int t = 1; t <= T; t++)
    {
        int N;
        fin >> N;
        
        bool x[10];
        for (int i = 0; i < 10; i++)
            x[i] = false;
        
        fout << "Case #" << t << ": ";
        
        int xc = 0;
        for (int i = 1; i <= 10000; i++)
        {
            long long k = N * (long long) i;
            while (k)
            {
                int p = k % 10;
                if (!x[p])
                {
                    x[p] = true;
                    xc++;
                }
                k /= 10;
            }
            
            if (xc == 10)
            {
                fout << N * (long long) i << "\n";
                break;
            }
        }
        if (xc < 10)
            fout << "INSOMNIA\n";
    }
    return 0;
}
