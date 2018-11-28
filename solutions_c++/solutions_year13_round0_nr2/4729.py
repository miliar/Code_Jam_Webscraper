#include <iostream>
#include <fstream>
using namespace std;

int T, N, M;
int tab[105][105];
int bc[105], bl[105];

bool isGood()
{
    for (int i=0; i<N; ++i)
        for (int j=0; j<M; ++j)
            if (tab[i][j] < bl[i] &&
                tab[i][j] < bc[j])
                return false;
    return true;
}

int main()
{
    ifstream inp("B-large.in");
    ofstream outp("lawn.out");

    inp >> T;
    for (int rep=1; rep<=T; ++rep)
    {
        inp >> N >> M;

        for (int i=0; i<N; ++i)
            for (int j=0; j<M; ++j)
                inp >> tab[i][j];

        for (int i=0; i<N; ++i)
        {
            bl[i]=0;
            for (int j=0; j<M; ++j)
                if (tab[i][j]>bl[i])
                    bl[i]=tab[i][j];
        }

        for (int j=0; j<M; ++j)
        {
            bc[j]=0;
            for (int i=0; i<N; ++i)
                if (tab[i][j]>bc[j])
                    bc[j]=tab[i][j];
        }

        /*
        for (int i=0; i<N; ++i)
        {
            for (int j=0; j<M; ++j)
                printf("%3d", tab[i][j]);
            printf("\n");
        }
        printf("--------------------------\n");
        for (int i=0; i<N; ++i)
            printf("%3d", bl[i]);
        printf("\n");
        for (int i=0; i<M; ++i)
            printf("%3d", bc[i]);
        cin.get();
        */

        if (rep > 1) outp << endl;
        outp << "Case #" << rep << ": ";
        if (isGood())
            outp << "YES";
        else
            outp << "NO";
    }
}
