//
//  main.cpp
//  Leetcode
//
//  Created by Zimu Wang on 3/25/16.
//  Copyright (c) 2016 Zimu Wang. All rights reserved.
//

#include<iostream>
#include<cmath>
#include<vector>
#include<time.h>
#include<algorithm>
#include<fstream>
using namespace std;

int main()
{
    int cases;
    cin>> cases;
    long number;
    long helper;
    int temp;
    long count;
    int round;
    vector<int> indicator;
    indicator.resize(10);
    
    for (int i=0;i<cases;i++)
    {
        for (int j=0;j<10;j++)
            indicator[j] = 0;
        count=0;
        cin>>number;
        cout<< "Case #"<<i+1<<": ";
        if (number==0) {cout<<"INSOMNIA"<<endl;count=10;}
        round = 1;
        while (count<10)
        {
            helper =round*number;
            while (helper>0)
            {
                temp = helper % 10;
                if (indicator[temp]==0)
                {
                    count++;
                    indicator[temp]=1;
                }
                helper = helper/10;
            }
            round++;
        };
        if (number!=0) cout<<(round-1)*number<<endl;
        
    }
}