#include <set>
#include <map>
#include <queue>
#include <stack>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <limits.h>
#include <string.h>
#include <string>
#include <algorithm>
using namespace std;
int m1[4][4];
int m2[4][4];
bool judge(int a,int b[])
{
    for(int i = 0; i < 4;i++)
    {
        if(a==b[i])return true;
    }
    return false;
}
int main()
{
    //freopen("A-small-attempt5.in","r",stdin);
    //freopen("A-small-attempt5.out","w",stdout);
    int T;
    int r1,r2;
    scanf("%d",&T);
    int ca = 1;
    while(T--)
    {
        scanf("%d",&r1);
        for(int i = 0; i < 4;i++)
        {
            for(int j = 0; j < 4;j++)
            {
                scanf("%d",&m1[i][j]);
            }
        }
        scanf("%d",&r2);
        for(int i = 0; i < 4;i++)
        {
            for(int j = 0; j < 4;j++)
            {
                scanf("%d",&m2[i][j]);
            }
        }
        int cnt = 0,rst;
        for(int i = 0; i < 4;i++)
        {
            if(judge(m1[r1-1][i],m2[r2-1])){
                cnt++;
                rst = m1[r1-1][i];
            }
        }
        printf("Case #%d: ",ca++);
        if(cnt == 0)
        {
            puts("Volunteer cheated!");
        }else if(cnt == 1){
            printf("%d\n",rst);
        }else {
            puts("Bad magician!");
        }

    }
}
