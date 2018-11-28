#include <fstream>
#include <queue>
#include <vector>

using namespace std;

ifstream f("test.in");
ofstream g("test.out");

const int KM = 101;
const int CM = 101;

typedef unsigned long long tlong;
vector<tlong> sol[KM+2][CM+2];
tlong pow[KM][CM];

tlong pos(int p, int k, int c)
{
    if (c == 1)
        return p;
    
    return 1ULL * (p-1) * (pow[k][c-1]) + pos(min(p+1, k), k, c-1);
}

int main()
{
    for (int K=1; K<KM; K++)
    {
        pow[K][0] = 1;
        for (int c=1; c<CM; c++)
            pow[K][c] = 1LL * K * pow[K][c-1];
    }
    
    for (int K=1; K<KM; K++)
        for (int C=1; C<CM; C++)
        {
            int p = 1;
            while (p <= K)
            {
                sol[K][C].push_back( pos(p, K, C) );
                p += C;
            }
            if (sol[K][C].size() > K)
            {
                g << "WRONG!!\n";
                return 0;
            }
        }
    
    int T;
    f >> T;
    for (int t=1; t<=T; t++)
    {
        g << "Case #" << t << ": ";
        int K, C, S;
        f >> K >> C >> S;
        if (sol[K][C].size() > S)
            g << "IMPOSSIBLE\n";
        else
        {
            for (tlong x : sol[K][C])
                g << x << ' ';
            g << '\n';
        }
    }
    
    f.close();
    g.close();
    
    
    return 0;
}