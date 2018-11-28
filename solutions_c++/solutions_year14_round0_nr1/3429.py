#include<iostream>
#include<cstdio>
#include<fstream>
using namespace std;
void findCard(int ar1[4][4],int ar2[4][4],int x,int y,int n)
{
    int ct=0;
    int card;
    for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
        {
            if(ar1[x-1][i]==ar2[y-1][j])
                {
                    ct++;
                    card=ar1[x-1][i];
                }
        }
    fstream fout;
    fout.open("out.txt",ios::out|ios::app);
    if(ct==0)
       fout<<"Case #"<<n-1<<": Volunteer cheated!"<<endl;
    else if(ct==1)
        fout<<"Case #"<<n-1<<": "<<card<<endl;
    else
        fout<<"Case #"<<n-1<<": Bad magician!"<<endl;
    fout.close();
    cout<<ct<<"  "<<card<<endl;
}
int main()
{
    int n;
    int x,y;
    int ar1[4][4];
    int ar2[4][4];
    fstream fin;
    fin.open("A-small-attempt1.in",ios::in);
    fin>>n;
    int i=1;
    while(i++<(n+1))
    {
        fin>>x;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
            fin>>ar1[i][j];
        fin>>y;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
            fin>>ar2[i][j];
           findCard(ar1,ar2,x,y,i);
    }
    fin.close();
}
