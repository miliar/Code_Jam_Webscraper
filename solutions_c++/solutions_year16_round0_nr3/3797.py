//
//  main.cpp
//  Coin Jam
//
//  Created by Qiu Xin on 9/4/16.
//  Copyright © 2016 Qiu Xin. All rights reserved.
//

#include <iostream>
#include <cmath>
#include <vector>
using namespace std;


double isPrime(double num)
{
    if (num==2||num==3)
        return 1;
    if (fmod(num,2.0)==0)
        return 2;
    if (fmod(num,3.0)==0)
        return 3;
    double cur=5.0, step=2.0;
    while (cur*cur<=num)
    {
        if (fmod(num,cur)==0)
            return cur;
        cur+=step;
        step=6.0-step;
    }
    return 1;
}

void dfsHelper(string tmp, int curIndex, int& curJ, const int& N, const int& J)
{
    if (curIndex==N-1)
    {
        vector<double> ans;
        double num, curBase, div;
        for (int base=2;base<=10;base++)
        {
            num=0;
            curBase=1;
            for (int i=N-1;i>=0;i--)
            {
                num+=(tmp[i]-'0')*curBase;
                curBase*=base;
            }
            div=isPrime(num);
            if (div==1)
                return;
            ans.push_back(div);
        }
        cout<<tmp;
        for (int i=0;i<9;i++)
            cout<<' '<<ans[i];
        cout<<endl;
        curJ++;
    }
    else
    {
        tmp[curIndex]='0';
        dfsHelper(tmp,curIndex+1,curJ,N,J);
        if (curJ==J)
            return;
        tmp[curIndex]='1';
        dfsHelper(tmp,curIndex+1,curJ,N,J);
    }
    return;
}

int main(int argc, const char * argv[]) {
    int runNum, J, N, curJ=0;
    cin >> runNum;
    for (int i=1;i<=runNum;i++)
    {
        cin >> N;
        cin >> J;
        string tmp(N,'1');
        for (int j=1;j<N-1;j++)
            tmp[j]='0';
        cout<<"Case #"<<i<<':'<<endl;
        dfsHelper(tmp,1,curJ,N,J);
    }
    return 0;
}
