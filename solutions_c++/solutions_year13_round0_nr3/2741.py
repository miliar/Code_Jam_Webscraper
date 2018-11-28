//
//  main.cpp
//  FairAndSquare
//
//  Created by PeterChoi on 13. 4. 13..
//  Copyright (c) 2013년 summerpool. All rights reserved.
//

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define INPUTFILENAME "./C-small-attempt1.in.txt"
#define OUTPUTFILENAME "./result00.txt"

#define INPUTSTR "%[^\n]s"
#define OUTPUTSTR "Case #%d: %d\n"

#define OPEN_FILE_READ(X) X=fopen(INPUTFILENAME,"r");
#define OPEN_FILE_WRITE(X) X=fopen(OUTPUTFILENAME,"w");
int main(int argc, const char * argv[])
{
    
    FILE * inputF, *outputF;
    
    OPEN_FILE_READ(inputF)
    OPEN_FILE_WRITE(outputF)
    
    int t;
    fscanf(inputF, "%d",&t);
    
    for(int i=0 ; i<t ; i++)
    {
        int a,b;
        fscanf(inputF, "%d",&a);
        fscanf(inputF, "%d",&b);
        
        int c=0;
        char cc[100];
        int size;
        for(int j=1 ; j<100 ; j++)
        {
            if(j*j >= a && j*j <= b)
            {
                
                sprintf(cc,"%d",j*j);
                size = (int)strlen(cc);
                
                if(size == 1)
                {
                    c++;
                    continue;
                }
                
                for(int k=0 ; k<size/2 ; k++)
                {
                    if(cc[k] != cc[size-1-k])
                    {
                        break;
                    }
                    if(k == size/2 - 1)
                    {
                        char ccc[100];
                        int sizes;
                        sprintf(ccc,"%d",j);
                        sizes = (int)strlen(ccc);
                        
                        if(sizes == 1)
                        {
                            c++;
                        }
                        
                        for(int ii=0 ; ii<sizes/2 ; ii++)
                        {
                            if(ccc[ii] != ccc[sizes-1-ii])
                            {
                                break;
                            }
                            if(ii == sizes/2 -1)
                            {
                                c++;
                            }
                        }
                        
                    
                    }
                }
            }
            else if( j*j > b)
            {
                break;
            }
        }
        
        fprintf(outputF, OUTPUTSTR, i+1, c);
        
    }
    
    
    
    fclose(inputF);
    fclose(outputF);
    
    
    return 0;
}

