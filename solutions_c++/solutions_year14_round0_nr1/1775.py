#include <iostream>
#include <stdio.h>
#include <vector>
FILE *fin = fopen("input.txt","r");
FILE *fout = fopen("output.txt","w");
using namespace std;
void pro()
{
    int a1,a2;
    int mapp[2][4][4];

    fscanf(fin,"%d",&a1);
    for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
            fscanf(fin,"%d",&mapp[0][i][j]);
    fscanf(fin,"%d",&a2);
    for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
            fscanf(fin,"%d",&mapp[1][i][j]);
    int cnt=0,x,y;
    for(int i=0;i<4;i++)
    {
        for(int j=0;j<4;j++)
            if(mapp[0][a1-1][i]==mapp[1][a2-1][j])
            {
                cnt++;
                if(cnt==1)
                {
                    x=a1-1;
                    y=i;
                }
            }
    }
    if(cnt==0)
    {
        fprintf(fout,"Volunteer cheated!\n");
    }
    else if(cnt==1)
    {
        fprintf(fout,"%d\n",mapp[0][x][y]);
    }
    else
    {
        fprintf(fout,"Bad magician!\n");
    }
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
    return 0;
}
