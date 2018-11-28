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
    ifstream fin;
    fin.open("B-large.in");
    ofstream fout;
    fout.open("B-large.out");
    int cases;
    fin>>cases;
    string input;
    vector<int> arr;
    vector<int> helper;
    int tail;
    int head;
    int answer;
    for (int i=0;i<cases;i++)
    {
        answer = 0;
        fin>>input;
        arr.resize(input.size());
        for (int j=0;j<input.size();j++)
            if (input[j]=='-')
                arr[j]=0;
            else
                arr[j]=1;
        tail = input.size()-1;
        while (arr[tail]==1)
            tail--;
        
        while (tail>=0)
        {
            
            if (arr[0]==1)
            {
                head=0;
                while (arr[head]==1)
                {
                    arr[head]=0;
                    head++;
                }
                answer++;
                head=0;
                helper.resize(tail-head+1);
                for (int j=0;j<=tail-head;j++)
                    helper[j] = 1 - arr[tail-j];
                answer++;
                for (int j=0;j<=tail-head;j++)
                    arr[j+head] = helper[j];
                
            }
            else{
                head = 0;
                helper.resize(tail-head+1);
                for (int j=0;j<=tail-head;j++)
                    helper[j] = 1 - arr[tail-j];
                answer++;
                for (int j=0;j<=tail-head;j++)
                    arr[j+head] = helper[j];
            };
            while (arr[tail]==1)
                tail--;
        };
        fout<< "Case #"<<i+1<<": "<<answer<<endl;

    }

}
