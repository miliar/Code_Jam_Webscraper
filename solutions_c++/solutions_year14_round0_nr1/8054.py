#include <iostream>
#include <algorithm>
#include <string>
#include <string.h>
#include <math.h>
#include <fstream>

using namespace std;

int main()
{
    ifstream in;
    ofstream of;
    of.open("output.txt");
    in.open("input.txt");
    long long int t;
    in>>t;
    for(int v=1;v<=t;v++)
    {
        int x,y;
        int mas1[5][5];
        int mas2[5][5];
        in>>x;
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                in>>mas1[i][j];
            }
        }
        in>>y;
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                in>>mas2[i][j];
            }
        }
        int temp=0,tempcard=0;
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                if(mas1[x][i]==mas2[y][j])
                {
                    tempcard=mas1[x][i];
                    temp++;
                }
            }
        }
        if(temp==0)
        {
            of<<"Case #"<<v<<": Volunteer cheated!"<<endl;
        }
        if(temp==1)
        {
            of<<"Case #"<<v<<": "<<tempcard<<endl;
        }
        if(temp>1)
        {
            of<<"Case #"<<v<<": Bad magician!"<<endl;
        }












    }
    return 0;
}
