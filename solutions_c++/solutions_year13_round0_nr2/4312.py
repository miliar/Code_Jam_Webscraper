#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream infile("q2.in");
    ofstream outfile("q2.out");
    unsigned int T;
    infile >> T;
    cout << T << "\n";
    for (unsigned int i = 0; i<T; i++)
    {
        unsigned short arr[150][150];
        unsigned short N,M;
        infile >> N >> M;
        for (unsigned short n=0;n<N;n++)
            for (unsigned short m=0;m<M;m++)
                infile >> arr[n][m];
        unsigned short maxn[150]={0}, maxm[150]={0};
        for (unsigned short n=0;n<N;n++)
            for (unsigned short m=0;m<M;m++)
            {
                if (maxn[n]<arr[n][m])
                    maxn[n] = arr[n][m];
                if (maxm[m]<arr[n][m])
                    maxm[m] = arr[n][m];
            }
        unsigned short yes = 1;
        for (unsigned short n=0;n<N &&yes;n++)
            for (unsigned short m=0;m<M && yes;m++)
            {
                yes &= ((arr[n][m]==maxm[m]) || (arr[n][m]==maxn[n]));
            }
        outfile << "Case #" << i+1 << ": " << (yes?"YES":"NO") << "\n";
    }
    infile.close();
    outfile.close();
    return 0;
}
