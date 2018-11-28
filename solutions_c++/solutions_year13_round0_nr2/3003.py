//
//  main.cpp
//  Lawnmower
//
//  Created by PeterChoi on 13. 4. 13..
//  Copyright (c) 2013년 summerpool. All rights reserved.
//

#include <stdio.h>
#include <string.h>

#define INPUTFILENAME "./B-large.in.txt"
#define OUTPUTFILENAME "./result01.txt"

#define INPUTSTR "%[^\n]s"
#define OUTPUTSTR "Case #%d: %d\'%d\" to %d\'%d\"\n"

#define OPEN_FILE_READ(X) X=fopen(INPUTFILENAME,"r");
#define OPEN_FILE_WRITE(X) X=fopen(OUTPUTFILENAME,"w");
int main(int argc, const char * argv[])
{
    
    FILE * inputF, *outputF;
    
    OPEN_FILE_READ(inputF)
    OPEN_FILE_WRITE(outputF)

    int t;
    
    fscanf(inputF, "%d", &t);
    
    for(int i=0 ; i<t ; i++)
    {
        char temp;
        int map[100][100];
        //int inmap[100][100];
        int n,m;
        
        fscanf(inputF, "%c", &temp);
        
        fscanf(inputF, "%d", &n);
        fscanf(inputF, "%d", &m);
        
        for(int j=0 ; j<n ; j++)
        {
            for(int k=0 ; k<m ; k++)
            {
                fscanf(inputF, "%d", &map[j][k]);
                //inmap[j][k] = 100;
            }
            //fscanf(inputF, "%c",&temp);
        }
        //큰값으로 들러 쌓여있을면 안된다.
        
        bool bb = true;
        
        if(n==1 || m==1)
        {
            bb=true;
        }
//        else if(n==2 || m==2)
//        {
//            if(n==2 && m==2)
//            {
//                if(map[0][0] < map[1][0] && map[0][0] < map[0][1])
//                    bb = false;
//                else if(map[0][1] < map[0][0] && map[0][1] < map[1][1])
//                    bb = false;
//                else if(map[1][0] < map[0][0] && map[1][0] < map[1][1])
//                    bb = false;
//                else if(map[1][1] < map[1][0] && map[1][1] < map[0][1])
//                    bb = false;
//            }
//            else if(n==2)
//            {
//                
//                for(int j=0 ; j<n ; j++)
//                {
//                    if(bb)
//                    {
//                        for(int k=1 ; k<m-1 ; k++)
//                        {
//                            a = map[j][k];
//                            
//                        }
//        
//                    }
//                }
//            }
//            else if(m==2)
//            {
//                
//            }
//        }
        else
        {
            for(int j=0 ; (j<n)&&bb ; j++)
            {
                if(bb)
                for(int k=0 ; k<m ; k++)
                {
                    int a= map[j][k];
                    bool c1,c2,r1,r2;
                    c1=c2=r1=r2 = true;
                    
                    for(int ii=0 ; ii<k ; ii++)
                        if(a < map[j][ii])
                        {
                            c1 = false;
                            break;
                        }
                        else if(ii == k-1)
                        {
                            c1 = true;
                        }
                    
                    for(int jj=k+1 ; jj<m ; jj++)
                        if(a < map[j][jj])
                        {
                            c2 = false;
                            break;
                        }
                    else if(jj == m-1)
                    {
                        c2 = true;
                    }
                    
                    for(int kk=0 ; kk<j ; kk++)
                        if(a < map[kk][k])
                        {
                            r1=false;
                            break;
                        }
                    else if(kk == j-1)
                    {
                        r1 = true;
                    }
                    
                    for(int iii=j+1 ; iii<n ; iii++)
                        if(a<map[iii][k])
                        {
                            r2=false;
                            break;
                        }
                    else if(iii == n-1)
                    {
                        r2 = true;
                    }
                    
                    if(!c1 && !r1)
                    {
                        bb= false;
                        break;
                    }
                    else if(!c1 && !r2)
                    {
                        bb= false;
                        break;
                    }
                    else if(!c2 && !r1)
                    {
                        bb= false;
                        break;
                    }
                    else if(!c2 && !r2)
                    {
                        bb= false;
                        break;
                    }
                    
                    
                }
            }
        }

        
        if(bb)
        {
            fprintf(outputF, "Case #%d: YES\n", i+1);
        }
        else
        {
            fprintf(outputF, "Case #%d: NO\n", i+1);
        }
        
        
    }
    
    
    
    
    fclose(inputF);
    fclose(outputF);
    
    
    return 0;
}

