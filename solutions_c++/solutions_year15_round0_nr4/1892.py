//
//  main.cpp
//  codejam3
//
//  Created by Vatsal Chanana on 11/04/15.
//  Copyright (c) 2015 VC. All rights reserved.
//

#include<iostream>
#include<vector>
#include<cstdio>
#include<algorithm>
#include<utility>
#include<set>
#include<map>
#include<cstring>
#include<cmath>
#include<string>
#include<cstdlib>
#include<queue>
using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        int x,r,c;
        cin>>x>>r>>c;
        bool won=false;
        if(x==1)
        {
            won=true;
        }
        if(x==2)
        {
            if((r*c)%2==0)
            {
                won=true;
            }
        }
        if(x==3 )
        {
            if((r*c)%3==0 && r>1 && c>1)
            {
                won=true;
            }
        }
        if(x==4)
        {
            if((r*c)%4==0 && r>2 && c>2)
            {
                won=true;
            }
        }
        if(won)
        {
            cout<<"Case #"<<i+1<<": "<<"GABRIEL"<<endl;
        }
        else
        {
            cout<<"Case #"<<i+1<<": "<<"RICHARD"<<endl;
        }
    }
}