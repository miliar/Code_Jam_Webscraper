#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream fin;
    ofstream fout;
    fin.open("A-small-attempt0.in");
    fout.open("op1.txt");
    int a[4][4], b[4][4], tc, p1, p2, s, i, j, k=0, val;
    fin>>tc;
    while(tc--)
    {
        s=0;
        k++;
        fin>>p1;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
            fin>>a[i][j];
        fin>>p2;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
            fin>>b[i][j];

        for(i=0;i<4;i++){
            for(j=0;j<4;j++)
                if(a[p1-1][i]==b[p2-1][j]){
                   if(s==0){s=1;val=a[p1-1][i];}
                   else if(s==1)s=2;
                   else;
                }
                if(s==2)break;}

        if(s==2)
            fout<<"Case #"<<k<<": Bad magician!\n";
        else if(s==1)
            fout<<"Case #"<<k<<": "<<val<<"\n";
        else if(s==0)
            fout<<"Case #"<<k<<": Volunteer cheated!\n";
        else;
}

    return 0;
}
