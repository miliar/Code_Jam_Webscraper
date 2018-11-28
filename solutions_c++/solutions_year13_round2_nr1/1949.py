#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

ifstream f("test.in");
ofstream g("test.out");

int N, T, i;
int ANS;
int aux;
long long A, B;
vector<long long> V;
long long X;

int main ()
{
    f >> T;
    for (int TI=1; TI<=T; TI++)
    {
        g << "Case #" << TI << ": ";

        A=0;
        V.clear();
        ANS=0;

        f >> A >> N;
        for (i=1; i<=N; i++)
        {
            f >> X;
            V.push_back(X);
        }

        sort(V.begin(), V.end());

        for (i=0; i<N; i++)
        {
            if (V[i]<A)
            {
                A+=V[i];
                continue;
            }
            aux=0;
            B=A;
            if (B==1)
                aux=999999999;
            else
                while (B<=V[i])
                {
                    B+=B-1;
                    aux++;
                }
            if (aux<=N-i-1)
            {
                A=B+V[i];
                ANS+=aux;
                continue;
            }
            ANS++;
        }

        g << ANS << '\n';
    }

    f.close();
    g.close();

    return 0;
}
