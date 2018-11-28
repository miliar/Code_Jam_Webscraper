//
//  main.cpp
//  gcj
//
//  Created by Ivan_L on 2015.4.11.
//  Copyright (c) 2015年 Ivan_L. All rights reserved.
//

#include <iostream>
using namespace std;
int main(int argc, const char * argv[]) {
    int T,smax,y;
    int x,xi;
    char c;
    cin>>T;
    for (int i=1;i<=T;i++)
    {
        cin>>smax;
        x=y=0;
        for(int j=0;j<=smax;j++)
        {
            while(cin>>c && (c=='\n' || c=='\t' || c==' '));
            xi=c-'0';
            if(x>=j || xi==0)x+=xi;
            else {
                y+=j-x;
                x=j+xi;
            }
        }
        cout<<"Case #"<<i<<": "<<y<<endl;
    }
    return 0;
}
