/* 
 * File:   main.cpp
 * Author: nitin
 *
 * Created on 13 November, 2012, 9:13 PM
 */

#include<iostream>
#include<vector>
#include<fstream>

using namespace std;

char box[4][4];

//2 not completed
//1 won
//0 no complete row/column/diagonal

int getresult(char x)
{
    int count = 0;
    int incomplete = 0;
    //horizontal check
    for(int i=0; i<4;i++)
    {
        for(int j=0;j<4;j++)
        {
            if(box[i][j]==x||box[i][j]=='T')
                count++;
            if(box[i][j]=='.')
                incomplete = 1;
            if(count==4)
                return 1;
        }
        count=0;
    }
    //vertical check
    count = 0;
    for(int i=0; i<4;i++)
    {
        for(int j=0;j<4;j++)
        {
            if(box[j][i]==x||box[j][i]=='T')
                count++;
            if(count==4)
                return 1;
        }
        count=0;
    }
    //diagonal check
    count = 0;
    for(int i=0;i<4;i++)
    {
        if(box[i][i]==x||box[i][i]=='T')
            count++;
        if(count==4)
            return 1;
    }
    count = 0;
    for(int i=0;i<4;i++)
    {
        if(box[i][3-i]==x||box[i][3-i]=='T')
            count++;
        if(count==4)
            return 1;
    }
    if(incomplete == 1)
        return 2;
    return 0;
}

int main()
{
    int t,total,ibox=0,resultx,resulto;
    string line;
    ifstream myfile ("example.txt");
    cin>>t;
    total = t;
    while(t)
    {
        getline(myfile,line);
        for(int i=0; i<line.length();i++)
        {
            box[ibox][i] = line[i];
        }
        ibox++;
        if(line=="")
        {
            t--;
            resultx = getresult('X');
            if(resultx != 1)
            {
                resulto = getresult('O');
            }
            if(resultx == 1)
                cout<<"Case #"<<total-t<<": X won"<<"\n";
            else if(resulto == 1)
                cout<<"Case #"<<total-t<<": O won"<<"\n";
            else if(resultx == 2)
                cout<<"Case #"<<total-t<<": Game has not completed"<<"\n";
            else
                cout<<"Case #"<<total-t<<": Draw"<<"\n";
            //run function to get who won, call for x and o
            ibox=0;
        }
    }
}