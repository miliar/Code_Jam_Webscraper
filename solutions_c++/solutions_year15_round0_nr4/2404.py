//
//  main.cpp
//  omni
//
//  Created by Rafał Stempowski on 11.04.2015.
//  Copyright (c) 2015 Rafał Stempowski. All rights reserved.
//

#include <iostream>

int main(int argc, const char * argv[])

{
    FILE *pFile;
    pFile= fopen("/Users/rafal/Downloads/A-large.in","r");
    
    
    int ile,x,r,c;
    fscanf(pFile, "%d",&ile);
    
    for(int h=0;h<ile;h++)
    {
        fscanf(pFile, "\n%d %d %d", &x,&r,&c);
        
        switch(x)
        {
            case 1:
                
                printf("\nCase #%d: GABRIEL",h+1);
                break;
            case 2:
                if(r*c%2==0)
                    printf("\nCase #%d: GABRIEL",h+1);
                else
                    printf("\nCase #%d: RICHARD",h+1);
                break;
            case 3:
                if(r*c%3==0 && r*c>=6)
                    printf("\nCase #%d: GABRIEL",h+1);
                else
                    printf("\nCase #%d: RICHARD",h+1);
                break;
            case 4:
                if(r*c==12 || r*c==16)
                    printf("\nCase #%d: GABRIEL",h+1);
                else
                    printf("\nCase #%d: RICHARD",h+1);
                break;

        }
        
        
    }

    printf("\n");
    return 0;
}
