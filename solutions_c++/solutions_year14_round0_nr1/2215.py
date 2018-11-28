#include<cstdio>
#include<cstdlib>
#include<iostream>

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int T, tc;
    int firstLayout[5][5], secondLayout[5][5];
    int firstRow, secondRow;
    int i,j;
    int ans[5], numAns, curNum;

    cin >> T;

    for(tc=1;tc<=T;tc++)
    {
        cin >> firstRow;

        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                cin >> firstLayout[i][j];
            }
        }

        cin >> secondRow;

        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                cin >> secondLayout[i][j];
            }
        }

        numAns = 0;
        for(i=1;i<=4;i++)
        {
            curNum = firstLayout[firstRow][i];
            for(j=1;j<=4;j++)
            {
                if(secondLayout[secondRow][j] == curNum)
                {
                    ans[numAns++] = curNum;
                    break;
                }
            }
        }

        printf("Case #%d: ", tc);
        if(numAns==1) printf("%d\n", ans[0]);
        else if(numAns==0) printf("Volunteer cheated!\n");
        else printf("Bad magician!\n");
    }


    return 0;
}

