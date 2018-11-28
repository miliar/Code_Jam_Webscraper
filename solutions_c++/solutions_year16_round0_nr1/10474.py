//
//  main.cpp
//  codeJam16
//
//  Created by Xian Pan on 4/9/16.
//  Copyright (c) 2016 __MyCompanyName__. All rights reserved.
//

#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>

using namespace std;


int lastNum(int n) {
    map<int,bool> my;
    vector<bool> showed(10,false);
    int total=0, i=1;
    int cur=n;
    while(total<10) {
        cur = n*(i++);
        if(my.find(cur)!=my.end()) return -1;
        my[cur]=true;
        int x=cur;
        while(x>0) {
            int temp= x%10; 
            x/=10;
            if(showed[temp]==false) {
                showed[temp]=true;
                total++;
                if(total==10) break;
            }
        }
    }
    return cur;
}

int main (int argc, const char * argv[])
{
    
    FILE *rfp=NULL;
    FILE *wfp=NULL;
    //char *filename = "/tmp/test.txt";
    
    rfp = fopen("/tmp/A-large.in","r");
    if(rfp == NULL)
    {
        printf("open file error\n");
        return 0;
    }
    wfp = fopen("/tmp/A-large.out","a");
    
    int line=0;
    int j;
    //line = fgetc(rfp);
    fscanf(rfp,"%d",&line);
    printf("line=%d\n",line);
    fgetc(rfp);
    
    int in,out;
    for(j=1;j<=line;j++)
    {
        fprintf(wfp,"Case #%d: ",j);
        
        fscanf(rfp,"%d",&in);
        printf("in=%c",in);
        out= lastNum(in);
        if(out!=-1)
            fprintf(wfp,"%d",out);
        else
            fprintf(wfp,"%s","INSOMNIA");
        
        fprintf(wfp,"\n");
    }   
    fclose(rfp);
    fclose(wfp);
    return 0;
}


