#include<iostream>
#include<fstream>
using namespace std;
int a[4][4], b[4][4];
int main()
{
    int i, j1, j2, N, y1, y2, f1=0, f2=0;
    ifstream fin;
    ofstream fout;
    fin.open("cj_magic_trick_small.in", ios::in);
    fout.open("cj_magic_trick_small.txt", ios::app);
    fin>>N;
    fin.seekg(4);
    for(i=0; i<N; i++)
    {
        fin>>y1;
        for(j1=0; j1<4; j1++)
        {
            for(j2=0; j2<4; j2++)
            {
                fin>>a[j1][j2];
            }
        }
        fin>>y2;
        for(j1=0; j1<4; j1++)
        {
            for(j2=0; j2<4; j2++)
            {
                fin>>b[j1][j2];
            }
        }
        --y1;
        --y2;
        for(j1=0; j1<4; j1++)
        {
            for(j2=0; j2<4; j2++)
            {
                if(a[y1][j1]==b[y2][j2])
                {
                    if(f1==0)
                    {
                        f1=a[y1][j1];
                        break;
                    }
                    if(f1!=0)
                    {
                        f2=a[y1][j2];
                        break;
                    }
                }
            }
            if(f2!=0)
                break;
        }
        fout<<"Case #"<<i+1<<": ";
        if(f1==0 && f2==0)
        {
            fout<<"Volunteer cheated!";
        }
        else if(f1!=0 && f2!=0)
        {
            fout<<"Bad magician!";
        }
        else
        {
            fout<<f1;
        }
        fout<<endl;
        f1=0;
        f2=0;
    }
    fin.close();
    fout.close();
    return 0;
}
