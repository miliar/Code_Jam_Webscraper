#include <iostream>
#include <fstream>

using namespace std;

ifstream fin("MagicTrick.in");
ofstream fout("MagicTrick.out");

int a[6][6],b[6][6],nr,nra,nrb;

void citire()
{
    fin>>nra;
    for(int i=1;i<5;i++)
        for(int j=1;j<5;j++)
            fin>>a[i][j];
    fin>>nrb;
    for(int i=1;i<5;i++)
        for(int j=1;j<5;j++)
            fin>>b[i][j];
}

void rezolvare()
{
    int nrx=0,y;
    for(int i=1;i<5;i++)
        for(int j=1;j<5;j++)
        if(a[nra][i]==b[nrb][j])
        {
            nrx++;
            y=a[nra][i];
        }
    if(nrx==1)
        fout<<y;
    if(nrx>1)
        fout<<"Bad magician!";
    if(nrx==0)
        fout<<"Volunteer cheated!";
}

int main()
{
fin>>nr;
for(int i=1;i<=nr;i++)
{
    citire();
    fout<<"Case #"<<i<<": ";
    rezolvare();
    fout<<endl;
}
    return 0;
}
