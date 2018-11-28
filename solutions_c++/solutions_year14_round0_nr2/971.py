#include <cstdio>
#include <fstream>
#include <iostream>
#include <vector>

#define INF 999999999999999

using namespace std;

ifstream fin("b.in");
FILE *fout = fopen("b.out", "w");

double Cost, Prod, Goal;
int T;

int main()
{
    fin >> T;

    for(int j = 1; j <= T; j++)
    {
        fin >> Cost >> Prod >> Goal;
        double c = 0, earn = 2, t = 0, res = INF;

        for(int i = 0; i <= 10000000; i++)
        {
            res = min(res, t + Goal / earn);
            t += Cost / earn;
            earn += Prod;
        }

        fprintf(fout, "Case #%d: %.12f\n", j, res);
    }
}
