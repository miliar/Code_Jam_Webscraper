#include <iostream>
#include <fstream>
#include <iomanip>
typedef long double ld;

using namespace std;

ld DP[1000000][16];
ld P[16];

ld dp(int bm, int votes)
{
    if (votes < 0)
        return 0;
    if (DP[bm][votes] != -1)
        return DP[bm][votes];
    ld& res = DP[bm][votes];
    int smallbit = (bm & -bm);
    int smallid = 0; int sb = smallbit;
    int rest = (bm & ~smallbit);
    while (sb > 1)
    {
        smallid++;
        sb /= 2;
    }
    if (rest == 0)
    {
        if (votes > 1)
            return res = 0;
        else if (votes == 1)
            return res = P[smallid];
        else return res = 1 - P[smallid];
    }
    return res = (dp(rest, votes-1)*(P[smallid]) + dp(rest, votes)*(1-P[smallid]));
}

int main()
{
    //istream& in = cin;
    //ostream& out = cout;
    ifstream in("in.txt");
    ofstream out("out.txt");
    int T;
    in >> T;
    for (int t = 1; t <= T; t++)
    {
        int N, K;
        in >> N >> K;
        for (int i = 0; i < N; i++)
        {
            in >> P[i];
        }
        for (int i = 0; i < (1<<N); i++)
            for (int j = 0; j < N; j++)
                DP[i][j] = -1;
        ld res = 0;
        for (int i = 0; i < (1<<N); i++)
        {
            int b = __builtin_popcount(i);
            if (b == K)
                res = max(res, dp(i, b/2));
        }
        out << setprecision(9) << "Case #" << t << ": " << res << endl;
        /// TODO PREC!
    }
}
