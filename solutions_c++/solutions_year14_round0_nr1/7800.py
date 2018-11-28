#include <fstream>
#include <cstring>

using namespace std;

int x,a[5][5],test,v[20];

ifstream fin ("A-small-attempt3.in");
ofstream fout ("A-small-attempt3.out");

int main()
{
    fin>>test;

    for (int k=1; k<=test; ++k)
    {
        memset (v,0,sizeof(v));

        fin>>x;

        for (int i=1; i<=4; ++i)
            for (int j=1; j<=4; ++j)
            fin>>a[i][j];

        for (int j=1; j<=4; ++j)
        {
            v[a[x][j]]++;
        }

        fin>>x;

        for (int i=1; i<=4; ++i)
            for (int j=1; j<=4; ++j)
            fin>>a[i][j];

        for (int j=1; j<=4; ++j)
        {
            v[a[x][j]]++;
        }

        int cnt = 0, wh;

        for (int i=1; i<=16; ++i)
        {
            if (v[i] == 2)
                ++cnt,wh = i;
        }

        fout<<"Case #"<<k<<": ";

        if (cnt == 0)
            fout<<"Volunteer cheated!";
        else if (cnt == 1)
            fout<<wh;
        else fout<<"Bad magician!";
        fout<<"\n";
    }
}
