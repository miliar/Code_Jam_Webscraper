//
//  code1.cpp
//  CP
//
//  Created by Bhargav  on 4/11/15.
//  Copyright (c) 2015 Bhargav . All rights reserved.
//

#include<iostream>
#include<string.h>
#include<stdio.h>

using namespace std;


int main()
{
    int t,sMax,count,standCount,p=1;
    char str[1005];
    
    scanf("%d",&t);
    
    while(t--)
    {
        scanf("%d",&sMax);
        scanf("%s",str);
        count=0;
        standCount=0;
        
        
        for(int i=0;i<=sMax;i++)
        {
            if(standCount>=i)
            {
                standCount+=str[i]-48;
            }
            else
            {
                
                if((str[i]-48)>0)
                {
                    count+=(i-standCount);
                    standCount=i+(str[i]-48);
                }
            }
        }
        
        printf("Case #%d: %d\n",p++,count);
        
        
        
    }
    
    return 0;
}