#include<iostream>
#include<stdio.h>
#include<fstream>

using namespace std;

int main()
{
    ifstream fin;
    fstream fout;
    fin.open("input.txt",ios::in);
    fout.open("output.out",ios::out);
    int T, x, y,i,j, a1[4][4], a2[4][4], arr[17],flag1,flag2,n;
    fin>>T;
    for(n=0;n<T;n++)
    {
        flag1 = 0;
        flag2 = 0;

        for(i=0;i<17;i++) arr[i]=0;
        fin>>x;
        x--;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
            fin>> a1[i][j];

        fin>>y;
        y--;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
            fin>> a2[i][j];

        for(j=0;j<4;j++) arr[a1[x][j]]++;
        for(j=0;j<4;j++) arr[a2[y][j]]++;
        for(i=1;i<17;i++)
        {
            if(arr[i]==2)
            {
                if(flag1>=1)
                    flag1=2;
                else
                {
                    flag1=1;
                    flag2=i;
                }
            }
        }
        cout<<"Case #"<<n+1<<": ";
        if(flag1==0) cout<<"Bad magician!";
        else if(flag1==2) cout<<"Volunteer cheated!";
        else cout<<flag2;
        cout<<endl;

        fout<<"Case #"<<n+1<<": ";
        if(flag1==0) fout<<"Volunteer cheated!";
        else if(flag1==2) fout<<"Bad magician!";
        else fout<<flag2;
        fout<<endl;
    }
    return 0;
}
