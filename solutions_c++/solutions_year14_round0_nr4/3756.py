#include <cstdio>
#include <set>

using namespace std;

int solveWar(set<double> A, set<double> B)
{
    int sol = 0;
    set<double>::iterator itB;

    for (set<double>::iterator itA = A.begin(); itA != A.end(); itA++)
    {
        if ((itB = B.lower_bound(*itA)) != B.end())
        {
            sol++;
            B.erase(itB);
        }
        else
        {
            B.erase(B.begin());
        }
    }

    return sol;
}

int main()
{
    FILE *fin = fopen("D-large.in", "r");
    FILE *fout = fopen("D-large.out", "w");
    set<double> A;
    set<double> B;
    int t, n;
    double tmp;

    fscanf(fin, "%d", &t);

    for (int i = 1; i <= t; i++)
    {
        A.erase(A.begin(), A.end());
        B.erase(B.begin(), B.end());

        fscanf(fin, "%d", &n);

        for (int j = 0; j < n; j++)
        {
            fscanf(fin, "%lf", &tmp);
            A.insert(tmp);
        }

        for (int j = 0; j < n; j++)
        {
            fscanf(fin, "%lf", &tmp);
            B.insert(tmp);
        }

        fprintf(fout, "Case #%d: %d %d\n", i, solveWar(B, A), n - solveWar(A, B));
    }

    fclose(fin);
    fclose(fout);
    return 0;
}
