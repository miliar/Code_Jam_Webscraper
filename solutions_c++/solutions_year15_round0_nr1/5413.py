//
//  main.cpp
//  GJC
//
//  Created by Rafał Stempowski on 11.04.2015.
//  Copyright (c) 2015 Rafał Stempowski. All rights reserved.
//

#include<stdio.h>
#include<iostream>


int main(int argc, const char * argv[])
{
    int ile,max,sum,need,temp;
    char tmp;
    scanf("%d\n",&ile);
    for(int h=0;h<ile;h++)
    {
        sum=0;
        need=0;
        //std::cin>>max;
        scanf("%d ",&max);
        //scanf("%d", &temp);
        //fseek(stdin,-(max+1),SEEK_END);
        for(int g=0;g<=max;g++)
        {
            if(g>sum)
            {
                need+=g-sum;
                sum=g;
            }
            scanf("%c",&tmp);
            //std::cin>>tmp;
            
            sum+=(int)tmp-'0';
            
        }
        //scanf("\n");
        printf("\nCase #%i: %i",h+1,need);
        
    }
    
    return 0;
}

/*

 1
 4 11111
 
 
5
4 11111
1 09
5 110011
0 1
0 1

*/