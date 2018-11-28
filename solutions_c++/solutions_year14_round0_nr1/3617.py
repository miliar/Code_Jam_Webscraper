#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    ifstream fin;
    fin.open("abc.txt");
    ofstream fout;
    fout.open("ans.txt");
    int test;
    fin>>test;
    for(int u=1;u<=test;u++)
    {
        int first;
        fin>>first;
        first--;
        int a[4][4];
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
                fin>>a[i][j];
        }
        int second;
        fin>>second;
        second--;
        int b[4][4];
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
                fin>>b[i][j];
        }
        int count=0;
        int element=0;
        for(int i=0;i<4;i++)
        {
            int check=a[first][i];
            for(int j=0;j<4;j++)
            {
                if(check==b[second][j])
                {
                    count++;
                    element=check;
                }
            }
        }
        if(count==1)
        {
            fout<<"Case #"<<u<<": "<<element<<"\n";
        }
        else if(count==0)
        {
            fout<<"Case #"<<u<<": Volunteer cheated!"<<"\n";
        }
        else
        {
            fout<<"Case #"<<u<<": Bad magician!"<<"\n";
        }
    }
    return 0;
}
