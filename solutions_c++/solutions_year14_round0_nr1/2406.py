#include <iostream>
#include <algorithm>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <vector>
#include <map>
using namespace std;

int main()
{
    int cas,n,ca=1;
    int num[16][16],cnt[17];
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);

    scanf("%d",&cas);
    while(cas--)
    {
        memset(cnt,0,sizeof(cnt));
        for(int k=0; k<2; k++)
        {
            scanf("%d",&n);
            n--;
            for(int i=0; i<4; i++)
                for(int j=0; j<4; j++)
                    scanf("%d",&num[i][j]);
            for(int i=0; i<4; i++)
                cnt[num[n][i]]++;
        }
        int ans=0;
        int id=0;
        for(int i=1;i<=16;i++)
           if(cnt[i]==2)
           {
               id=i;
               ans++;
           }
        if(ans==1)
           printf("Case #%d: %d\n",ca++,id);
        else if(ans>=2)
           printf("Case #%d: Bad magician!\n",ca++);
        else
           printf("Case #%d: Volunteer cheated!\n",ca++);
    }
    return 0;
}
