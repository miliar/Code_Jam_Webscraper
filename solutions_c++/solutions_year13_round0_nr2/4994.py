#include<iostream>
#include<fstream>
#include<stdlib.h>
#include <string.h>
using namespace std;


int main()
{
ifstream fin("in.in");
ofstream fout("out.out");

int tot, N, M,lawn[101][101]={0},row[101][101]={0},col[101][101]={0};
int *map,i,j,k,x,r,c;

char a[5];

fin>>tot;
fin.getline(a,'\n');

for (i=0;i<tot;i++)
    {
    memset(row,0,101*101*4);
    memset(col,0,101*101*4);

    fin>>N>>M;

    for(j=0;j<N;j++)
        {
        for(k=0;k<M;k++)
            {
            fin>>lawn[j][k];
            }
        }

    for(j=0;j<N;j++)
        {
        for(k=0;k<M;k++)
            {
            row[j][lawn[j][k]]++;
            col[k][lawn[j][k]]++;
            }
        }

int addr = 0,addc=0;

    for(x=1;x<100;x++)
        {
        addc = 0;
        for (r=0;r<N;r++)
            {
            if(row[r][x]==M)
                {
                row[r][x+1]=M;
                row[r][x]=0;
                addc++;
                }
            else
                {
                row[r][x-1]-=addr;
                row[r][x]+=addr;
                if(row[r][x]==M)
                    {
                    row[r][x+1]=M;
                    row[r][x]=0;
                    addc++;
                    }
                }
            }
        addr=0;
        for (c=0;c<M;c++)
            {
            if(col[c][x]==N)
                {
                col[c][x+1]=N;
                col[c][x]=0;
                addr++;
                }
            else
                {
                col[c][x]-=addc;
                col[c][x+1]+=addc;
                if(col[c][x]==N)
                    {
                    col[c][x+1]=N;
                    col[c][x]=0;
                    addr++;
                    }
                }
            }
        }

    int possible = 1;
    for(x=0;x<N;x++)
        {
            if(row[x][100]!=M) possible = 0;
        }
    for(x=0;x<M;x++)
        {
            if(col[x][100]!=N) possible = 0;
        }
    if(possible) fout<<"Case #"<<i+1<<": YES"<<endl;
    else fout<<"Case #"<<i+1<<": NO"<<endl;
    }








return 0;
}
