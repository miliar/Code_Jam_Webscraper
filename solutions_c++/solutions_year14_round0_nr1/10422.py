#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
using namespace std;
int cards1[17][17];
int cards2[17][17];
int main()
{
    int cse=0;
    int t;
    scanf("%d",&t);
    while(t--)
    {
        cse++;
        int ans1,ans2;
        scanf("%d",&ans1);
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                scanf("%d",&cards1[i][j]);
            }
        }
        scanf("%d",&ans2);
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                scanf("%d",&cards2[i][j]);
            }
        }
        int cnt=0;
        int card;
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                if(cards1[ans1][i]==cards2[ans2][j])
                {
                    cnt++;
                    card=cards1[ans1][i];
                }
            }
        }
        if(cnt==0)
        {
            printf("Case #%d: Volunteer cheated!\n",cse);
        }
        else if(cnt==1) printf("Case #%d: %d\n",cse,card);
        else printf("Case #%d: Bad magician!\n",cse);
    }
    return 0;
}
