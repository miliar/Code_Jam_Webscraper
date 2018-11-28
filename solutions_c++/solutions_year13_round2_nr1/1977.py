//
//  main.cpp
//  R1_A
//
//  Created by PeterChoi on 13. 5. 4..
//  Copyright (c) 2013년 R1. All rights reserved.
//

#include <iostream>

#define INPUTFILENAME "./A-large.in.txt"
#define OUTPUTFILENAME "./largeresult01.txt"

#define INPUTSTR "%[^\n]s"
#define OUTPUTSTR "Case #%d: %d\n"

#define OPEN_FILE_READ(X) X=fopen(INPUTFILENAME,"r");
#define OPEN_FILE_WRITE(X) X=fopen(OUTPUTFILENAME,"w");


bool isAllFalse(int n, bool* bnn)
{
    for(int i=0 ; i<n ; i++)
    {
        if (bnn[i])
        {
            return false;
        }
    }
    return true;
}

bool nothingTodo(int n, long long& am, int* nn, bool* bnn)
{
    for(int i=0 ; i<n ; i++)
    {
        if(bnn[i])
        {
            if(am > (long long)nn[i])
            {
                am += nn[i];
                bnn[i] = false;
                return false;
            }
        }
    }
    return true;
}


int howmanytrue(int n, bool* bnn)
{
    int a=0;
    for(int i=0 ; i<n ; i++)
    {
        if(bnn[i])
            a++;
    }
    return a;
}

int main(int argc, const char * argv[])
{
    FILE *inputF, *outputF;
    
    OPEN_FILE_READ(inputF)
    OPEN_FILE_WRITE(outputF)
    
    int t;
    fscanf(inputF, "%d",&t);
    
    int a,n;
    int nn[100];
    bool bnn[100];
    
    long long am;
    
    for(int i=0 ; i<t ; i++)
    {
        fscanf(inputF, "%d", &a);
        fscanf(inputF, "%d", &n);
        
        am = a;
        
        for(int j=0 ; j<n ; j++)
        {
            fscanf(inputF, "%d", &nn[j]);
            if(am > nn[j])
            {
                am += nn[j];
                bnn[j] = false;
            }
            else
            {
                bnn[j] = true;
            }
        }
        
        while(isAllFalse(n, bnn) == false)
        {
            if(nothingTodo(n, am, nn, bnn))
            {
                break;
            }
        }
        
        if(isAllFalse(n, bnn))
        {
            fprintf(outputF, OUTPUTSTR, i+1,0);
        }
        else if(am == 1)
        {
            fprintf(outputF, OUTPUTSTR, i+1, howmanytrue(n, bnn));
        }
        else
        {
            if(howmanytrue(n, bnn) == 1)
            {
                fprintf(outputF, OUTPUTSTR, i+1,1);
            }
            else
            {
                
                int an1, an2;
                int mincase;
                int addmote = 1;
                
                mincase = an1 = howmanytrue(n, bnn);
                
                long long amm = am + am - 1;
                
                while (true)
                {
                    if(nothingTodo(n, amm, nn, bnn))
                    {
                        if(isAllFalse(n, bnn))
                        {
                            an2 = howmanytrue(n, bnn);
                            if( mincase > addmote + an2)
                            {
                                mincase = addmote + an2;
                            }
                            break;
                        }
                        else if(amm == 1)
                        {
                            break;
                        }
                        else
                        {
                            an2 = howmanytrue(n, bnn);
                            if( mincase > addmote + an2)
                            {
                                mincase = addmote + an2;
                            }
                            addmote++;
                            amm = amm + amm -1;
                        }
                    }
                }
                
                if(amm == 1)
                {
                    fprintf(outputF, OUTPUTSTR, i+1, an1);
                }
                else if(addmote == 1)
                {
                    fprintf(outputF, OUTPUTSTR, i+1, 1);
                }
                else
                {
                    fprintf(outputF, OUTPUTSTR, i+1, mincase);
                }
                
//                while(isAllFalse(n, bnn) == false)
//                {
//                    if(nothingTodo(n, amm, nn, bnn))
//                    {
//                        break;
//                    }
//                }
//                if(isAllFalse(n, bnn))
//                {
//                    fprintf(outputF, OUTPUTSTR, i+1,1);
//                }
//                else
//                {
//                    an2 = howmanytrue(n, bnn);
//                    
//                    if(an1 - an2 <= 1)
//                    {
//                        fprintf(outputF, OUTPUTSTR, i+1, an1);
//                    }
//                    else
//                    {
//                        fprintf(outputF, OUTPUTSTR, i+1, an2 + 1);
//                    }
//                    
//                }
            }
        }
        
        
    }
    
    
    fclose(inputF);
    fclose(outputF);
    
    return 0;
}

