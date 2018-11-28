#include <fstream>
#include <iostream>

using namespace std;

int main()
{
    ifstream fin("B-large.in");
    ofstream fout("B-large.out");
    int T;
    fin >> T;
    int N,M;
    bool possible;
    for (int x=1;x<=T;x++)
    {
        possible=true;
        fin >> N >> M;
        int lawn[N][M];
        int lawn2[N][M];
        int columns[N];
        int rows[M];

        for (int n=0;n<N;n++)
            columns[n]=0;

        for (int m=0;m<M;m++)
            rows[m]=0;

        for (int n=0;n<N;n++)
            for (int m=0;m<M;m++)
                {
                    fin >> lawn[n][m];
                    lawn2[n][m]=100;
                }

        for (int n=0;n<N;n++)
            for (int m=0;m<M;m++)
            if (columns[n]<lawn[n][m]) columns[n]=lawn[n][m];

        for (int m=0;m<M;m++)
            for (int n=0;n<N;n++)
            if (rows[m]<lawn[n][m]) rows[m]=lawn[n][m];

        for (int n=0;n<N;n++)
            for (int m=0;m<M;m++)
                if (columns[n]<rows[m]) lawn2[n][m]=columns[n];
                else lawn2[n][m]=rows[m];

        for (int n=0;n<N;n++)
            for (int m=0;m<M;m++)
                if (lawn[n][m]!=lawn2[n][m]) possible=false;

        if (possible) fout << "Case #" << x << ": YES" << endl;
        else fout << "Case #" << x << ": NO" << endl;
    }
    return 0;
}
