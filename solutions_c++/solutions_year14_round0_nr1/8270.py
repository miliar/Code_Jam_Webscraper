#include <iostream>
#include <fstream>
using namespace std;
ifstream fin ("input");
ofstream fout ("output");
int main()
{   int T,r1,r2,a1[5][5],a2[5][5],i,j,ok,val=0,t;
    fin>>T;
    t=T;
    while(T>0)
    {
        ok=0;val=0;
        fin>>r1;
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
                fin>>a1[i][j];

        fin>>r2;
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
                fin>>a2[i][j];

        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
                if(a1[r1][i]==a2[r2][j]) {ok++;if(val==0)val=a1[r1][i];}

        fout<<"Case #"<<t-T+1<<": ";
        if(ok==1) fout<<val;
            else if(ok==0) fout<<"Volunteer cheated!";
            else if(ok>1) fout<<"Bad magician!";
        fout<<endl;
        T--;
    }
    return 0;
}


