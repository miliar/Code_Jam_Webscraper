//
//  main.cpp
//  Deceitful War
//
//  Created by hijackyan on 4/12/14.
//  Copyright (c) 2014 leetcode. All rights reserved.
//
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;
int cmp(double a, double b)
{
    return a<b;
}
int main(int argc, const char * argv[])
{
    int t,n;
    double a[10001],b[10001];
    bool visita[10001], visitb[10001];
    int i,j,score1 = 0, score2 = 0;
    cin>>t;
    int Case = 1;
    while(t--)
    {
        cin>>n;
        for(i = 0; i < n; i++)
            cin>>a[i];
        for(i = 0; i < n; i++)
            cin>>b[i];
        sort(a,a+n,cmp);
        sort(b,b+n,cmp);
        score1 = score2 = 0;
        memset(visita,0,sizeof(visita));
        int last = 0;
        for(i = 0; i < n; i++)//b
        {
            for(j = last; j < n; j++)//a
            {
                if(b[i] < a[j] && visita[j] == 0)
                {
                    visita[j] = 1;
                    score1 ++;
                    last = j;
                    break;
                }
            }
        }
        memset(visitb,0,sizeof(visitb));

        last = 0;
        for(i = 0; i < n; i++)//a
        {
            for(j = last; j < n; j++)//b
            {
                if(a[i] < b[j] && visitb[j] == 0)
                {
                    visitb[j] = 1;
                    score2 ++;
                    last = j;
                    break;
                }
            }
        }
        score2 = n - score2;
        printf("Case #%d: %d %d\n",Case, score1, score2);
        Case++;
    }
}


