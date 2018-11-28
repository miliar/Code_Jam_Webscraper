//
//  main.cpp
//  Problem A. Magic Trick
//
//  Created by 朱 翼 on 14-4-12.
//  Copyright (c) 2014年 朱 翼. All rights reserved.
//



#include <cstdio>
#include <cstring>

int res[20];
int map[5][5];

int main(){
    int t;
    scanf("%d",&t);
    int kase=1;
    while(t--)
    {
        memset(res,0,sizeof(res));
        int n;
        for(int i=0;i<2;i++)
        {
            scanf("%d",&n);
            for(int i=1;i<5;i++)  for(int j=1;j<5;j++)  scanf("%d",&map[i][j]);
            for(int i=1;i<5;i++)  res[map[n][i]]++;
        }
        int flag=0,cnt=0;
        for(int i=1;i<17;i++)
        {
            if(res[i]>=2)
            {
                flag=1;
                cnt++;
            }
        }
        printf("Case #%d: ",kase++);
        if(!flag)
        {
            printf("Volunteer cheated!\n");
        }else{
            if(cnt>1)
            {
                printf("Bad magician!\n");
            }else
            {
                for(int i=1;i<17;i++)
                {
                    if(res[i]==2)
                    {
                        printf("%d\n",i);
                        break;
                    }
                }
            }
        }
    }
    return 0;
}