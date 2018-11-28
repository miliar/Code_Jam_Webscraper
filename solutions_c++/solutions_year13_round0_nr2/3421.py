#include <fstream>
#include <cstring>
#define NM 110

using namespace std;

ifstream f("test.in");
ofstream g("test.out");

int T, TI;
int N, M;
int A[NM][NM];

bool Line (int i, int x)
{
    for (int j=1; j<=M; j++)
        if (A[i][j]>x)
            return 1;

    return 0;
}

bool Column (int j, int x)
{
    for (int i=1; i<=N; i++)
        if (A[i][j]>x)
            return 1;

    return 0;
}

bool Solve ()
{
    for (int i=1; i<=N; i++)
        for (int j=1; j<=M; j++)
            if (Line(i, A[i][j]) && Column(j, A[i][j]))
                return 0;

    return 1;
}

int main ()
{
    f >> T;
    for (TI=1; TI<=T; ++TI)
    {
        g << "Case #" << TI << ": ";

        f >> N >> M;
        for (int i=1; i<=N; i++)
            for (int j=1; j<=M; j++)
                f >> A[i][j];

        if (Solve())
            g << "YES";
        else
            g << "NO";
        g << '\n';
    }

    f.close();
    g.close();

    return 0;
}
