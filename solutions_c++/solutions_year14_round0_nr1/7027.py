//
//  main.cpp
//  google.code.jam.2014
//
//  Created by Lam Leung Tung on 14年4月12日.
//  Copyright (c) 2014年 Lam Leung Tung. All rights reserved.
//
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cstring>
#include <cstdlib>
#include <string>
#include <vector>
#include <cstdio>

#include <set>
#include <cmath>
using namespace std;
void solve()
{
    //first question
    int board1[4][4];
    int row1;
    cin >> row1;
    for (int i =0; i<4; i++) {
        for (int j=0; j<4; j++) {
            cin >> board1[i][j];
        }
    }
    
    set<int>first;
    for (int i=0;i<4;i++)
    {
        first.insert(board1[row1-1][i]);
    }
    
    //second question
    int board2[4][4];
    int row2;
    cin >> row2;
    for (int i =0; i<4; i++) {
        for (int j=0; j<4; j++) {
            cin >> board2[i][j];
        }
    }
    
    set<int> second;
    for (int i=0;i<4;i++)
    {
        second.insert( board2[row2-1][i]);
    }
    
    vector<int> v(4);
    vector<int>::iterator it;
    it=set_intersection (first.begin(), first.end(), second.begin(), second.end(), v.begin());
    v.resize(it-v.begin());
    if(v.size() == 1)
        cout << v[0] <<endl;
    else if(v.size() >1)
        cout << "Bad magician!"<<endl;
    else if(v.size() ==0)
        cout << "Volunteer cheated!"<<endl;
}
int Main(){
    int testCase;
    cin >> testCase;
    for (int i = 1 ;i <= testCase ;i++ ){
        cout << "Case #" << i << ": ";
        solve();
        
    }
    return 0;
}
int main(int argc, const char * argv[])
{
    freopen("in.in", "r",stdin);
    freopen("out.txt", "w", stdout);
    Main();
    
}

