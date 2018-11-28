#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;

int main()
{
    int times,row,row2;
    int data1[4][4],data2[4][4];
    freopen("a_small.in","r",stdin);
    freopen("a_small.txt","w",stdout);
    scanf("%d",&times);
    for (int t=0;t<times;t++)
    {
        scanf("%d",&row);
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
                scanf("%d",&data1[i][j]);
        scanf("%d",&row2);
        for (int i = 0; i < 4; i++)
            for (int j = 0; j<4;j++)
                scanf("%d",&data2[i][j]);
        int currentans = 0;
        for (int i = 0; i <4; i++)
        {
            for (int j = 0; j<4;j ++)
            {
                if (data1[row-1][i] == data2[row2-1][j])
                    if (currentans == 0){
                        currentans = data1[row-1][i];
                        break;
                    }
                    else{
                        currentans = -1;
                        break;
                    }
            }
            if (currentans == -1) break;
        }
        printf("Case #%d: ",t+1);
        if (currentans == 0)
            printf("Volunteer cheated!\n");
        else if (currentans == -1)
            printf("Bad magician!\n");
        else
            printf("%d\n",currentans);
    }
}
