//
//  main.cpp
//  gcj
//
//  Created by Julian Wu on 4/12/14.
//  Copyright (c) 2014 Julian Wu. All rights reserved.
//

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void Check(int arra[4][4], int arrb[4][4], int row1, int row2) {
    vector<int> first, second, v(4);
    for (int i = 0; i < 4; ++i) {
        first.push_back(arra[row1-1][i]);
        second.push_back(arrb[row2-1][i]);
    }
    sort(first.begin(), first.end());
    sort(second.begin(), second.end());
    vector<int>::iterator it = set_intersection(first.begin(), first.end(), second.begin(), second.end(), v.begin());
    v.resize(it - v.begin());
    if (v.size() > 1) {
        cout<<"Bad magician!"<<endl;
    } else {
        if (v.size() == 1) {
            cout<<v[0]<<endl;
        } else {
            cout<<"Volunteer cheated!"<<endl;
        }
    }
}

int main(int argc, const char * argv[])
{
    int T, row1, row2, ipt, cnt = 1, res;
    int arr1[4][4], arr2[4][4], dist[4];
    cin>>T;
    
    while(T-- > 0){
        cin>>row1;
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                cin>>arr1[i][j];
            }
        }
        cin>>row2;
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                cin>>arr2[i][j];
            }
        }
        cout<<"Case #"<<cnt++<<": ";
        Check(arr1, arr2,row1, row2);
    }
    return 0;
}

