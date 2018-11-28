#include <iostream>
#include <cstdio>
#define f cin
#define g cout
#include <cmath>
#include <iomanip>

using namespace std;

int N;
double V, X;
double R[110], C[110];

double EPS = 1e-9;
bool equals (double a, double b)
{
    return fabs(a-b)<EPS;
}

int main()
{
    #ifndef ONLINE_JUDGE
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    #endif

    int T;
    f >> T;

    for (int t=1; t<=T; t++)
    {
        g << "Case #" << t << ": ";

        f >> N >> V >> X;
        for (int i=1; i<=N; i++)
            f >> R[i] >> C[i];

        if (N==1)
        {
            if (equals(X, C[1]))
                g << fixed << setprecision(10) << (V/R[1]) << '\n';
            else
                g << "IMPOSSIBLE\n";
        }
        else
        {
            if (equals(C[1], C[2]))
            {
                if (equals(X, C[1]))
                    g << fixed << setprecision(10) << (V/(R[1]+R[2])) << '\n';
                else
                    g << "IMPOSSIBLE\n";
            }
            else
            {
                if (min(C[1], C[2])-EPS <= X && X <= max(C[1], C[2])+EPS)
                {
                    double t2 = (V*X - V*C[1]) / (R[2]*C[2]-R[2]*C[1]);
                    double t1 = (V - R[2]*t2) / R[1];


                    if (t1<-EPS || t2<-EPS)
                        g << "IMPOSSIBLE\n";
                    else
                        g << fixed << setprecision(10) << max(t1, t2) << '\n';
                }
                else
                    g << "IMPOSSIBLE\n";
            }
        }
    }

    return 0;
}
