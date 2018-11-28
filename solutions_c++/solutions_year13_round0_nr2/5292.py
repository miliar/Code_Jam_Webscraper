#include <iostream>
#include <cstdio>

using namespace std;

FILE * iFile=fopen("kitten.in", "r");
FILE * oFile=fopen("kitten.out", "w");

int lawn[105][105];
int rows, columns, cases, q;
bool col, row;

void kitten()
{
    fscanf(iFile, "%d%d", &rows, &columns);
        for(int i=1; i<=rows; i++)
        {
            for(int j=1; j<=columns; j++)
            {
                fscanf(iFile, "%d", &lawn[j][i]);
            }
        }
        for(int i=1; i<=rows; i++)
        {
            for(int j=1; j<=columns; j++)
            {
                row=true;
                col=true;
                for(int g=1; g<=columns; g++)
                {
                    if(lawn[g][i]>lawn[j][i])
                    {
                        row=false;
                    }
                }
                for(int g=1; g<=rows; g++)
                {
                    if(lawn[j][g]>lawn[j][i])
                    {
                        col=false;
                    }
                }
                if(col || row)
                {
                }
                else
                {
                    fprintf(oFile, "Case #%d: NO\n", q);
                    return;
                }
            }
        }
        fprintf(oFile, "Case #%d: YES\n", q);
        return;
}

int main()
{
    fscanf(iFile, "%d", &cases);
    for(q=1; q<=cases; q+=1)
    {
        kitten();
    }
    return 0;
}
