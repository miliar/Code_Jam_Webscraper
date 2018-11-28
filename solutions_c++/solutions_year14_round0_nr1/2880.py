#include<fstream>
using namespace std;
ifstream fin ("temp.in");
ofstream fout ("temp.out");
int first [4][4];
int second [4][4];
int main ()
{
    int t;
    fin>>t;
    int i;
    int x,y;
    for (i=1;i<=t;i++)
    {
        fout<<"Case #"<<i<<": ";
        int a;
        fin>>a;
        a-=1;
        for (x=0;x<4;x++)
            for (y=0;y<4;y++)
                fin>>first[x][y];
        int b;
        fin>>b;
        b-=1;
        for (x=0;x<4;x++)
            for (y=0;y<4;y++)
                fin>>second[x][y];
        int number=-1;
        for (x=0;x<4;x++)
            for (y=0;y<4;y++)
                if (first[a][x]==second[b][y])
                    if (number==-1) number=first[a][x];
                    else number=0;
        if (number>0) fout<<number<<endl;
        else if (number==0) fout<<"Bad magician!"<<endl;
             else fout<<"Volunteer cheated!"<<endl;
    }
    return 0;
}
