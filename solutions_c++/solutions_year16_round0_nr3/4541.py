#include <fstream>
#include <math.h>
using namespace std;
ifstream ka("C-small-attempt0.in");
ofstream ki("ceva.out");
int PUT_MAX, CATE_MAX;
long long t, put[11][16], raspunsuri[51][11];
int main()
{
    ka >> t >> PUT_MAX >> CATE_MAX;
    for(int r = 1; r <= t; r++)
    {
        ki << "Case #" << r << ":" << '\n';
        for(long long i = 2; i <= 10; i++)
            for(long long f = 0; f <= PUT_MAX - 1; f++)
                put[i][f] = pow(i, f);
        int i = (1 << (PUT_MAX - 1)) + 1;
        int gasite = 0;
        while(i < (1 << PUT_MAX) && gasite < CATE_MAX)
        {
            bool este_mare = true;
            for(int j = 2; j <= 10 && este_mare; j++)
            {
                bool este = false;
                long long t = 0;
                for(int f = PUT_MAX - 1; f >= 0; f--)
                    if((1 << f) & i)
                        t += put[j][f];
                if(t % 2 == 0)
                {
                    raspunsuri[gasite][j] = 2;
                    este = true;
                }
                else
                {
                    for(int d = 3; d <= sqrt(t) && !este; d += 2)
                    {
                        if(t % d == 0)
                        {
                            raspunsuri[gasite][j] = d;
                            este = true;
                        }
                    }
                }
                este_mare &= este;
            }
            if(este_mare)
            {
                for(int f = PUT_MAX - 1; f >= 0; f--)
                {
                    if((1 << f) & i)
                        ki << 1;
                    else
                        ki << 0;
                }
                ki << " ";
                for(int j = 2; j <= 10; j++)
                    ki << raspunsuri[gasite][j] << " ";
                ki << '\n';
                gasite++;
            }
            i += 2;
        }
    }
}
