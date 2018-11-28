//
//  main.cpp
//  Magic Trick
//
//  Created by hijackyan on 4/12/14.
//  Copyright (c) 2014 leetcode. All rights reserved.
//

#include <iostream>
#include <algorithm>
using namespace std;
int main(int argc, const char * argv[])
{
    int t,a[4][4],b[4][4],rowa,rowb,i,j,Case = 1;
    cin>>t;
    while(t--)
    {
        cin>>rowa;
        for(i = 0; i < 4; i++)
            for(j = 0; j < 4; j++)
                cin>>a[i][j];
        cin>>rowb;
        for(i = 0; i < 4; i++)
            for(j = 0; j < 4; j++)
                cin>>b[i][j];
        int count = 0;
        int num = 0;
        for(i = 0; i < 4; i++)
        {
            for(j = 0; j < 4;j++)
            {
                if(a[rowa-1][i] == b[rowb-1][j])
                {
                    count++;
                    num = a[rowa-1][i];
                    break;
                }
            }
        }
        cout<<"Case #"<<Case++<<": ";
        if(count == 1)
            cout<<num<<endl;
        else if(count > 1)
            cout<<"Bad magician!"<<endl;
        else
            cout<<"Volunteer cheated!"<<endl;
        
    }
}

