//
//  main.c
//  problem1
//
//  Created by Mingliang jiang on 15/4/17.
//  Copyright (c) 2015? Mingliang jiang. All rights reserved.
//

#include <stdio.h>
#include <string.h>

int mushr[1002];
int first(int num1)
{
    int i=0;
    int count=0;
    for(i=1;i<num1;i++)
    {
        if(mushr[i]<mushr[i-1])
        {
            count+=mushr[i-1]-mushr[i];
        }
    }
    
    
    return count;
}
int second(int num1)
{   int i=0;
    int count=0;
    int maxrate=0;
    for(i=1;i<num1;i++)
    {
        if(mushr[i-1]>mushr[i])
        {
            if(mushr[i-1]-mushr[i]>maxrate)
            {
                maxrate=mushr[i-1]-mushr[i];
            }
        }
    }
    for (int i=0;i<num1-1;i++)
    {
        if(mushr[i]<=maxrate)
        {
            count+=mushr[i];
        }
        else
        {
            count+=maxrate;
        }
    }
    return count;
}
int main() {
   
    int num,num1,i=0,tag=1;
   
   	freopen ("A-large.in", "r", stdin);
	freopen("alarge.txt", "w", stdout);
    while(~scanf("%d",&num))
    {
        while (num--) {
        memset(mushr, 0, sizeof(mushr));
        scanf("%d",&num1);
        for (i=0; i<num1; i++)
        {
            scanf("%d",&mushr[i]);
        }
            printf("Case #%d: %d %d\n",tag,first(num1),second(num1));
            tag++;
        }
    }
    
    
    return 0;
}