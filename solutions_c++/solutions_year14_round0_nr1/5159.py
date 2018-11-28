#include <iostream>
#include <string>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <list>
#include <set>
#include <cmath>
#include <cstring>
#include <stdio.h>
#include <string.h>
#include <sstream>
#include <stdlib.h>
#include <vector>

using namespace std;

int CardArrayFirst[5][5], CardArraySecond[5][5];
int temp[5], temp2[5];
int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int cardNo , rowFirst , rowSecond, tCase , i, chk, cnt,CaseNo=1;
    scanf("%d", &tCase);
    while(tCase--)
    {
         cnt = 0;
         scanf("%d", &rowFirst);
         for(i = 0; i<4; i++)
            for(int j= 0; j<4; j++)
              scanf("%d", &CardArrayFirst[i][j]);

         scanf("%d", &rowSecond);
         for(i = 0; i<4; i++)
            for(int j= 0; j<4; j++)
              scanf("%d", &CardArraySecond[i][j]);

         for(i = 0;i<4; i++)
            temp[i] = CardArrayFirst[rowFirst-1][i];
         for(i = 0;i<4; i++)
            temp2[i] = CardArraySecond[rowSecond-1][i];

         for(i = 0; i<4; i++)
         for(int j = 0; j<4; j++)
            if(temp[i] == temp2[j])
            {       chk=temp[i];
                    cnt++;
                    break;
            }
            if(cnt == 1)
                printf("Case #%d: %d\n", CaseNo++ , chk);
            else if(cnt > 1)
                printf("Case #%d: Bad magician!\n", CaseNo++);
            else
                printf("Case #%d: Volunteer cheated!\n", CaseNo++);
    }
    return 0;
}

