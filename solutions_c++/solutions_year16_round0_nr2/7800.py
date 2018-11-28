//
//  main.cpp
//  CodeJam2
//
//  Created by Sanya B. Taneja on 09/04/16.
//  Copyright (c) 2016 Name. All rights reserved.
//

#include <iostream>
#include <string.h>
using namespace std;
char s[100];
void fliparray(int n)
{
    for(int k=0;k<=n;k++)
    {
        if(s[k]=='-')
            s[k]='+';
        else
            s[k]='-';
    }
}
int main()
{
    
    int t, l=1, length=0, j, flip;
    freopen("B-large.in", "r", stdin);
    freopen("output.in", "w", stdout);
    cin>>t;
    while(t>0)
    {
        flip=0;
        scanf("%s",s);
        length=(int)strlen(s);
        for(j=length-1;j>=0;j--)
        {
            if(s[j]=='-')
            {
                flip++;
                fliparray(j-1);
            }
        }
        cout<<"Case #"<<l<<": "<<flip<<"\n";
        l++;
        t--;
    }
    getchar();
    return 0;
    
}

