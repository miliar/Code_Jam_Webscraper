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
    //ifstream fin;
    //fin.open("B-large.in");
    //ofstream fout;
    //fout.open("B-large.out");
    int cases;
    cin>>cases;
    int K,C,S;
    for (int i=0;i<cases;i++)
    {
        cin>>K>>C>>S;
        
        cout<< "Case #"<<i+1<<":";
        for (int j=1;j<=K;j++)
            cout<<" "<<j;
        cout<<endl;

    };
    

}
