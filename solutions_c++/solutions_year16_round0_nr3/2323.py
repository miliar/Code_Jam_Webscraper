#include <iostream>
#include <fstream>
#include <string>

using namespace std;

ifstream fin ("A.in");
ofstream fout ("A.txt");

long long fget (int n, int b)
{
    long long x = 0;
    for (int i = 15; i >= 0; i--)
    {
        x *= b;
        if (n & (1 << i))
            x++;
    }
    return x;
}

int fval (long long x)
{
    for (int k = 2; k * (long long) k <= x; k++)
        if (x % k == 0)
            return k;
    return -1;
}

int res[11];

int main()
{
    fout << "Case #1:\n";
    
    int tot = 50;
    for (int i = (1 << 15) + 1; i < (1 << 16) && tot; i += 2)
    {
        bool bad = false;
        for (int j = 2; j <= 10; j++)
        {
            res[j] = fval (fget (i, j));
            if (res[j] == -1) bad = true;
        }
        
        if (!bad)
        {
            tot--;
            for (int j = 15; j >= 0; j--)
            {
                if (i & (1 << j))
                    fout << 1;
                else
                    fout << 0;
            }
            
            for (int j = 2; j <= 10; j++)
                fout << " " << res[j];
            fout << "\n";
        }
    }
    
    return 0;
}
