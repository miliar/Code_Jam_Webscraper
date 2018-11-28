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
#define MAX_N 505
#define MAX_Q 100
#define MAXK 100000
#define MAX_V 5005
#define MAX_E 100005
#define inf 1000005
using namespace::std;
typedef long long ll;

int mat1[4][4],mat2[4][4];
int r1,r2;
void solve(){
    r1--;r2--;
    int ans=-1,num=0;
    for (int i=0; i<4; i++) {
        for (int j=0; j<4; j++) {
            if (r1>=0&&r1<4&&r2>=0&&r2<4&&mat1[r1][i]==mat2[r2][j]) {
                num++;ans=mat1[r1][i];
            }
        }
    }
    if (num<1) {
        cout<<"Volunteer cheated!"<<endl;
    }
    else if(num==1){
        cout<<ans<<endl;
    }
    else
        cout<<"Bad magician!"<<endl;
}

int main()
{
    freopen("/Users/mascure/Desktop/A-small-attempt1.in", "r", stdin);
    freopen("/Users/mascure/Desktop/A-small-attempt1.out", "w", stdout);
    int caseN;
    cin>>caseN;
    for (int i=1; i<=caseN; i++) {
        cin>>r1;
        for (int j=0; j<4; j++) {
            for (int k=0; k<4; k++) {
                scanf("%d",&mat1[j][k]);
            }
        }
        cin>>r2;
        for (int j=0; j<4; j++) {
            for (int k=0; k<4; k++) {
                scanf("%d",&mat2[j][k]);
            }
        }
        cout<<"Case #"<<i<<": ";
        solve();
    }
    return 0;
}

