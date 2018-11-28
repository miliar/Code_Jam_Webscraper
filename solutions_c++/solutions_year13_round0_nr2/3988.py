#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
#include<vector>
#include<fstream>
using namespace std;
int main()
{
    ifstream fin("test.in");
    ofstream fout("test3.out");
    int t=0,k,i,j,flagA,flagB;
    fin>>t;
    for(k=1;k<=t;k++)
    {
       flagA=flagB=0;
       int n,m,x,y;
       fin>>n>>m;
       vector< vector<int> > field(n,vector<int>(m));
       vector< vector<int> > test(n,vector<int>(m));
       for(i=0;i<n;i++)
          for(j=0;j<m;j++)
             fin>>field[i][j];
       for(i=0;i<n;i++)
       {
           for(j=0;j<m;j++)
              {
                 for(x=0,y=j;x<n;x++)
                 {
                     if(field[x][y]>field[i][j])
                     flagA=1;
                     //cout<<field[x][y]<<" "<<field[i][j]<<endl;
                 }
                 for(x=i,y=0;y<m;y++)
                 {
                     if(field[x][y]>field[i][j])
                     flagB=1;
                     //cout<<field[x][y]<<" "<<field[i][j]<<endl;
                 }
                 if(flagA==1 && flagB==1)
                 goto abc;
                 flagA=flagB=0;

              }

       }

              abc:
              if(flagA==1 && flagB==1)
              fout<<"Case #"<<k<<": "<<"NO"<<endl;
              else
              fout<<"Case #"<<k<<": "<<"YES"<<endl;

    }

}
