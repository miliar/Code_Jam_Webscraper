#include <iostream>
#include <fstream>
#include <algorithm>
#include <stdio.h>
#define FOR(i,a,b) for(i=a;i<=b;i++)
#define bad "Bad magician!"
#define out "case #"
#define cheat "Volunteer cheated!"

using namespace std;

ifstream fin;
ofstream fout;

int main()
{
    int grid[5][5],t,ans,line[3][5],i,j,k,m,counter,number;

    fin.open("1.in",ios::in);

    fout.open("1_0.out");

    fin.seekg(0);

    fin>>t;

FOR(j,1,t)
{
    counter=0;
    FOR(k,1,2)
        {
            fin>>ans;

            FOR(i,1,4)
                FOR(m,1,4)
                    fin>>grid[i][m];

            FOR(i,1,4)
                line[k][i]=grid[ans][i];

            sort(line[k]+1,line[k]+5);
        }

    k=1;
    FOR(i,1,4)
    {
        while(line[1][i]>line[2][k])
            k++;
        if(line[1][i]==line[2][k])
        {number=line[1][i];counter++;}
    }

    fout<<out<<j<<':';
    if(counter==0) fout<<' '<<cheat;
    else if(counter==1) fout<<' '<<number;
    else if(counter>1) fout<<' '<<bad;
    fout<<'\n';
}
fin.close();
fout.close();
    return 0;
}
