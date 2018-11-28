#include <iostream>
#include <string>
#include <fstream>
#include <cstdio>
using namespace std;
int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0..out", "w", stdout);
    int T;
    int CountT;
    int in1[4][4];
    int in2[4][4];
    int A1, A2;
    int i,j,k,f;
    scanf("%d",&T);
    bool yes;
    bool bad;
    int answer;
    for(CountT=1;T>0;T--,CountT++)
    {
        scanf("%d",&A1);
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                scanf("%d",&in1[i][j]);
            }
        }
        scanf("%d",&A2);
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                scanf("%d",&in2[i][j]);
            }
        }

        yes=false;
        bad=false;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(in1[A1-1][i]==in2[A2-1][j])
                {
                    if(!yes)
                    {
                        yes=true;
                        answer=in1[A1-1][i];
                    }
                    else
                    {
                        bad=true;
                        break;
                    }
                }
            }
        }

        if(bad)
        {
            printf("Case #%d: Bad magician!\n",CountT);
        }
        else if(yes)
        {
            printf("Case #%d: %d\n",CountT,answer);
        }
        else
        {
            printf("Case #%d: Volunteer cheated!\n",CountT);
        }

    }

}
