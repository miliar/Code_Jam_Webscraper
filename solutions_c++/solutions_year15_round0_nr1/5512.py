//
//  a.cpp
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

#define maxN 10000010
#define maxK 10001
using namespace std;
int n, test;
vector< int > res;
string c;

void solve(int test_)
{
    int temp = 0;
    int cur = c[0] - '0';
    for (int i = 1; i <= n; i++)
        if (c[i] != '0')
        {
            if (cur < i)
            {
                temp += (i - cur);
                cur = i;
            }
            cur += c[i] - '0';
        }
    res[test_] = temp;
}

void readInputData_fstream()
{
    ifstream cin("inputL.in");
    
    cin >> test;
    res.resize(test);
    for (int i = 0; i < test; i++)
    {
        cin >> n;
        cin >> c;
        solve(i);
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
    
    //cin >> n;
    return 0;
    
}
#endif
