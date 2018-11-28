#include <fstream>
#define NM 10000010

using namespace std;

ifstream f("test.in");
ofstream g("test.out");

int T, TI;
long long A, B, N;
long long a, b;
long long V[NM];
int C[20];

bool pal (long long x)
{
    C[0]=0;
    while (x)
    {
        C[++C[0]]=x%10;
        x/=10;
    }

    for (int i=1; i<=C[0]; i++)
        if (C[i]!=C[C[0]-i+1])
            return 0;

    return 1;
}

void Build ()
{
    for (long long i=1; i<=NM-10; i++)
        if (pal(i) && pal(1LL*i*i))
            V[++N]=1LL*i*i;
}

long long SearchLeft (int X)
{
    long long P=1, U=N, ANS=N+1, M;

    while (P<=U)
    {
        M=(P+U)/2;

        if (V[M]>=X)
        {
            ANS=M;
            U=M-1;
        }
        else
            P=M+1;
    }

    return ANS;
}

long long SearchRight (int X)
{
    long long P=1, U=N, ANS=0, M;

    while (P<=U)
    {
        M=(P+U)/2;

        if (V[M]<=X)
        {
            ANS=M;
            P=M+1;
        }
        else
            U=M-1;
    }

    return ANS;
}

int main ()
{
    Build();

    f >> T;
    for (TI=1; TI<=T; TI++)
    {
        g << "Case #" << TI << ": ";
        f >> A >> B;
        a=SearchLeft(A);
        b=SearchRight(B);

        if (a<=b)
            g << b-a+1;
        else
            g << 0;

        g << '\n';
    }

    f.close();
    g.close();

    return 0;
}
