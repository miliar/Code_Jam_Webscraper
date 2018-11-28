#include <fstream>
using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

int a[4][4];
int b[4][4];

int main()
{
    int i,j,n,m,l,k;
    int t,tt;
    fin>>tt;
    for(t=1; t<=tt; ++t)
    {
        fin>>n;
        for(i=0; i<4; ++i)
            for(j=0; j<4; ++j)
                fin>>a[i][j];

        fin>>m;
        for(i=0; i<4; ++i)
            for(j=0; j<4; ++j)
                fin>>b[i][j];

        k = 0;
        for(i=0; i<4; ++i)
            for(j=0; j<4; ++j)
                if(a[n-1][i] == b[m-1][j])
                {
                    ++k;
                    l = a[n-1][i];
                }

        fout << "Case #"<<t<<": ";
        if(k == 1)
            fout << l << endl;
        else if(k==0)
            fout << "Volunteer cheated!" << endl;
        else
           fout << "Bad magician!" << endl; 


    }
    return 0;
}
