#include<stdio.h>
#include<algorithm>
#include<queue>
#include<vector>
#include<cstdio>
#include<fstream>
using namespace std;
ifstream fin("B.in");
ofstream fout("B.out");
int pattern[110][110];
int init[110][110];
int colmax[110];
int rowmax[110];
int main()
{
    int T;
    fin>>T;
    for(int t=1;t<=T;t++)
    {
        fout<<"Case #"<<t<<": ";
        int N,M;
        fin>>N>>M;
        for(int i=0;i<N+4;i++)
        rowmax[i]=0;
        for(int i=0;i<M+4;i++)
        colmax[i]=0;
        for(int i=0;i<N;i++)
        {
           for(int j=0;j<M;j++)
           {
               fin>>pattern[i][j];
               colmax[j]=max(colmax[j],pattern[i][j]);
               rowmax[i]=max(rowmax[i],pattern[i][j]);
               init[i][j]=100;
           }
        }
        bool flag=0;
        for(int i=0;i<N;i++)
        {
            for(int j=0;j<M;j++)
            {
               init[i][j]=init[i][j]>colmax[j]?colmax[j]:init[i][j];
               init[i][j]=init[i][j]>rowmax[i]?rowmax[i]:init[i][j];
               if(init[i][j]!=pattern[i][j])
               {
                  flag=1;
                  break;
               }
            }
            if(flag)
            break;
        }
        if(flag)
        fout<<"NO\n";
        else
        fout<<"YES\n";
    }
    return 0;
}
