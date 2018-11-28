#include <iostream>
#include <fstream>

using namespace std;

int T,a1,a2,m1[4][4],m2[4][4],pos[4],psol,sol;

int main()
{
    ifstream f1("1.in");
    ofstream f2("1.out");
    f1>>T;
    for(int c=1;c<=T;c++)
    {
        f1>>a1;
        a1--;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                f1>>m1[i][j];
        for(int i=0;i<4;i++)
            pos[i]=m1[a1][i];
        f1>>a2;
        a2--;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                f1>>m2[i][j];
        psol=0;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                if(m2[a2][j]==pos[i])
                {
                    psol++;
                    sol=m2[a2][j];
                    break;
                }
        f2<<"Case #"<<c<<": ";
        if(psol==1)
            f2<<sol;
        else if(psol>1)
            f2<<"Bad magician!";
        else if(psol==0)
            f2<<"Volunteer cheated!";
        f2<<"\n";
    }
    return 0;
}
