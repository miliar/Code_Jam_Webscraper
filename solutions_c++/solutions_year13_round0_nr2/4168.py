#include <iostream>
#include <fstream>
#include <limits.h>

using namespace std;

int lawn[100][100];

bool check(int i, int n, int v)
{
    for(int j=0; j<n; j++)
    {
        if(lawn[j][i]>v)
            return false;
    }
    return true;
}

int main()
{
    ifstream fin("lawnmowerin.txt");
    ofstream fout("lawnmowerout.txt");
    int t,n,m;
    fin>>t;
    for (int test=1; test<=t; test++)
    {
        fin>>n>>m;
        for (int i=0; i<n; i++)
        {
            for (int j=0; j<m; j++)
            {
                fin>>lawn[i][j];
            }
        }

        for (int i=0; i<n; i++)
        {
            int prev=lawn[i][0];
            for (int j=0; j<m; j++)
            {
                if(lawn[i][j]>prev)
                    prev=lawn[i][j];
            }
            for (int j=0; j<m; j++)
            {
                if(lawn[i][j]<prev)
                {
                    if(!check(j,n,lawn[i][j]))
                    {
                        fout<<"Case #"<<test<<": NO"<<endl;
                        goto snext;
                    }
                }
            }
        }
        fout<<"Case #"<<test<<": YES"<<endl;
    snext:
    continue;
    }
    return 0;
}
