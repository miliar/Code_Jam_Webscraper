//
//  main.cpp
//  CodeJam A
//
//  Created by Baker Mohd Anas on 4/12/14.
//  Copyright (c) 2014 Baker Mohd Anas. All rights reserved.
//

#include <iostream>
#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <math.h>

using namespace std;

double naomi[1010],ken[1010];

bool comp(double p, double q)
{
    return p<q;
}

int warScore(int N);
int decWarScore(int N);

int main(int argc, const char * argv[])
{
    freopen("/Users/Baker/Desktop/CodeJam_A/D.in", "r", stdin);
    freopen("/Users/Baker/Desktop/CodeJam_A/D.out", "w", stdout);
    // insert code here...
    
    int Case = 1, test;
    
    scanf("%d",&test);
    int N;
    
    
    while(test--)
    {
        scanf("%d",&N);
        for(int i=0;i<N;i++)
            scanf("%lf", &naomi[i]);
        for(int i=0;i<N;i++)
            scanf("%lf", &ken[i]);
        
        sort(&naomi[0], &naomi[N], comp);
        sort(&ken[0], &ken[N], comp);
        
        int war = warScore(N);
        int dec_war = decWarScore(N);
        
        printf("Case #%d: %d %d\n",Case++, dec_war, war);
    }
    return 0;
}


int warScore(int N)
{
    int ret = 0;
    bool flag[1010];
    memset(flag,0, sizeof(flag));
    for(int i=0;i<N;i++)
    {
        bool t = false;
        for(int j=0;j<N;j++)
            if(flag[j]) continue;
            else if(ken[j]>naomi[i])
            {
                flag[j] = true;
                t = true;
                break;
            }
        if(t) continue;
        ret++;
        for(int j=0;j<N;j++)
            if(flag[j]) continue;
            else {
                flag[j] = true;
                break;
            }
    }
    return ret;
}

int decWarScore(int N)
{
    int i=0, ret = 0;
    if( fabs(1.0-ken[N-1])<1e-7)
    {
        i++; N--;
    }
    
    int start = 0, end = N-1;
    for( ; i<N; i++)
    {
        if(naomi[i]>ken[start])
        {
            ret++;
            start++;
        }
        else {
            end--;
        }
    }
    return ret;
}

