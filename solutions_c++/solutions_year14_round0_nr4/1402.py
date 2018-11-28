//
//  main.cpp
//  abc
//
//  Created by mascure on 14-3-22.
//  Copyright (c) 2014年 mascure. All rights reserved.
//
#include <iostream>
#include <queue>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <stdio.h>
#include <sstream>
#define MAX_N 1005
#define MAX_Q 100
#define MAXK 100000
#define MAX_V 5005
#define MAX_E 100005
#define inf 1000005
using namespace::std;
typedef long long ll;

int N;
double Na[MAX_N],Ke[MAX_N];
//b相对于a的最优策略下能得到的分数
int opt(double *a,double *b){
    int ans=0;
    bool flag[MAX_N];
    fill(flag, flag+N, false);
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            if (!flag[j]&&b[j]>a[i]) {
                ans++;
                flag[j]=true;
                break;
            }
        }
    }
    return ans;
}
void solve(){
    sort(Na, Na+N);
    sort(Ke, Ke+N);
    int ans=opt(Ke,Na);
    cout<<ans<<" ";
    ans=opt(Na,Ke);
    cout<<N-ans<<endl;
}

int main()
{
    freopen("/Users/mascure/Desktop/D-large.in", "r", stdin);
    freopen("/Users/mascure/Desktop/D-large.out", "w", stdout);
    //freopen("/Users/mascure/Desktop/abc.in", "r", stdin);
    int caseN;
    cin>>caseN;
    for (int i=1; i<=caseN; i++) {
        cin>>N;
        for (int j=0; j<N; j++) {
            scanf("%lf",&Na[j]);
        }
        for (int j=0; j<N; j++) {
            scanf("%lf",&Ke[j]);
        }
        cout<<"Case #"<<i<<": ";
        solve();
    }
    return 0;
}

