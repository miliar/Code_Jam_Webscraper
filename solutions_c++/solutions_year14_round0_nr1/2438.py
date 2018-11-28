#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>
#include <iostream>
using namespace std;
int card1[4][4],card2[4][4];
int main()
{
	freopen("in","r",stdin);
	freopen("out","w",stdout);
    int t;
    int ans,res;
    int nrow1,nrow2;
    while(~scanf("%d",&t))
    {
        ans = 1;
        while(t--)
        {
            scanf("%d",&nrow1);
            for(int i = 0;i<4;i++)
                for(int j = 0;j<4;j++)
                {
                    scanf("%d",&card1[i][j]);
                }
            scanf("%d",&nrow2);
            for(int i = 0;i<4;i++)
                for(int j = 0;j<4;j++)
                {
                    scanf("%d",&card2[i][j]);
                }
            int temp = 0;
            for(int i = 0;i<4;i++)
                for(int j= 0;j<4;j++)
                {
                    if(card1[nrow1-1][i] == card2[nrow2-1][j])
                    {
                        temp++;
                        res = card1[nrow1-1][i];
                    }
                }
            printf("Case #%d: ",ans++);
            if(temp == 0)
                printf("Volunteer cheated!\n");
            if(temp == 1)
                printf("%d\n",res);
            else if(temp >= 2)
                printf("Bad magician!\n");
        }
    }
    return 0;
}

