//
//  b.cpp
//  GoogleCodeJam2015
//
//  Created by Tran Hieu on 4/11/15.
//  Copyright (c) 2015 TranHieu. All rights reserved.
//


#if 1
#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <queue>
#include <stack>
#include <fstream>
#define for1(i,j,k) for (int i=j;i<=k;i++)
#define for2(i,n) for (int i=0;i<n;i++)
#define for1_(i,j,k) for (int i=j;i>=k;i--)
#define for2_(i,n) for (int i=n-1;i>=0;i--)
#define c_s cout.setf(ios::fixed)
#define c_p(x) cout.precision(x)
#define can(x,n) (int)pow(x,1.0/n)
#define mp(x,y) make_pair(x,y)
#define hvi(a,n) next_permutation(a,a+n)
#define Pi 2*asin(1.0)

#define maxN 1001
#define maxK 10001
using namespace std;
int n, test;
vector< int > res;
vector< int > a;
vector< int > c;
int timeMin;

void try_(int cur)
{
    if (cur >= timeMin) return;
    bool done = true;
    for (int i = 0; i < a.size(); i++)
        if (a[i]>0)
            done = false;
    
    if (done)
    {
        timeMin = min(cur, timeMin);
        return;
    }
    
    // an
    for (int i = 0; i < a.size(); i++)
        a[i]--;
    try_(cur + 1);
    for (int i = 0; i < a.size(); i++)
        a[i]++;
    // tim 1 thang de chia
    int pos=-1;
    for (int i = 0; i < a.size(); i++)
        if (a[i] > 0)
            if (pos == -1 || (a[pos] < a[i]))
                pos = i;
    if (a[pos] <= 2)
    {
        timeMin = min(cur + a[pos], timeMin);
        return;
    }
    int temp = a[pos];
    
   // int ii = temp / 2;
    for (int ii = 1; ii <= temp / 2; ii++)
    {
        a[pos] = ii;
        a.push_back(temp - ii);
        try_(cur + 1);
        a[pos] = temp;
        a.pop_back();
    }
    
}

void solve2(int test_)
{
    timeMin = 9;
    try_(0);
    res[test_] = timeMin;
}

void solve(int test_)
{
    int tempRes = 0;
    c.resize(maxN);
    for (int i = 0; i < maxN; i++) c[i] = 0;
    
    for (int i = 0; i < n; i++)
        c[a[i]]++;
    
    for (int i = maxN-1; i >= 1; i--)
        if (c[i] != 0)
        {
            
            if (i == 1)
                tempRes++;
            else
            {
                int j = i - 1;
                int newDiv = i / 2;
                while (j > 0  && !c[j]) j--;
                int t = max(max(newDiv, i - newDiv), j);
                if (t + c[i] <= i)
                {
                    c[newDiv]+=c[i];
                    c[i-newDiv]+=c[i];
                    tempRes += c[i];
                }
                else
                {
                    int timeUse = i - t;
                    tempRes += timeUse;
                    for (int tt = 1; tt <= t; tt++)
                        c[tt] = c[tt+timeUse];
                }
            }
        }
    res[test_] = tempRes;
}
void readInputData_fstream()
{
    ifstream cin("input.in");
    
    cin >> test;
    res.resize(test);
    for (int i = 0; i < test; i++)
    {
        cin >> n;
        a.resize(n, 0);
        for (int j = 0; j < n; j++)
            cin >> a[j];
        solve2(i);
    }
    cin.close();
}
void writeOutputData_fstream()
{
    ofstream cout("output");
    for (int i = 0; i < res.size(); i++)
        cout << "Case #"<< i+1 <<": "<< res[i] << endl;
    cout.close();
}

int main()
{
    //freopen("a.in","r",stdin);
    //freopen("a.out","w",stdout);
    readInputData_fstream();
    writeOutputData_fstream();
    return 0;
    
}
#endif
