//
//  main.cpp
//  hackercup
//
//  Created by L on 15-1-10.
//  Copyright (c) 2015Äê L. All rights reserved.
//

#include <iostream>
#include <stdio.h>
#include <string>
#include <string.h>
#include <math.h>
#include <queue>
using namespace std;

int main(int argc, const char * argv[]) {
    int T,cas = 1;
    int X,R,C;
    freopen("C:\\Users\\L\\Downloads\\D-small-attempt0.in","r",stdin);
    freopen("C:\\Users\\L\\Downloads\\D-small-attempt0.out","w",stdout);
    cin>>T;
    while(T--)
    {
        cout<<"Case #"<<cas++<<": ";
        cin>>X>>R>>C;
        if(X==1)
        {
            cout<<"GABRIEL"<<endl;
        }
        else if(X==2)
        {
            if(R*C%2==0)
                cout<<"GABRIEL"<<endl;
            else
                cout<<"RICHARD"<<endl;
        }
        else if(X==3)
        {
            if(R*C==6 ||R*C==12)
                cout<<"GABRIEL"<<endl;
            else
                cout<<"RICHARD"<<endl;
        }
        else if(X==4)
        {
            cout<<"RICHARD"<<endl;
        }
        else
        {
            cout<<"RICHARD"<<endl;
        }
    }
    return 0;
}
