#include <fstream>

const int NMAX = 10000006;
const int inf = 0x3f3f3f3f;

using namespace std;

ifstream f("test.in");
ofstream g("test.out");

int T,N;
long long d[NMAX];

int minim(int a, int b)
{
    if (a < b)
        return a;
    return b;
}

int main()
{
    f >> T;
    for (int t = 1; t <= T; ++t)
    {
        f >> N;
        d[1] = 1;
        for (int i = 2; i <= N; ++i)
        {
            int invers = 0;
            int aux = i;
            d[i] = inf;
            d[i] = minim(d[i],d[i-1]+1);
            while (aux)
            {
                invers = invers*10 + aux%10;
                aux /= 10;
            }
            if (i % 10 != 0 && invers < i)
                d[i] = minim(d[i],d[invers]+1);
        }
        g << "Case #" << t << ": " << d[N] <<'\n';
    }

    f.close();
    g.close();
    return 0;
}
