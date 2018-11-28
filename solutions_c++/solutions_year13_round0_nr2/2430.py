#include <iostream>
#include <stdio.h>
#include <vector>
FILE *fin = fopen("input.in","r");
FILE *fout = fopen("output.txt","w");
using namespace std;
void pro()
{
    int map[100][100],n,m;
    int y[100],x[100];
    fscanf(fin,"%d",&n);
    fscanf(fin,"%d",&m);
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        {
            fscanf(fin,"%d",&map[i][j]);
            x[j]=0;
        }
        y[i]=0;
    }
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        {
            if(map[i][j]>y[i])
                y[i]=map[i][j];
        }
    }
    for(int i=0;i<m;i++)
    {
        for(int j=0;j<n;j++)
        {
            if(map[j][i]>x[i])
                x[i]=map[j][i];
        }
    }
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<m;j++)
        {
            int min=y[i];
            if(y[i]>x[j])
                min=x[j];
            if(min!=map[i][j])
            {
                fprintf(fout,"NO\n");
                return;
            }
        }
    }
    fprintf(fout,"YES\n");
}
int main()
{
    int n;
    fscanf(fin,"%d",&n);
    for(int i=0;i<n;i++)
    {
        fprintf(fout,"Case #%d: ",i+1);
        pro();
    }
}
