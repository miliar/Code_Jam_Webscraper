#include <fstream>
#include <cstring>
using namespace std;
ifstream fin("f.in");
ofstream fout("f.out");
int nr, a[5][5], x, t;
bool mark[17];

int main()
{
    fin>>t;
    for(int k=1; k<=t; k++)
    {
        int sol=0;
        nr=0;
        memset(mark,0,sizeof(mark));
        fin>>x;
        for(int i = 1; i<= 4; i++)
        {
            for(int j = 1; j<= 4; j++ )
            {
                fin>>a[i][j];
            }
        }
        for(int i = 1; i<= 4; i++ )
            mark[a[x][i]]=1;
        fin>>x;
        for(int i = 1; i<= 4; i++ )
            for(int j = 1; j<= 4; j++ )
                fin>>a[i][j];
        for(int i = 1; i<= 4; i++ )
            if(mark[a[x][i]])
            {
                sol=a[x][i];
                nr++;
            }
        if(nr==1)
            fout<<"Case #"<<k<<": "<<sol<<'\n';
        else if(nr==0)
            fout<<"Case #"<<k<<": Volunteer cheated!\n";
        else if(nr>1)
            fout<<"Case #"<<k<<": Bad magician!\n";

    }
    fin.close();
    fout.close();
    return 0;
}
