//Lupu Constantin
//codejam contest
#include <iostream>
#include <fstream>
unsigned short t,x,y,a[5][5],b[5][5],i,j,k,contor,z;
using namespace std;
ifstream fin("A-small-attempt4.in");
ofstream fout("a4.out");
int main()
{fin>>t;
for(contor=1;contor<=t;contor++)
{
    fin>>x;
    for(i=1;i<=4;i++)
    for(j=1;j<=4;j++)
    fin>>a[i][j];
    fin>>y;
    for(i=1;i<=4;i++)
    for(j=1;j<=4;j++)
    fin>>b[i][j];
    k=0;z=0;
    for(i=1;i<=4;i++)
    {
        for(j=1;j<=4;j++)
        if(a[x][i]==b[y][j]){k++;z=a[x][i];  }
    }




     if(k==1)  fout<<"Case #"<<contor<<": " <<z<<'\n';
         else
         if(k>1)
           fout<<"Case #"<<contor<<": Bad magician!"<<'\n';
            else
             fout<<"Case #"<<contor<<": Volunteer cheated!"<<'\n';


}

  fin.close();fout.close();
    return 0;
}
