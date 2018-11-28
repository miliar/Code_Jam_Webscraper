#include <fstream>
#include <cstring>
using namespace std;

#define in "test.in"
#define out "test.out"

ifstream f(in);
ofstream g(out);

int T, L1, L2, First[10][10], Second[10][10], FR[18];

int main()
{
    f >> T;
    for(int i = 1; i <= T; ++i) {
        f >> L1;
        for(int t = 1; t <= 4; ++t)
            for(int tt = 1; tt <= 4; ++tt)  f >> First[t][tt];
        f >> L2;
        for(int t = 1; t <= 4; ++t)
            for(int tt = 1; tt <= 4; ++tt) f >> Second[t][tt];
        for(int t = 1; t <= 4; ++t) FR[ First[L1][t] ] ++;
        for(int t = 1; t <= 4; ++t) FR[ Second[L2][t] ] ++;
        int ok = 0, nbr = -1;
        for(int t = 1; t <= 16; ++t)    {
            if(FR[t] == 2 && !ok)  ok = 1, nbr = t;
            else
            if(FR[t] == 2 && ok)   {
                ok = 2;
                t = 20;
            }
        }

        if(ok == 0) g << "Case #" << i << ": Volunteer cheated!";
        else
        if(ok == 1) g << "Case #" << i << ": " << nbr;
        else
        if(ok == 2) g << "Case #" << i << ": Bad magician!";
        if(i < T)  {
            g << '\n';
            memset(FR, 0, sizeof(FR));
        }
    }

    return 0;
}
